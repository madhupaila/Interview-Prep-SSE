"""Schema reference for DSA question data modules (not loaded by the generator).

Each _data_<pattern>.py exposes a list named QUESTIONS of dicts:

QUESTION = {
    "slug": "two-sum",                 # required, kebab-case, unique within pattern+tier
    "title": "Two Sum",                # required
    "pattern": "arrays-hashing",       # required, must be a key in PATTERNS (generator)
    "tier": "A",                       # required: "A" | "B" | "C"
    "companies": "Google, Amazon",     # required, comma-separated
    "difficulty": "Easy",              # required: Easy | Medium | Hard
    "cue": "unsorted + find pair ...", # required, the recognition memory hook
    "problem": "Given ...",            # required, problem statement (markdown ok)
    "solution": "def two_sum(...): ...",  # required, full runnable Python (triple-quoted)

    # optional:
    "leetcode": 1,                     # LeetCode number
    "clarify": ["...", "..."],         # clarifying questions
    "approaches": [("Brute force", "O(N^2)", "O(1)", "all pairs"),
                   ("Hashmap", "O(N)", "O(N)", "complement lookup")],
    "identify": "Why this pattern ...",
    "time": "O(N)",
    "space": "O(N)",
    "edges": ["empty", "no answer"],
    "followups": ["sorted input?", "k-sum?"],
    "related": ["two-sum-ii", "3sum"],
}

Run `python _generate_dsa_questions.py` from the track root to (re)generate.
"""
