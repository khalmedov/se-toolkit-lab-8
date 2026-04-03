---
name: observability
description: Use observability MCP tools to query logs and traces
always: true
---

# Observability Skill

You have access to the following observability tools:
- `mcp_obs_logs_search` — search logs with LogsQL query
- `mcp_obs_logs_error_count` — count errors for a service over a time window
- `mcp_obs_traces_list` — list recent traces for a service
- `mcp_obs_traces_get` — fetch a specific trace by ID

## Strategy

### When the user asks "What went wrong?" or "Check system health":
1. Call `mcp_obs_logs_error_count` with minutes=10 for service "Learning Management Service"
2. Call `mcp_obs_logs_search` with query `_time:10m service.name:"Learning Management Service" severity:ERROR` to get details and extract trace_id
3. Call `mcp_obs_traces_get` with the most recent trace_id found
4. Write ONE concise summary that mentions: which service failed, which operation failed, what the root cause is (from logs), and what the trace shows

### When the user asks about errors:
- Call `mcp_obs_logs_error_count` first
- If errors > 0, call `mcp_obs_logs_search` to get details
- Extract trace_id and call `mcp_obs_traces_get`
- Summarize concisely — do NOT dump raw JSON

### Rules:
- Default time window: 10 minutes
- For LMS backend: service name is "Learning Management Service"
- Always cite both log evidence AND trace evidence in investigation responses
- Name the affected service and the root failing operation explicitly
