# Lab 8 Report

## Task 1A — Bare agent

### Question 1: What is the agentic loop?

The agentic loop is the core cycle that an AI agent follows to accomplish tasks
autonomously. Instead of a simple one-shot request → response pattern, an agent
iterates through a loop of:
1. Perceive — Receive the user's request and observe the current state (files, tools, context).
2. Think / Plan — Reason about what needs to be done, break the task into steps, and decide on the next action.
3. Act — Execute an action: call a tool, run a command, read/write a file, search the web, etc.
4. Observe — See the result of that action (output, error, file contents).
5. Repeat — Re-evaluate: Is the task done? If not, go back to step 2 with the new information.

This loop continues until the task is complete or a stopping condition is met (max iterations, user intervention, etc.).

### Question 2: What labs are available in our LMS?

The agent answered from local documentation (no live backend access at this stage):
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. Lab 08 — lab-08

## Task 1B — Agent with LMS tools

### Question 1: What labs are available?

1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

(Real data returned via MCP lms_labs tool from the backend.)

### Question 2: Is the LMS backend healthy?

The agent called lms_health and confirmed the backend is healthy.

## Task 1C — Skill prompt

### Question: Show me the scores

The agent responded:

"I'll check what labs are available first.

Here are the available labs. Which one would you like to see scores for?
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08"

The skill prompt correctly guides the agent to call lms_labs first when no lab is specified.
