import os
import httpx
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-obs")

VICTORIALOGS_URL = os.environ.get("NANOBOT_VICTORIALOGS_URL", "http://localhost:9428")
VICTORIATRACES_URL = os.environ.get("NANOBOT_VICTORIATRACES_URL", "http://localhost:10428")


@mcp.tool()
def logs_search(query: str, limit: int = 20) -> str:
    """Search logs using LogsQL query. Example query: '_time:10m service.name:"Learning Management Service" severity:ERROR'"""
    try:
        resp = httpx.get(
            f"{VICTORIALOGS_URL}/select/logsql/query",
            params={"query": query, "limit": limit},
            timeout=10,
        )
        lines = [l for l in resp.text.strip().split("\n") if l]
        results = [json.loads(l) for l in lines[:limit]]
        return json.dumps(results, indent=2)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def logs_error_count(service: str = "Learning Management Service", minutes: int = 60) -> str:
    """Count errors per service over a time window."""
    try:
        query = f'_time:{minutes}m service.name:"{service}" severity:ERROR'
        resp = httpx.get(
            f"{VICTORIALOGS_URL}/select/logsql/query",
            params={"query": query, "limit": 1000},
            timeout=10,
        )
        lines = [l for l in resp.text.strip().split("\n") if l]
        return json.dumps({"service": service, "error_count": len(lines), "minutes": minutes})
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def traces_list(service: str = "Learning Management Service", limit: int = 10) -> str:
    """List recent traces for a service."""
    try:
        resp = httpx.get(
            f"{VICTORIATRACES_URL}/select/jaeger/api/traces",
            params={"service": service, "limit": limit},
            timeout=10,
        )
        data = resp.json()
        traces = data.get("data", [])
        result = []
        for t in traces:
            spans = t.get("spans", [])
            result.append({
                "traceID": t.get("traceID"),
                "spans": len(spans),
                "duration_ms": round(t.get("spans", [{}])[0].get("duration", 0) / 1000, 2) if spans else 0,
                "start": spans[0].get("startTime", "") if spans else "",
            })
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def traces_get(trace_id: str) -> str:
    """Fetch a specific trace by ID and return span hierarchy."""
    try:
        resp = httpx.get(
            f"{VICTORIATRACES_URL}/select/jaeger/api/traces/{trace_id}",
            timeout=10,
        )
        data = resp.json()
        traces = data.get("data", [])
        if not traces:
            return "Trace not found"
        spans = traces[0].get("spans", [])
        result = []
        for s in spans:
            result.append({
                "spanID": s.get("spanID"),
                "operationName": s.get("operationName"),
                "duration_ms": round(s.get("duration", 0) / 1000, 2),
                "tags": {t["key"]: t["value"] for t in s.get("tags", []) if t["key"] in ["error", "http.status_code", "db.statement"]},
            })
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {e}"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
