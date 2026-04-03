---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to the following LMS tools:
- `lms_health` — check if the LMS backend is healthy
- `lms_labs` — list all available labs
- `lms_pass_rates` — get pass rates for a specific lab (requires lab_id)
- `lms_scores` — get scores for a specific lab (requires lab_id)
- `lms_completion` — get completion stats for a specific lab (requires lab_id)
- `lms_top_learners` — get top learners for a specific lab (requires lab_id)
- `lms_groups` — get group breakdown for a specific lab (requires lab_id)
- `lms_timeline` — get submission timeline for a specific lab (requires lab_id)

## Strategy

- If the user asks about scores, pass rates, completion, groups, timeline, or top learners **without naming a lab**, call `lms_labs` first to get the list, then ask the user which lab they want.
- If multiple labs are available, present them as a numbered list and ask the user to choose.
- Use each lab title as the user-facing label.
- Once the user picks a lab, call the appropriate tool with that lab_id.
- Format numeric results nicely: show percentages with 1 decimal place, counts as integers.
- Keep responses concise — show the key numbers, not raw JSON.
- If the user asks "what can you do?", explain that you can show lab lists, pass rates, scores, completion stats, top learners, group breakdowns, and submission timelines using live LMS data.
