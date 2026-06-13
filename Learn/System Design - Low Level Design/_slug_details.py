#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Problem-specific overrides per slug — clarifying Qs, APIs, sequences, scripts."""

from __future__ import annotations


def _seq(*lines: str) -> str:
    return "\n".join(lines)


# slug -> dict of optional override fields
OVERRIDES: dict[str, dict] = {
    "library-management": {
        "clarify": [
            ("Physical or digital books?", "Physical copies with ISBN; e-books extension"),
            ("Multiple branches?", "Single library MVP; branchId extension"),
            ("Loan period?", "14 days default; configurable per item type"),
            ("Reservation queue?", "Yes — FIFO when all copies checked out"),
            ("Fine calculation?", "Per day overdue; FineStrategy injectable"),
            ("Librarian roles?", "Member vs Librarian for catalog edits"),
            ("Concurrent checkout desks?", "Yes — synchronize per BookItem"),
            ("Search scope?", "By title, author, ISBN"),
        ],
        "functional": [
            "Checkout BookItem to Member if available and loan limit OK",
            "Return item, compute overdue fine, notify reservation queue",
            "Reserve Book when no copies available — FIFO queue",
            "Librarian add/remove catalog items",
        ],
        "methods": [
            "Loan checkout(Member member, String barcode)",
            "void returnItem(String barcode)",
            "void reserve(Member member, String isbn)",
            "BigDecimal calculateFine(Loan loan)",
        ],
        "verbs": "`checkout(member, barcode)`, `returnItem(barcode)`, `reserve(member, isbn)`",
        "happy_seq": _seq(
            "participant M as Member", "participant L as LendingService", "participant BI as BookItem",
            "M->>L: checkout(barcode)", "L->>BI: isAvailable()", "BI-->>L: true",
            "L->>BI: markBorrowed(member)", "L-->>M: Loan receipt",
        ),
        "fail_seq": _seq(
            "participant M as Member", "participant L as LendingService", "participant BI as BookItem",
            "M->>L: checkout(barcode)", "L->>BI: isAvailable()", "BI-->>L: false",
            "L-->>M: ItemUnavailableException",
        ),
        "concurrency": [
            "Synchronize checkout/return on BookItem — prevent double borrow",
            "Return unknown barcode → NotFoundException",
            "Reserve when copies exist → reject or auto-checkout per policy",
            "Concurrent return + checkout on same item — lock per BookItem",
        ],
        "script": [
            "Library owns Book metadata and physical BookItem copies with unique barcodes.",
            "Member borrows a BookItem, not an abstract Book — one copy one borrower.",
            "checkout validates membership, item availability, and per-member loan limit.",
            "return computes overdue days via FineStrategy, frees item, wakes ReservationQueue.",
            "ReservationQueue is FIFO per ISBN — fair ordering when copy returns.",
            "CatalogService separated from LendingService — ISP for librarian operations.",
            "FineStrategy injected — daily rate vs flat fee without changing return loop.",
            "HLD: catalog in DB, search via Elasticsearch; LLD entities map cleanly.",
        ],
        "followups": [
            "How to support inter-library loan?",
            "Design notification when reserved book becomes available?",
            "How to handle lost book replacement fees?",
            "Index structure for fast ISBN lookup?",
        ],
    },
    "atm": {
        "clarify": [
            ("Single ATM or bank network?", "Single terminal MVP; network extension"),
            ("Card authentication?", "Insert card + 4-digit PIN"),
            ("Supported operations?", "Withdraw, deposit, balance inquiry, transfer"),
            ("Cash denominations?", "Configurable — $20 bills default in dispenser"),
            ("Daily withdraw limit?", "Per-account limit enforced"),
            ("Concurrent sessions?", "One active session per ATM"),
            ("Receipt printing?", "Optional ReceiptPrinter interface"),
            ("Persistence?", "In-memory BankAccount registry"),
        ],
        "functional": [
            "Authenticate card + PIN before any transaction",
            "Withdraw if sufficient balance and CashDispenser has notes",
            "Deposit increases balance without dispensing",
            "Transfer between accounts at same bank",
        ],
        "methods": [
            "Session authenticate(Card card, String pin)",
            "void withdraw(BigDecimal amount)",
            "void deposit(BigDecimal amount)",
            "BigDecimal getBalance()",
            "void transfer(BankAccount to, BigDecimal amount)",
        ],
        "verbs": "`authenticate(card, pin)`, `withdraw(amount)`, `deposit(amount)`, `transfer(to, amount)`",
        "patterns": [("State", "ATM session: idle, authenticated, transaction"), ("Strategy", "Transaction type handlers")],
        "happy_seq": _seq(
            "participant U as User", "participant A as ATMService", "participant Auth as AuthenticationService",
            "participant D as CashDispenser", "U->>A: insert card + PIN", "A->>Auth: validate(card, pin)",
            "Auth-->>A: session", "U->>A: withdraw(100)", "A->>D: dispense(100)", "A-->>U: cash + receipt",
        ),
        "fail_seq": _seq(
            "participant U as User", "participant A as ATMService", "participant Acct as BankAccount",
            "U->>A: withdraw(10000)", "A->>Acct: checkBalance()", "Acct-->>A: insufficient",
            "A-->>U: InsufficientFundsException",
        ),
        "concurrency": [
            "One session per ATM — synchronized session state",
            "Insufficient funds → InsufficientFundsException",
            "Wrong PIN 3 times → CardRetainedException",
            "Dispenser empty → TemporarilyUnavailableException",
        ],
        "script": [
            "ATM is a facade over authentication, account operations, and cash hardware.",
            "Session state machine: IDLE until card inserted, AUTHENTICATED after PIN, back to IDLE on eject.",
            "AuthenticationService validates PIN against Card — not stored on ATM.",
            "Withdraw checks balance, daily limit, then asks CashDispenser for note combination.",
            "Deposit updates balance immediately — no cash validation in MVP.",
            "Transfer debits source, credits target atomically on same bank.",
            "Transaction log records every operation for audit.",
            "HLD: ATM connects to core banking via secure API; LLD models terminal behavior.",
        ],
        "followups": [
            "How to model cash denomination optimization in dispenser?",
            "Design for ATM network with shared cash management?",
            "How to prevent concurrent sessions on same card?",
            "Rollback if dispense fails after debit?",
        ],
    },
    "lru-cache": {
        "clarify": [
            ("Capacity fixed or dynamic?", "Fixed at construction"),
            ("Thread-safe?", "Single-threaded MVP; concurrent variant separate"),
            ("Eviction policy?", "Least Recently Used only"),
            ("Null keys/values allowed?", "No — reject null"),
            ("get() behavior on miss?", "Return null or Optional.empty"),
            ("put() on existing key?", "Update value and mark most recent"),
            ("Time complexity requirement?", "O(1) get and put"),
            ("Persistence?", "In-memory only"),
        ],
        "functional": [
            "get(key) returns value and marks entry most recently used",
            "put(key, value) inserts or updates; evicts LRU when at capacity",
            "O(1) operations via HashMap + doubly linked list",
            "Evict least recently used entry when size exceeds capacity",
        ],
        "methods": ["V get(K key)", "void put(K key, V value)", "int size()", "void clear()"],
        "verbs": "`get(key)`, `put(key, value)`",
        "patterns": [("Composite", "HashMap + DLL working together"), ("Template", "EvictionPolicy hook optional")],
        "happy_seq": _seq(
            "participant C as Client", "participant L as LRUCache", "participant H as HashMap",
            "C->>L: put(A,1)", "C->>L: put(B,2)", "C->>L: get(A)", "L->>H: lookup(A)",
            "H-->>L: node", "L->>L: moveToHead(node)", "L-->>C: 1",
        ),
        "fail_seq": _seq(
            "participant C as Client", "participant L as LRUCache",
            "C->>L: put(D,4) at capacity", "L->>L: evict tail (LRU)", "C->>L: get(evictedKey)",
            "L-->>C: null",
        ),
        "concurrency": [
            "Single-threaded — no locking needed in MVP",
            "Capacity 0 → reject put or no-op per design choice",
            "get on missing key → return null",
            "put same key → update in place, no size change, mark MRU",
        ],
        "script": [
            "LRUCache combines HashMap for O(1) lookup with doubly linked list for recency order.",
            "Each Node holds key, value, prev, next pointers.",
            "get: lookup node in map; if miss return null; else move node to head and return value.",
            "put: if key exists update value and move to head; else add at head, evict tail if over capacity.",
            "Dummy head/tail sentinels simplify edge cases — no null checks on insert.",
            "Eviction removes tail.prev from both list and map.",
            "This is classic LLD — interviewer may ask concurrent version next.",
            "HLD: distributed cache uses Redis with TTL; LLD teaches local eviction logic.",
        ],
        "followups": [
            "Design thread-safe LRU cache?",
            "How to add TTL expiry alongside LRU?",
            "Implement LFU instead — what changes?",
            "How would Redis implement approximate LRU?",
        ],
    },
    "rag-orchestrator": {
        "clarify": [
            ("Distributed or in-process?", "In-process object model; vector DB is HLD"),
            ("Swappable components?", "Retriever, Reranker, Generator as interfaces"),
            ("Streaming response?", "Extension via StreamAggregator"),
            ("Safety filters?", "Extension — GuardrailChain on input/output"),
            ("Multi-tenant?", "Optional tenantId in Query context"),
            ("Token budget?", "Yes — truncate context before generate"),
            ("Citation required?", "Return source ids with RetrievedChunk"),
            ("Reranker optional?", "Yes — passthrough if not injected"),
        ],
        "functional": [
            "answer(query) → retrieve → rerank → assemble context → generate",
            "Pluggable retriever (keyword stub, vector stub)",
            "Token budget awareness before generation",
            "Return answer with optional source citations",
        ],
        "methods": [
            "String answer(Query query)",
            "List<RetrievedChunk> retrieve(Query query)",
            "String assemble(List<RetrievedChunk> chunks)",
        ],
        "verbs": "`answer(Query)`, `retrieve(Query)`, `assemble(chunks)`",
        "patterns": [("Pipeline", "Sequential stages with shared Query context"), ("Strategy", "Swappable Retriever/Reranker/Generator")],
        "happy_seq": _seq(
            "participant U as User", "participant R as RAGOrchestrator", "participant Ret as Retriever",
            "participant Rank as Reranker", "participant G as Generator",
            "U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: chunks",
            "R->>Rank: rerank(query, chunks)", "Rank-->>R: topK", "R->>G: generate(query, context)",
            "G-->>R: answer", "R-->>U: answer + citations",
        ),
        "fail_seq": _seq(
            "participant U as User", "participant R as RAGOrchestrator", "participant Ret as Retriever",
            "U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: empty",
            "R-->>U: NoContextException",
        ),
        "concurrency": [
            "Pipeline stages sequential in MVP — parallel retrieve+embed is HLD",
            "Empty retrieval → NoContextException or fallback message",
            "Token overflow → TruncationStrategy trims oldest chunks",
            "Generator timeout → wrap in CompletableFuture at HLD layer",
        ],
        "script": [
            "RAGOrchestrator coordinates retrieve-rerank-generate pipeline behind single answer() API.",
            "Query carries user text, tenantId, maxTokens, and metadata.",
            "Retriever interface abstracts vector DB — LLD uses in-memory stub.",
            "Reranker re-scores chunks; default passthrough if not configured.",
            "ContextAssembler builds prompt string respecting TokenBudget.",
            "Generator interface wraps LLMProvider — returns completion text.",
            "Each stage is independently testable with mocks — OCP.",
            "HLD adds Pinecone, embedding service, queue; LLD pipeline shape unchanged.",
        ],
        "followups": [
            "How to add hybrid retrieval (keyword + vector)?",
            "Design streaming answer with partial citations?",
            "How to cache retrieval results per query hash?",
            "Evaluate retrieval quality — what metrics?",
        ],
        "hld": "02-genai-llm-hld/questions/Q02-rag-document-qa.md",
    },
    "decorator-coffee": {
        "clarify": [
            ("Which add-ons?", "Milk, whip, caramel, extra shot — each adds cost"),
            ("Base beverages?", "Espresso, HouseBlend, DarkRoast"),
            ("Can add-ons stack?", "Yes — milk + whip on same base"),
            ("Size variants?", "Extension — Tall/Grande via decorator or enum"),
            ("Discount rules?", "Extension — CouponDecorator"),
            ("Takeaway vs dine-in?", "Out of scope"),
            ("Recipe display?", "getDescription() returns full stack string"),
            ("Pricing source?", "Each component reports getCost()"),
        ],
        "functional": [
            "Compose beverage from base + zero or more add-on decorators",
            "getCost() sums base and all decorator prices",
            "getDescription() lists full recipe chain",
            "Add decorators at runtime — open for extension",
        ],
        "methods": [
            "BigDecimal getCost()",
            "String getDescription()",
            "Beverage addMilk()",
            "Beverage addWhip()",
        ],
        "verbs": "`getCost()`, `getDescription()`, `addMilk()`, `addWhip()`",
        "patterns": [("Decorator", "Wrap Beverage with add-ons dynamically"), ("Component", "Beverage interface unifies base and decorated")],
        "service": "CoffeeShop",
        "happy_seq": _seq(
            "participant C as Customer", "participant S as CoffeeShop", "participant B as Beverage",
            "C->>S: order(espresso + milk + whip)", "S->>B: new Espresso()", "S->>B: wrap MilkDecorator",
            "S->>B: wrap WhipDecorator", "B-->>S: getCost()", "S-->>C: total + description",
        ),
        "fail_seq": _seq(
            "participant C as Customer", "participant S as CoffeeShop",
            "C->>S: order(unknownType)", "S-->>C: UnknownBeverageException",
        ),
        "concurrency": [
            "Immutable decorator chain — thread-safe after construction",
            "Unknown base type → UnknownBeverageException",
            "Null wrap target → NullPointerException — validate in constructor",
            "Deep stack — no hard limit in MVP",
        ],
        "script": [
            "Beverage interface declares getCost() and getDescription().",
            "Concrete bases: Espresso, HouseBlend implement Beverage directly.",
            "Decorator abstract class implements Beverage and holds wrapped Beverage.",
            "MilkDecorator adds milk cost/description delegating to inner beverage.",
            "Customer order builds chain: new MilkDecorator(new WhipDecorator(new Espresso())).",
            "Open-Closed: new add-on = new Decorator subclass, no change to existing code.",
            "Contrast with subclass explosion — Latte extends EspressoWithMilk extends...",
            "This is canonical Gang-of-Four Decorator interview question.",
        ],
        "followups": [
            "Decorator vs subclassing for add-ons?",
            "How to serialize order for receipt?",
            "Add size as decorator or property?",
            "Remove an add-on from middle of chain?",
        ],
    },
    "thread-safe-singleton": {
        "clarify": [
            ("Lazy or eager init?", "Lazy — created on first getInstance()"),
            ("Which approach?", "Double-checked locking or enum singleton"),
            ("Reflection attack?", "Enum singleton prevents; DCL needs guard"),
            ("Serialization?", "readResolve for DCL; enum handles automatically"),
            ("Subclassing?", "No — private constructor"),
            ("Testability?", "Package-private ctor for tests or reset hook"),
            ("Multiple class loaders?", "Edge case — one instance per loader"),
            ("Java version?", "volatile + DCL safe since Java 5"),
        ],
        "functional": [
            "getInstance() returns same instance across all threads",
            "Lazy initialization on first access",
            "Thread-safe without global synchronized bottleneck after init",
            "Prevent duplicate instance via private constructor",
        ],
        "methods": ["static Singleton getInstance()", "void configure(String key, String value)"],
        "verbs": "`getInstance()`, `configure(key, value)`",
        "patterns": [("Singleton", "Single instance guarantee"), ("Holder", "Initialization-on-demand holder idiom")],
        "happy_seq": _seq(
            "participant T1 as Thread1", "participant T2 as Thread2", "participant S as Singleton",
            "T1->>S: getInstance()", "T2->>S: getInstance()", "S-->>T1: instance",
            "S-->>T2: same instance",
        ),
        "fail_seq": _seq(
            "participant T as Thread", "participant S as Singleton",
            "T->>S: new Singleton()", "S-->>T: compile error — private ctor",
        ),
        "concurrency": [
            "DCL: volatile instance + synchronized block on first create",
            "Enum singleton — preferred for simplicity and serialization safety",
            "No locking after instance published — performance",
            "Class loading initializes holder only when referenced",
        ],
        "script": [
            "Singleton ensures exactly one instance in the JVM.",
            "Enum approach: public enum Singleton { INSTANCE; } — Joshua Bloch recommended.",
            "DCL: check null, synchronize, check null again, construct with volatile field.",
            "Holder idiom: static nested class holds instance — lazy and thread-safe via class init.",
            "Avoid synchronized getInstance() every call — performance bottleneck.",
            "Private constructor blocks external new; reflection needs test awareness.",
            "ConfigManager example: singleton holds app settings loaded once.",
            "In DI frameworks singleton is container-scoped — different lifecycle.",
        ],
        "followups": [
            "Why is volatile required in DCL?",
            "Enum vs DCL — when to pick each?",
            "How to test code that calls getInstance()?",
            "Singleton anti-pattern in microservices?",
        ],
    },
}


