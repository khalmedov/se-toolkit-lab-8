# Lab 8 Report

## Task 1A — Bare agent

### Q: What is the agentic loop?

The agentic loop is the core cycle that an AI agent follows to accomplish tasks
autonomously. Instead of a simple one-shot request → response pattern, an agent
iterates through a loop of:
1. Perceive — Receive the user's request and observe the current state (files, tools, context).
2. Think / Plan — Reason about what needs to be done, break the task into steps, and decide on the next action.
3. Act — Execute an action: call a tool, run a command, read/write a file, search the web, etc.
4. Observe — See the result of that action (output, error, file contents).
5. Repeat — Re-evaluate: Is the task done? If not, go back to step 2 with the new information.

This loop continues until the task is complete or a stopping condition is met (max iterations, user intervention, etc.).

### Q: What labs are available in our LMS?

The agent did not have live backend access at this stage and answered from local documentation:

1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. Lab 08 — lab-08

## Task 1B — Agent with LMS tools

### Q: What labs are available?

Here are the available labs:
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

Would you like more details on any specific lab, such as pass rates, completion stats, or top learners?

### Q: Is the LMS backend healthy?

Yes, the LMS backend is healthy! It currently has 56 items.

## Task 1C — Skill prompt

### Q: Show me the scores

I'll check what labs are available first.

Here are the available labs. Which one would you like to see scores for?
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

## Task 2A — Deployed agent

Nanobot gateway started successfully in Docker. Startup log excerpt:

    Using config: /tmp/config.resolved.json
    Starting nanobot gateway version 0.1.4.post5 on port 18790...
    WebChat channel enabled
    Channels enabled: webchat
    MCP server lms: connected, 9 tools registered
    MCP server webchat: connected, 1 tools registered
    Agent loop started

## Task 2B — Web client

Flutter web client accessible at http://10.93.25.106:42002/flutter

Agent responses from the web client:

**Q: How is the backend doing?**
The backend is healthy! It's currently managing 56 items. Everything looks good.

**Q: Show me the scores**
Which lab would you like to see scores for? Here are the available options:
1. Lab 01 - Products, Architecture & Roles
2. Lab 02 - Run, Fix, and Deploy a Backend Service
3. Lab 03 - Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 - Testing, Front-end, and AI Agents
5. Lab 05 - Data Pipeline and Analytics Dashboard
6. Lab 06 - Build Your Own Agent
7. Lab 07 - Build a Client with an AI Coding Agent
8. lab-08

## Task 3A — Structured logging

Happy-path log entry (JSON from VictoriaLogs):
```json
{"_msg":"request_completed","event":"request_completed","service.name":"Learning Management Service","severity":"INFO","status":"200","method":"GET","path":"/items/","duration_ms":"67","trace_id":"eb97fe15d658e4a6809ffe0f852631d8","span_id":"12cf27ea2999a130","_time":"2026-04-03T20:19:30.364908288Z"}
```

Error-path log entry (JSON from VictoriaLogs, after stopping PostgreSQL):
```json
{"_msg":"db_query","event":"db_query","service.name":"Learning Management Service","severity":"ERROR","error":"asyncpg.exceptions.InterfaceError: connection is closed","trace_id":"a95051263f1aedfbeb9e68c9dc4315c2","span_id":"95d00c5a88149103","_time":"2026-04-03T20:29:59.961542912Z"}
```

VictoriaLogs query: `_time:1h service.name:"Learning Management Service" severity:ERROR`
Result: 16 total error entries found, including db_query and items_list_failed_as_not_found events.

## Task 3B — Traces

VictoriaTraces UI accessible at http://10.93.25.106:42002/utils/victoriatraces/select/vmui

Healthy trace: GET /items/ HTTP/1.1 200 OK - spans show request through Learning Management Service with successful db_query.

Error trace: GET /items/ HTTP/1.1 404 - spans show db_query failure with asyncpg connection error when PostgreSQL was stopped.

[Screenshots taken of both traces in VictoriaTraces UI]

## Task 3C — Observability MCP tools

Q: Any LMS backend errors in the last 10 minutes? (normal conditions)

No errors detected in the LMS backend over the last 10 minutes. Everything looks clean!

Q: Any LMS backend errors in the last 10 minutes? (after stopping PostgreSQL)

Yes, there are 2 errors in the last 10 minutes, both database-related:
1. Connection closed - asyncpg.exceptions.InterfaceError: connection is closed on a SELECT query against the item table.
2. DNS resolution failure - [Errno -2] Name or service not known during another db_query operation.
Both errors occurred around 20:29 UTC and point to database connectivity issues.
