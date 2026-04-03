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

- When the user asks about errors, call `mcp_obs_logs_error_count` first to see how many there are
- Then call `mcp_obs_logs_search` to inspect details and extract `trace_id` from the logs
- If a `trace_id` is found, call `mcp_obs_traces_get` to see the full request path
- Summarize findings concisely — do NOT dump raw JSON
- For LMS backend queries, use service name "Learning Management Service"
- Default time window is 10 minutes unless user specifies otherwise
- Report: number of errors, which operation failed, and what the root cause appears to be