def merge_details(slug: str, base: dict) -> dict:
    """Merge slug-specific overrides into base spec dict."""
    ov = OVERRIDES.get(slug, {})
    out = dict(base)
    for k, v in ov.items():
        out[k] = v
    return out


def enrich_generic(slug: str, title: str, service: str, entities: list, iface: str, track: str, problem: str) -> dict:
    """Fill problem-aware defaults when no full override exists."""
    names = [e[0] for e in entities]
    nouns = ", ".join(f"`{n}`" for n in names)
    primary = names[0] if names else "Request"
    method0 = {
        "library-management": "Loan checkout(Member member, String barcode)",
        "hotel-booking": "Booking createBooking(Guest guest, Room room, LocalDateRange dates)",
        "chess": "boolean makeMove(Move move)",
        "vending-machine": "Product selectItem(String code)",
        "rate-limiter": "boolean allowRequest(String clientKey)",
        "logger": "void log(LogLevel level, String message)",
        "splitwise": "void addExpense(Expense expense)",
        "movie-ticket-booking": "Booking confirmSeats(Show show, List<Seat> seats)",
        "shopping-cart": "void addItem(String sku, int quantity)",
        "pubsub-event-bus": "void publish(String topic, Event event)",
        "strategy-payment": "PaymentResult process(PaymentRequest request)",
        "bounded-blocking-queue": "void put(E item)",
        "producer-consumer": "void produce(T item)",
        "dining-philosophers": "void dine()",
    }.get(slug, f"void execute({primary} request)")

    clarify_extra = {
        "chess": [("Draw conditions?", "Stalemate, threefold repetition — extension"), ("AI opponent?", "Two human players MVP")],
        "hotel-booking": [("Overbooking allowed?", "No — reject when full"), ("Cancellation policy?", "Free cancel 24h before")],
        "vending-machine": [("Payment types?", "Coins + bills MVP"), ("Change return?", "Greedy coin return")],
        "rate-limiter": [("Algorithm?", "Token bucket or sliding window — Strategy"), ("Per-client key?", "UserId or IP string")],
        "in-memory-file-system": [("Symlinks?", "Extension"), ("Max path depth?", "Unlimited MVP")],
        "ride-sharing-uber": [("Surge pricing?", "FareCalculator extension"), ("Pool rides?", "Extension")],
    }.get(slug, [
        (f"Key constraint for {title}?", f"See problem — {problem[:60]}..."),
        ("Scale?", "Single JVM; HLD for distributed"),
    ])

    clarify = [
        (f"What is MVP scope for {title}?", "Core entities + 2 primary flows end-to-end"),
        ("Persistence?", "In-memory; Repository interface if asked"),
        ("Concurrency?", "Thread-safe shared state if multi-user access assumed"),
        (f"Variation point?", f"Inject {iface} — swap behavior without editing {service}"),
        ("Invalid input?", "Domain exceptions — fail fast"),
        ("Testing?", f"Mock {iface} in {service} unit tests"),
    ] + list(clarify_extra)

    functional = {
        "chess": ["Validate and execute legal moves", "Detect check, checkmate, stalemate", "Alternate turns between players", "Reject illegal moves with reason"],
        "hotel-booking": ["Search rooms by date range and type", "Create/cancel booking", "Check-in transitions room to occupied", "Prevent double-booking same room"],
        "vending-machine": ["Select product, accept coins, dispense item", "Return change using coin inventory", "Reject when out of stock or insufficient payment", "State machine for idle/has-money/dispensing"],
        "rate-limiter": ["allowRequest(key) returns true if under limit", "Reject when window/quota exhausted", "Configurable limits per client key", "Support token bucket or sliding window via Strategy"],
    }.get(slug, [
        f"{service} orchestrates primary {title} workflow",
        "Validate inputs before mutating domain state",
        f"Delegate variation to {iface}",
        "Return typed results; throw domain exceptions on rule violations",
    ])

    happy_custom, fail_custom = {
        "chess": (
            _seq("participant P as Player", "participant G as ChessGame", "participant V as MoveValidator",
                 "P->>G: makeMove(e2e4)", "G->>V: isValid(move)", "V-->>G: true", "G->>G: applyMove()", "G-->>P: success"),
            _seq("participant P as Player", "participant G as ChessGame", "participant V as MoveValidator",
                 "P->>G: makeMove(invalid)", "G->>V: isValid(move)", "V-->>G: false", "G-->>P: IllegalMoveException"),
        ),
        "strategy-payment": (
            _seq("participant C as Client", "participant P as PaymentProcessor", "participant S as StripeProcessor",
                 "C->>P: process(request)", "P->>S: charge(amount)", "S-->>P: success", "P-->>C: PaymentResult"),
            _seq("participant C as Client", "participant P as PaymentProcessor",
                 "C->>P: process(invalid)", "P-->>C: PaymentDeclinedException"),
        ),
    }.get(slug, (None, None))

    happy = happy_custom or _seq(
        "participant U as User", f"participant S as {service}", f"participant D as {primary}",
        f"U->>S: {method0.split('(')[0].split()[-1]}()", f"S->>D: validate", "D-->>S: ok", "S-->>U: result",
    )
    fail = fail_custom or _seq(
        "participant U as User", f"participant S as {service}",
        f"U->>S: {method0.split('(')[0].split()[-1]}(invalid)", "S-->>U: DomainException",
    )

    script = {
        "chess": [
            "ChessGame owns Board, two Players, and current turn.",
            "Piece subclasses encode movement rules — Polymorphism over piece type.",
            "MoveValidator checks legality including pin, check, path obstruction.",
            "makeMove validates, applies, toggles turn, updates GameState.",
            "CheckDetector scans opponent king threat after each move.",
            "Checkmate when king in check and no legal moves.",
            "Could use Command pattern for move history and undo.",
            "HLD not needed — pure in-memory game state.",
        ],
        "hotel-booking": [
            "Hotel has Rooms; AvailabilityCalendar indexes free rooms by date.",
            "Guest searches date range + RoomType; system returns available rooms.",
            "Booking locks room for date range — reject overlap.",
            "PricingStrategy computes total from nightly rates.",
            "Check-in updates Booking status; check-out frees room.",
            "Cancel within policy window — no fee; else CancellationFeeStrategy.",
            "Synchronize booking creation per room to prevent double book.",
            "HLD: distributed inventory with optimistic locking; LLD model same.",
        ],
    }.get(slug, [
        f"I'll clarify scope for {title} — in-memory, MVP flows.",
        f"Entities: {nouns}. Service facade: {service}.",
        f"Variation via {iface} — Strategy/Open-Closed.",
        f"Core method: {method0}.",
        "Validate first, delegate to domain, return typed result.",
        "Extensibility: new interface impl without editing service loop.",
        "Tradeoff: enum for simple state; State pattern for complex transitions.",
        "Sketch Java with constructor injection for testability.",
        "HLD pivot if distributed scale required — object model unchanged.",
    ])

    return merge_details(slug, {
        "clarify": clarify[:8],
        "functional": functional if isinstance(functional, list) else list(functional),
        "methods": [method0] if slug not in OVERRIDES else OVERRIDES[slug].get("methods", [method0]),
        "verbs": OVERRIDES.get(slug, {}).get("verbs", f"`{method0.split('(')[0].split()[-1]}()`"),
        "happy_seq": happy,
        "fail_seq": fail,
        "script": script if isinstance(script, list) else list(script),
        "nouns": nouns,
    })
