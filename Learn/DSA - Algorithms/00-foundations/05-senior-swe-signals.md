# Senior SWE Signals — DSA Rounds

At 3–5 YOE, interviewers expect more than a correct answer. These signals separate **Senior** from **Mid**.

---

## Senior Signals Checklist

| Signal | What it looks like |
|--------|-------------------|
| **Pattern fluency** | Names the pattern in <60s, justifies from cues |
| **Complexity-first thinking** | Derives target complexity from N before coding |
| **Brute → optimal** | Always has a working baseline, then improves deliberately |
| **Clean code** | Helper functions, clear names, no dead code |
| **Edge-case discipline** | Empty, single, duplicates, overflow, negatives — unprompted |
| **Self-testing** | Dry-runs and finds own bugs |
| **Tradeoff articulation** | "Hashmap is O(N) space; two pointers is O(1) but needs sorting" |
| **Communication** | Thinks out loud, takes hints gracefully |

---

## Red Flags Interviewers Notice

- Jumping to code before understanding the problem
- Silent for minutes
- Can't state complexity
- Only one approach, no awareness of alternatives
- Ignores edge cases until prompted
- Defensive when given a hint
- Messy variable names (`a`, `b`, `temp`, `temp2`)

---

## How to Show Seniority

1. **Drive the structure** — run UMPIRE without being asked.
2. **Quantify** — "N is up to 10^5, so I need at least O(N log N)."
3. **Generalize** — "This is the same sliding-window idea as longest-substring problems."
4. **Discuss scale** — "If this ran in production on a stream, I'd…"
5. **Test like an engineer** — write the assertions you'd put in code.

---

## Mock Self-Grading Rubric

| Score | Criteria |
|-------|----------|
| 5/5 | Correct + optimal + clean + self-tested + complexity + tradeoffs, all proactively |
| 4/5 | Correct optimal; needed a small hint or missed one edge case |
| 3/5 | Working solution but not optimal, or messy; complexity correct |
| 2/5 | Brute force only; struggled to optimize |
| 1/5 | Incorrect or couldn't code the idea |

**Target before interviewing:** consistent 4–5 on Tier A and Tier B questions.

---

## The Senior Mindset

> "I don't memorize solutions — I recognize patterns. Given any new problem, I extract the cues, match a pattern, recall its template, adapt it, and reason about complexity. That's repeatable under pressure."

---

## Related

- [Interview Round Flow](04-interview-round-flow.md)
- [Pattern Master Index](../01-patterns/00-pattern-master-index.md)
