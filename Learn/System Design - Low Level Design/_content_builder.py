#!/usr/bin/env python3
"""Build Parking Lot-level rich content for every LLD question slug."""
from __future__ import annotations

import re
from typing import Any

# Correct design patterns per slug (not interface names)
PATTERN_MAP: dict[str, list[tuple[str, str]]] = {
    "library-management": [("Strategy", "Fine calculation policies"), ("Observer", "Notify when reserved book available")],
    "chess": [("Strategy", "Per-piece move rules"), ("Template Method", "Turn loop skeleton")],
    "tic-tac-toe": [("Strategy", "Win detection algorithm")],
    "vending-machine": [("State", "Idle / has-money / dispensing"), ("Strategy", "Change-making algorithm")],
    "lru-cache": [("Doubly Linked List + HashMap", "O(1) get/put eviction")],
    "rate-limiter": [("Strategy", "Token bucket vs sliding window")],
    "logger": [("Chain of Responsibility", "Log level filtering"), ("Observer", "Multiple appenders")],
    "in-memory-file-system": [("Composite", "Directory contains files and subdirs")],
    "splitwise": [("Strategy", "Equal / percent / exact split")],
    "movie-ticket-booking": [("State", "Seat available / held / booked"), ("Strategy", "Pricing")],
    "ride-sharing-uber": [("Strategy", "Driver matching"), ("State", "Trip lifecycle")],
    "messenger-1to1": [("Repository", "Message persistence abstraction")],
    "notification-system": [("Strategy", "Channel selection"), ("Factory", "Channel sender creation")],
    "pubsub-event-bus": [("Observer", "Topic subscribers"), ("Mediator", "EventBus decoupling")],
    "news-feed-object-model": [("Strategy", "Feed ranking"), ("Observer", "New post notifications")],
    "comment-thread": [("Composite", "Nested comments tree")],
    "elevator": [("Strategy", "SCAN / nearest-car dispatch"), ("State", "Elevator direction and door")],
    "parking-lot": [("Strategy", "Spot allocation"), ("Factory", "Vehicle creation")],
    "rag-orchestrator": [("Chain of Responsibility", "Retrieve → rerank → generate"), ("Strategy", "Swappable retriever/generator")],
    "agent-tool-registry": [("Registry", "Tool lookup by name"), ("Strategy", "Tool execution")],
    "guardrail-safety-chain": [("Chain of Responsibility", "PII → toxicity → injection filters")],
    "multi-agent-coordinator": [("Mediator", "Supervisor routes to workers"), ("Strategy", "Task routing")],
    "dining-philosophers": [("Concurrency", "Ordered fork acquisition avoids deadlock")],
    "producer-consumer": [("Producer-Consumer", "BlockingQueue between threads")],
    "command-undo-redo": [("Command", "Encapsulate actions with undo"), ("Memento", "Optional state snapshots")],
    "observer-stock-ticker": [("Observer", "Price change notifies investors")],
    "state-vending-machine": [("State", "Vending machine lifecycle states")],
    "decorator-coffee": [("Decorator", "Stack add-ons on beverage")],
    "composite-org-chart": [("Composite", "Manager contains employees")],
    "strategy-payment": [("Strategy", "Swappable payment gateways")],
    "singleton-thread-safe": [("Singleton", "Single JVM instance")],
    "flyweight-forest": [("Flyweight", "Shared tree mesh per type")],
    "visitor-shopping-cart-tax": [("Visitor", "Tax calc per item type")],
}

# Problem-specific clarifying question extras (appended to base)
CLARIFY_EXTRA: dict[str, list[tuple[str, str]]] = {
    "library-management": [
        ("Loan period?", "14 days default"),
        ("Multiple copies per title?", "Yes — BookItem per physical copy"),
        ("Fine on overdue?", "Per day via FineStrategy"),
        ("Reservation when checked out?", "FIFO queue per ISBN"),
    ],
    "hotel-booking": [
        ("Overbooking?", "No — reject when room unavailable"),
        ("Cancellation window?", "Free cancel 24h before check-in"),
        ("Room types?", "Single, double, suite enum"),
        ("Pricing?", "Nightly rate × nights via PricingStrategy"),
    ],
    "chess": [
        ("Two players?", "Human vs human MVP"),
        ("Castling / en passant?", "Include in move rules"),
        ("Draw rules?", "Stalemate MVP; repetition extension"),
        ("Undo?", "Command pattern extension"),
    ],
    "lru-cache": [
        ("Capacity fixed?", "Set at construction"),
        ("Thread-safe?", "Single-threaded; see concurrent-lru-cache Q"),
        ("Null values?", "Reject or allow — document choice"),
        ("Eviction policy?", "Least recently used only"),
    ],
    "rate-limiter": [
        ("Per client key?", "userId or IP string"),
        ("Algorithm?", "Token bucket default; sliding window via Strategy"),
        ("Burst allowed?", "Yes — bucket capacity > steady rate"),
        ("Distributed?", "HLD — in-process only for LLD"),
    ],
    "splitwise": [
        ("Split types?", "Equal, exact amounts, percentage"),
        ("Simplify debts?", "Optional balance simplification graph"),
        ("Multi-currency?", "Extension"),
        ("Groups?", "Group contains multiple users"),
    ],
    "messenger-1to1": [
        ("Group chat?", "Extension — 1:1 MVP"),
        ("Message order?", "Per-conversation FIFO"),
        ("Read receipts?", "Per-message DeliveryStatus enum"),
        ("Offline delivery?", "Queue extension — in-memory MVP"),
    ],
    "in-memory-file-system": [
        ("Operations?", "mkdir, ls, cd, touch, cat, find, du"),
        ("Symlinks?", "Extension"),
        ("Permissions?", "Extension"),
        ("Max file size?", "Unbounded in-memory"),
    ],
    "ride-sharing-uber": [
        ("Matching?", "Nearest available driver via MatchingStrategy"),
        ("Surge?", "FareCalculator multiplier extension"),
        ("Trip states?", "REQUESTED → ACCEPTED → IN_PROGRESS → COMPLETED"),
        ("Pool rides?", "Extension"),
    ],
    "dining-philosophers": [
        ("Deadlock prevention?", "Ordered fork pickup or waiter"),
        ("Philosopher count?", "Configurable N"),
        ("Eat time?", "Random or fixed think/eat cycles"),
        ("Waiter arbitrator?", "Alternative to ordered forks"),
    ],
    "thread-pool-executor": [
        ("Pool size?", "Fixed N worker threads"),
        ("Queue type?", "Bounded BlockingQueue"),
        ("Rejection policy?", "Abort, caller-runs, or block"),
        ("Shutdown?", "Graceful drain then interrupt"),
    ],
    "rag-orchestrator": [
        ("Vector DB?", "HLD — stub Retriever interface"),
        ("Reranking?", "Optional Reranker stage"),
        ("Token limit?", "ContextAssembler trims chunks"),
        ("Streaming?", "Separate StreamAggregator Q"),
    ],
}

# Service method signatures per slug
METHODS_MAP: dict[str, list[str]] = {
    "library-management": [
        "Loan checkout(Member member, String barcode)",
        "void returnItem(String barcode)",
        "void reserve(Member member, String isbn)",
        "BigDecimal calculateFine(Loan loan)",
    ],
    "hotel-booking": [
        "Booking createBooking(Guest guest, Room room, LocalDateRange dates)",
        "void cancelBooking(String bookingId)",
        "List<Room> searchAvailable(RoomType type, LocalDateRange dates)",
        "void checkIn(Booking booking)",
    ],
    "chess": [
        "boolean makeMove(Move move)",
        "boolean isInCheck(Player player)",
        "GameState getState()",
        "List<Move> getLegalMoves()",
    ],
    "lru-cache": [
        "V get(K key)",
        "void put(K key, V value)",
        "int size()",
        "void clear()",
    ],
    "rate-limiter": [
        "boolean allowRequest(String clientKey)",
        "void reset(String clientKey)",
        "long remainingTokens(String clientKey)",
    ],
    "logger": [
        "void log(LogLevel level, String message)",
        "void addAppender(LogAppender appender)",
        "void setLevel(LogLevel minLevel)",
    ],
    "vending-machine": [
        "void insertCoin(Coin coin)",
        "Product selectItem(String code)",
        "void dispense()",
        "BigDecimal getChange()",
    ],
    "splitwise": [
        "void addExpense(Expense expense)",
        "Map<User, BigDecimal> getBalances(Group group)",
        "void settle(User from, User to, BigDecimal amount)",
    ],
    "movie-ticket-booking": [
        "SeatLock holdSeats(Show show, List<Seat> seats, Duration ttl)",
        "Booking confirm(SeatLock lock, Payment payment)",
        "void releaseHold(SeatLock lock)",
    ],
    "in-memory-file-system": [
        "void mkdir(String path)",
        "void cd(String path)",
        "List<String> ls(String path)",
        "String cat(String path)",
        "long du(String path)",
    ],
    "messenger-1to1": [
        "Message sendMessage(String conversationId, String text)",
        "Conversation getOrCreateConversation(User a, User b)",
        "void markRead(String messageId)",
        "List<Message> getHistory(String conversationId)",
    ],
    "pubsub-event-bus": [
        "void subscribe(String topic, Subscriber subscriber)",
        "void unsubscribe(String topic, Subscriber subscriber)",
        "void publish(String topic, Event event)",
    ],
    "strategy-payment": [
        "PaymentResult process(PaymentRequest request)",
        "void setProcessor(PaymentProcessor processor)",
    ],
    "command-undo-redo": [
        "void execute(Command command)",
        "void undo()",
        "void redo()",
    ],
    "bounded-blocking-queue": [
        "void put(E item)",
        "E take()",
        "int size()",
    ],
    "producer-consumer": [
        "void produce(T item)",
        "T consume()",
    ],
    "rag-orchestrator": [
        "String answer(Query query)",
        "List<Chunk> retrieve(Query query)",
    ],
    "agent-tool-registry": [
        "void register(String name, Tool tool)",
        "ToolResult execute(String toolName, Map<String, Object> args)",
        "List<ToolSchema> listTools()",
    ],
}

# Entity methods for Mermaid class diagrams
ENTITY_METHODS: dict[str, list[str]] = {
    "ParkingLot": ["-floors: List", "+addFloor(Floor) void", "+allSpots() Stream"],
    "ParkingSpot": ["-type: SpotType", "+isAvailable() boolean", "+assign(Vehicle) void", "+vacate() void"],
    "Vehicle": ["-type: VehicleType", "-licensePlate: String"],
    "Ticket": ["-id: String", "-entryTime: Instant", "+getSpot() ParkingSpot"],
    "ParkingStrategy": ["<<interface>>", "+findSpot(Vehicle, List) Optional"],
    "Elevator": ["-currentFloor: int", "-direction: Direction", "+addRequest(Request) void", "+step() void"],
    "ElevatorController": ["+requestElevator(int, Direction) void", "+stepAll() void"],
    "SchedulingStrategy": ["<<interface>>", "+select(List, Request) Elevator"],
    "Board": ["-cells: Cell[][]", "+getPiece(int,int) Piece", "+movePiece(Move) void"],
    "ChessPiece": ["<<abstract>>", "+isValidMove(Board, Move) boolean"],
    "ChessGame": ["+makeMove(Move) boolean", "+getState() GameState"],
    "MoveValidator": ["<<interface>>", "+validate(Board, Move) boolean"],
    "LRUCache": ["-capacity: int", "+get(K) V", "+put(K,V) void"],
    "Node": ["-key: K", "-value: V", "-prev, next: Node"],
    "RateLimiter": ["+allowRequest(String) boolean"],
    "TokenBucket": ["-tokens: double", "+tryConsume() boolean"],
    "Logger": ["-level: LogLevel", "+log(Level, String) void"],
    "LogAppender": ["<<interface>>", "+append(LogMessage) void"],
    "VendingMachine": ["+insertCoin(Coin) void", "+selectProduct(String) void", "+dispense() void"],
    "VendingState": ["<<interface>>", "+insertCoin()", "+selectProduct()"],
    "FileSystem": ["-root: Directory", "+mkdir(String) void", "+cd(String) void", "+ls() List"],
    "Directory": ["-children: Map", "+addChild(INode) void"],
    "File": ["-content: byte[]", "+read() byte[]"],
    "RAGOrchestrator": ["+answer(Query) String"],
    "Retriever": ["<<interface>>", "+retrieve(Query) List"],
    "Generator": ["<<interface>>", "+generate(Query, String) String"],
    "PaymentProcessor": ["<<interface>>", "+pay(double) void"],
    "Command": ["<<interface>>", "+execute() void", "+undo() void"],
    "Editor": ["+insert(String) void", "+delete(int) void"],
    "EventBus": ["+publish(String, Event) void", "+subscribe(String, Subscriber) void"],
    "BoundedBlockingQueue": ["+put(E) void", "+take() E"],
    "Account": ["-balance: BigDecimal", "+debit(BigDecimal) void", "+credit(BigDecimal) void"],
    "ToolRegistry": ["+register(String, Tool) void", "+execute(String, Map) ToolResult"],
    "Guardrail": ["<<interface>>", "+filter(String) SafetyResult"],
    "ShoppingCart": ["+addItem(SKU, int) void", "+removeItem(SKU) void", "+total() Money"],
    "Order": ["-items: List", "-status: OrderStatus", "+addItem(Item) void"],
    "User": ["-id: String", "-name: String"],
    "Message": ["-text: String", "-status: DeliveryStatus", "+markRead() void"],
    "Conversation": ["-participants: Pair<User>", "-messages: List"],
    "Library": ["-catalog: Map", "+addBook(Book) void", "+findByIsbn(String) Book"],
    "Book": ["-isbn: String", "-title: String", "-author: String"],
    "BookItem": ["-barcode: String", "+checkout(Member) void", "+returnItem() void"],
    "Member": ["-id: String", "+getActiveLoans() List"],
    "LendingService": ["+checkout(Member, String) Loan", "+returnItem(String) void"],
    "ReservationQueue": ["+enqueue(Member, String) void", "+pollNext(String) Member"],
    "FineStrategy": ["<<interface>>", "+calculate(Loan) BigDecimal"],
    "Bookmark": ["-url: String", "-title: String", "+validateUrl() boolean"],
    "Folder": ["-name: String", "-children: List", "+addChild(Folder) void"],
    "Tag": ["-label: String"],
    "BookmarkStore": ["<<interface>>", "+save(Bookmark) void"],
    "SearchIndex": ["<<interface>>", "+search(String) List"],
    "Reranker": ["<<interface>>", "+rerank(Query, List) List"],
    "ContextAssembler": ["+assemble(List) String"],
    "Query": ["-text: String", "-maxTokens: int"],
    "Wishlist": ["+addItem(String productId) void", "+removeItem(String productId) void"],
    "Auction": ["+placeBid(Bid) void", "+getWinner() Bidder"],
    "Trip": ["-status: TripStatus", "+complete() void"],
    "Driver": ["-location: Location", "+setAvailable(boolean) void"],
    "Playlist": ["+addSong(Song) void", "+shuffle() void"],
    "Post": ["-content: String", "+addReaction(Reaction) void"],
    "Comment": ["-text: String", "+reply(String) Comment"],
    "Coupon": ["-code: String", "+isValid(Cart) boolean"],
    "Account": ["-balance: BigDecimal", "+debit(BigDecimal) void", "+credit(BigDecimal) void"],
    "Philosopher": ["+think() void", "+eat() void"],
    "Fork": ["+pickUp() void", "+putDown() void"],
    "CommandHistory": ["+push(Command) void", "+pop() Command"],
    "InsertCommand": ["+execute() void", "+undo() void"],
    "PaymentContext": ["+checkout(double) void"],
}


def _entity_mermaid_lines(entities: list[tuple[str, str]]) -> list[str]:
    lines = []
    for name, role in entities:
        methods = ENTITY_METHODS.get(name)
        if methods:
            lines.append(f"    class {name} {{")
            for m in methods:
                if m.startswith("<<"):
                    lines.append(f"        {m}")
                elif m.startswith(("+", "-", "#")):
                    lines.append(f"        {m}")
                else:
                    lines.append(f"        +{m}")
            lines.append("    }")
        else:
            # Derive 1-2 methods from role
            lines.append(f"    class {name} {{")
            if "interface" in role.lower() or "strategy" in role.lower() or "policy" in role.lower():
                lines.append("        <<interface>>")
                lines.append(f"        +apply() void")
            elif "enum" in role.lower() or "status" in role.lower() or "state" in role.lower():
                lines.append("        <<enumeration>>")
            elif "queue" in role.lower():
                lines.append("        +enqueue() void")
                lines.append("        +dequeue() Object")
            elif "factory" in role.lower():
                lines.append(f"        +create() {name.replace('Factory', '')}")
            else:
                lines.append(f"        +execute() void")
                if "root" in role.lower() or "aggregate" in role.lower():
                    lines.append("        +getId() String")
            lines.append("    }")
    return lines


def build_mermaid_class(service: str, methods: list[str], entities: list[tuple[str, str]], iface: str) -> str:
    lines = ["classDiagram"]
    seen: set[str] = set()
    entity_names = {e[0] for e in entities}

    def add_class(name: str, body: list[str]) -> None:
        if name in seen:
            return
        seen.add(name)
        lines.append(f"    class {name} {{")
        for bl in body:
            lines.append(f"        {bl}")
        lines.append("    }")

    svc_body = []
    for m in methods[:5]:
        ms = m.strip()
        if ms.startswith("public "):
            ms = ms[7:].strip()
        if not ms.startswith(("+", "-", "#", "~")):
            ms = "+" + ms
        svc_body.append(ms)
    add_class(service, svc_body)

    for ent_line_block in _entity_mermaid_lines(entities):
        # parse back from generated lines - use direct entity iteration instead
        pass

    for name, role in entities:
        if name in seen:
            continue
        methods_ent = ENTITY_METHODS.get(name)
        body: list[str] = []
        if methods_ent:
            for m in methods_ent:
                body.append(m if m.startswith("<<") else (m if m.startswith(("+", "-", "#")) else f"+{m}"))
        else:
            if "interface" in role.lower() or name.endswith("Strategy") or name.endswith("Policy"):
                body = ["<<interface>>", "+apply() void"]
            elif "enum" in role.lower() or "status" in role.lower():
                body = ["<<enumeration>>"]
            elif "queue" in role.lower():
                body = ["+enqueue() void", "+dequeue() Object"]
            else:
                body = [f"+execute() void"]
        add_class(name, body)

    if iface and iface not in entity_names and iface not in seen:
        add_class(iface, ["<<interface>>", "+apply() void"])

    if entities:
        root = entities[0][0]
        if root != service:
            lines.append(f"    {service} --> {root}")
    if iface and iface not in entity_names:
        lines.append(f"    {service} ..> {iface}")
    return "\n".join(lines)


def _seq(*lines: str) -> str:
    return "\n".join(lines)


def build_happy_fail(slug: str, service: str, entities: list[tuple[str, str]], methods: list[str]) -> tuple[str, str]:
    primary_method = methods[0].split("(")[0].split()[-1] if methods else "execute"
    e0 = entities[0][0] if entities else "Domain"
    e1 = entities[1][0] if len(entities) > 1 else "Domain"

    custom = {
        "bookmark-manager": (
            _seq("participant U as User", "participant S as BookmarkService", "participant F as Folder",
                 "U->>S: addBookmark(url, title, folderId)", "S->>S: validateUrl(url)", "S->>F: place(bookmark)",
                 "S-->>U: Bookmark"),
            _seq("U->>S: addBookmark(invalidUrl)", "S-->>U: InvalidUrlException"),
        ),
        "library-management": (
            _seq("participant M as Member", "participant L as LendingService", "participant BI as BookItem",
                 "M->>L: checkout(barcode)", "L->>BI: isAvailable()", "BI-->>L: true",
                 "L->>BI: markBorrowed(member)", "L-->>M: Loan"),
            _seq("M->>L: checkout(barcode)", "L->>BI: isAvailable()", "BI-->>L: false", "L-->>M: ItemUnavailableException"),
        ),
        "hotel-booking": (
            _seq("participant G as Guest", f"participant B as {service}", "participant R as Room",
                 "G->>B: createBooking(room, dates)", "B->>R: isAvailable(dates)", "R-->>B: true",
                 "B->>B: createRecord()", "B-->>G: Booking"),
            _seq("G->>B: createBooking(room, dates)", "B->>R: isAvailable(dates)", "R-->>B: false", "B-->>G: RoomUnavailableException"),
        ),
        "lru-cache": (
            _seq("participant C as Client", "participant L as LRUCache",
                 "C->>L: put(k1,v1)", "C->>L: put(k2,v2)", "C->>L: get(k1)", "L-->>C: v1"),
            _seq("C->>L: put(k4,v4) at capacity", "L->>L: evict LRU entry", "C->>L: get(k1)", "L-->>C: null"),
        ),
        "vending-machine": (
            _seq("participant U as User", "participant V as VendingMachine", "participant S as VendingState",
                 "U->>V: insertCoin(1)", "U->>V: selectItem(A1)", "V->>S: dispense()", "V-->>U: Product"),
            _seq("U->>V: selectItem(A1)", "V->>V: checkFunds()", "V-->>U: InsufficientFundsException"),
        ),
        "splitwise": (
            _seq("participant U as User", f"participant S as {service}", "participant E as Expense",
                 "U->>S: addExpense(expense)", "S->>E: validateSplit()", "S->>S: updateBalances()", "S-->>U: ok"),
            _seq("U->>S: addExpense(invalid)", "S-->>U: InvalidSplitException"),
        ),
        "in-memory-file-system": (
            _seq("participant U as User", "participant FS as FileSystem", "participant D as Directory",
                 "U->>FS: mkdir(/a/b)", "FS->>D: createPath()", "U->>FS: cd(/a/b)", "FS-->>U: ok"),
            _seq("U->>FS: cat(/missing)", "FS-->>U: PathNotFoundException"),
        ),
        "messenger-1to1": (
            _seq("participant A as UserA", f"participant S as {service}", "participant C as Conversation",
                 "A->>S: sendMessage(convId, text)", "S->>C: append(message)", "S-->>A: Message"),
            _seq("A->>S: sendMessage(invalidConv)", "S-->>U: ConversationNotFoundException"),
        ),
        "pubsub-event-bus": (
            _seq("participant P as Publisher", "participant B as EventBus", "participant Sub as Subscriber",
                 "P->>B: publish(order.created, event)", "B->>Sub: onEvent(event)", "Sub-->>B: ack"),
            _seq("P->>B: publish(unknown, event)", "B-->>P: no subscribers — optional log"),
        ),
        "rag-orchestrator": (
            _seq("participant U as User", "participant R as RAGOrchestrator", "participant Ret as Retriever", "participant G as Generator",
                 "U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: chunks",
                 "R->>G: generate(query, context)", "G-->>R: text", "R-->>U: answer"),
            _seq("U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: empty", "R-->>U: NoContextException"),
        ),
        "dining-philosophers": (
            _seq("participant P as Philosopher", "participant F as Fork", "participant T as Table",
                 "P->>T: pickLeftFork()", "P->>T: pickRightFork()", "P->>T: eat()", "P->>T: releaseForks()"),
            _seq("participant P1 as Phil1", "participant P2 as Phil2", "P1->>F: pickLeft", "P2->>F: pickRight", "Note over P1,P2: deadlock without ordering"),
        ),
        "producer-consumer": (
            _seq("participant Prod as Producer", "participant Q as BlockingQueue", "participant Cons as Consumer",
                 "Prod->>Q: put(item)", "Q->>Cons: take()", "Cons-->>Cons: process(item)"),
            _seq("Prod->>Q: put(item)", "Note over Q: queue full — producer blocks", "Cons->>Q: take()", "Q-->>Prod: notify"),
        ),
        "bank-transfer-deadlock": (
            _seq("participant T as TransferService", "participant A1 as Account1", "participant A2 as Account2",
                 "T->>A1: lock(id order)", "T->>A2: lock(id order)", "T->>A1: debit()", "T->>A2: credit()"),
            _seq("Note over T: Without ordering — Thread1 locks A1, Thread2 locks A2 → deadlock"),
        ),
    }
    if slug in custom:
        return custom[slug]

    return (
        _seq("participant U as User", f"participant S as {service}", f"participant D as {e0}",
             f"U->>S: {primary_method}()", f"S->>D: validate / process", "D-->>S: ok", "S-->>U: result"),
        _seq("participant U as User", f"participant S as {service}",
             f"U->>S: {primary_method}(invalid)", f"S-->>U: DomainException"),
    )


def build_script(slug: str, title: str, service: str, entities: list[tuple[str, str]], iface: str, track: str, problem: str) -> list[str]:
    names = ", ".join(f"`{e[0]}`" for e in entities[:6])
    custom = {
        "library-management": [
            "Library owns Book catalog metadata and physical BookItem copies with barcodes.",
            "Member checks out a BookItem — one copy, one borrower at a time.",
            "checkout validates membership, availability, and per-member loan limit.",
            "return computes overdue fine via injected FineStrategy.",
            "ReservationQueue is FIFO per ISBN when all copies are out.",
            "CatalogService separated from LendingService — Single Responsibility.",
            "Synchronize checkout/return on BookItem to prevent double borrow.",
            "HLD: search index + DB; LLD entity graph maps cleanly.",
        ],
        "hotel-booking": [
            "Hotel contains Rooms; AvailabilityCalendar indexes free rooms by date range.",
            "Guest searches by RoomType and dates — returns only non-overlapping rooms.",
            "createBooking atomically marks room reserved for date range.",
            "PricingStrategy computes total from nightly rates and seasonal rules.",
            "checkIn transitions Booking to CHECKED_IN; checkOut frees room.",
            "cancel within policy window — no fee; else CancellationFeeStrategy.",
            "Synchronize per-room booking to prevent double-book race.",
            "HLD: distributed inventory with optimistic locking; same object model.",
        ],
        "lru-cache": [
            "LRUCache combines HashMap for O(1) lookup and doubly-linked list for recency.",
            "get(key): if present, move node to head; return value.",
            "put(key, value): update or insert at head; evict tail if over capacity.",
            "Node stores key, value, prev, next pointers.",
            "All operations O(1) — classic Amazon/Google interview problem.",
            "Thread-safe variant: synchronize methods or segment locks — separate concurrency Q.",
            "Extension: TTL per entry via wrapper or decorator.",
            "HLD: distributed cache is different problem — Redis cluster, consistent hashing.",
        ],
        "rate-limiter": [
            "RateLimiter facade delegates to RateLimitAlgorithm Strategy.",
            "Token bucket: refill tokens per second up to capacity; each request consumes one.",
            "Sliding window: count requests in rolling time buckets.",
            "allowRequest(clientKey) returns false when quota exhausted.",
            "Per-client state in Map — ConcurrentHashMap for thread safety.",
            "Stripe/Google classic — LLD is single-node; HLD uses Redis + Lua.",
            "Extension: tiered limits per API key plan.",
            "Mention burst vs steady rate tradeoff explicitly.",
        ],
        "vending-machine": [
            "VendingMachine context object holds current VendingState.",
            "States: Idle, HasMoney, Dispensing, SoldOut — State pattern.",
            "insertCoin transitions Idle → HasMoney; accumulates balance.",
            "selectProduct validates funds and inventory, moves to Dispensing.",
            "dispense decrements stock, returns change via ChangeStrategy.",
            "SoldOut when inventory zero — reject selection.",
            "Each state class implements same interface — no giant switch.",
            "Extension: card payment as new state or parallel PaymentProcessor.",
        ],
        "in-memory-file-system": [
            "FileSystem root is a Directory node at /.",
            "Composite pattern: Directory and File implement INode interface.",
            "mkdir creates nested directories; cd changes current working directory.",
            "PathResolver normalizes .. and . segments.",
            "ls lists immediate children; find walks tree BFS/DFS.",
            "du sums file sizes recursively on directories.",
            "cat reads file bytes; touch creates empty file.",
            "HLD: distributed FS is metadata + blob store — different design.",
        ],
        "messenger-1to1": [
            "User has many Conversations; Conversation links exactly two users for MVP.",
            "getOrCreateConversation returns existing thread or creates new.",
            "sendMessage appends Message with SENT status; updates DeliveryStatus on read.",
            "MessageRepository interface — in-memory list or map for MVP.",
            "Inbox shows conversations sorted by last message time.",
            "Extension: group chat adds ConversationType and participant list.",
            "HLD: WebSocket + Cassandra by conversation_id — see HLD WhatsApp Q.",
            "LLD focuses on object relationships and status enums.",
        ],
        "splitwise": [
            "Group contains Users; Expense has payer and Split list per participant.",
            "SplitStrategy: equal split, exact amounts, or percentage.",
            "addExpense validates splits sum to total amount.",
            "BalanceSheet tracks net owed between each pair — simplify optionally.",
            "settle records payment reducing balance between two users.",
            "Extension: multi-currency with exchange rate service.",
            "Immutable Expense after creation — audit trail.",
            "HLD: event sourcing for expenses; LLD model is clean domain.",
        ],
        "ride-sharing-uber": [
            "Rider requests trip with pickup and dropoff Location.",
            "MatchingStrategy selects nearest available Driver.",
            "Trip state machine: REQUESTED → ACCEPTED → IN_PROGRESS → COMPLETED.",
            "FareCalculator uses distance, time, and SurgePricingStrategy.",
            "Driver accepts trip — exclusive lock on driver until complete.",
            "Extension: pool rides add waypoints.",
            "HLD: real-time location stream, dispatch service — see HLD Uber Q.",
            "LLD: Trip aggregate owns lifecycle; Driver is supply entity.",
        ],
        "dining-philosophers": [
            "N philosophers, N forks — each needs two forks to eat.",
            "Naive pick-left-then-right causes circular deadlock.",
            "Fix 1: total ordering on fork IDs — always pick lower ID first.",
            "Fix 2: waiter arbitrator grants permission when both forks free.",
            "Philosopher thread loops: think, acquire forks, eat, release.",
            "synchronized on forks or ReentrantLock per fork.",
            "Classic concurrency interview — explain deadlock four conditions.",
            "Extension: asymmetric solution — odd/even philosopher pick order.",
        ],
        "rag-orchestrator": [
            "RAGOrchestrator wires Retriever, optional Reranker, ContextAssembler, Generator.",
            "answer(query): retrieve chunks, rerank, assemble context within token budget, generate.",
            "Each stage is an interface — swap OpenAI vs local embeddings.",
            "Empty retrieval → NoContextException or fallback response.",
            "ContextAssembler joins chunks with separators and metadata.",
            "GuardrailChain extension on input/output strings.",
            "HLD: vector DB, embedding service, GPU inference fleet.",
            "LLD tests each stage with mocks — high testability.",
        ],
    }
    if slug in custom:
        return custom[slug]

    paras = [
        f"I'll design {title} starting with scope: in-memory, single JVM, core flows in MVP.",
        f"Core entities: {names}. I'll separate domain structure from {service} orchestration.",
        f"Variation point: `{iface}` interface — swap algorithms without editing the service loop.",
        f"Primary API on `{service}` — validate inputs, enforce business rules, return typed results.",
        f"Problem focus: {problem[:120]}{'...' if len(problem) > 120 else ''}",
        "Open-Closed: new behavior = new interface implementation, not if/else sprawl.",
        "Tradeoff: enum for simple lifecycles; State pattern when transitions have side effects.",
        "Constructor injection for testability — mock interfaces in unit tests.",
    ]
    if track == "concurrency":
        paras.append("Identify shared mutable state; choose lock granularity; prevent deadlock with consistent ordering.")
    elif track == "genai":
        paras.append("Pipeline object model here; vector DB, model serving, and queues are HLD concerns.")
    elif track == "patterns":
        paras.append(f"This question demonstrates {iface or 'the target'} pattern — name it explicitly and justify.")
    else:
        paras.append("If interviewer asks millions of users — pivot to HLD; object model remains valid.")
    return paras


def build_concurrency(slug: str, track: str, entities: list[tuple[str, str]]) -> list[str]:
    if track == "concurrency":
        base = {
            "dining-philosophers": [
                "Deadlock without ordering — demonstrate then fix with fork ID ordering",
                "synchronized(fork) or ReentrantLock per fork",
                "Waiter pattern: centralized arbitrator avoids hold-and-wait",
                "Starvation possible — fair lock or waiter queue extension",
            ],
            "producer-consumer": [
                "BlockingQueue: wait/notify when full or empty",
                "Multiple producers/consumers — queue is shared synchronized structure",
                "Poison pill pattern to shut down consumers gracefully",
                "Spurious wakeup handled by while loop on condition",
            ],
            "bank-transfer-deadlock": [
                "Always lock accounts in ascending ID order — global total ordering",
                "Never hold lock on A then try B while another thread holds B and tries A",
                "Transfer is atomic: debit source, credit dest in same synchronized block",
                "Insufficient funds → InsufficientFundsException before any mutation",
            ],
            "concurrent-lru-cache": [
                "Synchronize get/put or use read-write lock if read-heavy",
                "Eviction during get must be atomic with list reorder",
                "Alternative: ConcurrentHashMap + synchronized list head/tail",
                "Document lock granularity tradeoff: whole cache vs per-segment",
            ],
            "thread-safe-singleton": [
                "Double-checked locking requires volatile instance field",
                "Enum singleton preferred — JVM guarantees single instance",
                "Holder idiom: static nested class — lazy and thread-safe",
                "Avoid synchronized getInstance() on every call after init",
            ],
        }
        return base.get(slug, [
            "Identify shared mutable state across threads",
            "Use synchronized, Lock, or concurrent collections appropriately",
            "Avoid deadlock — consistent lock acquisition order",
            "Document happens-before relationships for interview clarity",
        ])

    per_slug = {
        "parking-lot": [
            "synchronize on ParkingSpot during assign/vacate — check-then-act",
            "ConcurrentHashMap for active tickets by ID",
            "Lot full → LotFullException before partial assign",
            "Motorcycle/truck spot compatibility enforced per SpotType",
        ],
        "elevator": [
            "synchronize addRequest on each Elevator instance",
            "Multiple hall calls same floor — idempotent queue add",
            "stepAll() can run on scheduler thread — readers see consistent floor",
            "Invalid floor → InvalidFloorException",
        ],
        "movie-ticket-booking": [
            "SeatLock with TTL — synchronized per Seat during hold",
            "Double booking prevented by atomic seat state transition",
            "Expired hold releases seat for other buyers",
            "confirm() validates lock still valid and owned by session",
        ],
        "hotel-booking": [
            "synchronize createBooking per Room — prevent overlapping reservations",
            "Optimistic: check-then-act on availability calendar",
            "Cancel races with check-in — state machine on Booking",
            "RoomUnavailableException when dates overlap",
        ],
        "shopping-cart": [
            "Per-session cart — ConcurrentHashMap by sessionId if multi-thread",
            "addItem validates inventory via InventoryService",
            "checkout is single-use — clear cart after order",
            "Coupon apply validates expiry and usage limits",
        ],
        "rate-limiter": [
            "synchronized allowRequest or AtomicLong for token count",
            "Refill tokens based on elapsed time — monotonic clock",
            "Per-client map — ConcurrentHashMap for client state",
            "RateLimitExceededException when rejected",
        ],
    }
    return per_slug.get(slug, [
        "Single-threaded MVP unless clarifying assumes concurrent access",
        "If multi-user: synchronize on mutable aggregates or use concurrent collections",
        "Fail fast on invalid input with domain exceptions",
        "Idempotent retries where duplicate operations are possible",
    ])


def build_followups(slug: str, iface: str, title: str) -> list[str]:
    custom = {
        "chess": ["Implement castling and en passant?", "Add move history with Command undo?", "Detect threefold repetition?", "AI opponent via minimax extension?"],
        "lru-cache": ["Implement thread-safe version?", "Add TTL eviction?", "Persist to disk on shutdown?", "Distributed cache at HLD level?"],
        "parking-lot": ["Dynamic pricing by hour?", "Reserved spots?", "Multi-garage registry?", "Test allocation strategy in isolation?"],
        "rag-orchestrator": ["Add hybrid search retriever?", "Stream tokens to client?", "Cache retrieval results?", "Multi-tenant prompt isolation?"],
        "dining-philosophers": ["Compare waiter vs ordered forks?", "What if one philosopher is greedy?", "Extend to multiple tables?", "Model with semaphores instead?"],
        "strategy-payment": ["Add Apple Pay gateway?", "Handle idempotent retries?", "PCI compliance at HLD?", "Refund flow design?"],
        "in-memory-file-system": ["Add permissions chmod?", "Symbolic links?", "Copy/move operations?", "Persist FS snapshot?"],
    }
    return custom.get(slug, [
        f"How would you unit test `{iface}` in isolation?",
        f"How would you extend {title} without modifying core service?",
        "How would you add persistence behind a Repository?",
        "How does this map to a distributed HLD?",
    ])


def build_extensibility(slug: str, iface: str, service: str, entities: list[tuple[str, str]]) -> list[str]:
    e0 = entities[0][0] if entities else "Entity"
    custom = {
        "parking-lot": [
            "Electric spots: SpotType.ELECTRIC + ChargingCapable interface on ElectricSpot.",
            "Pricing: inject PricingStrategy into PaymentService without changing park loop.",
        ],
        "vending-machine": [
            "Card payment: new PaymentProcessor alongside coin flow.",
            "New product category: extend Product type enum and slot configuration.",
        ],
        "logger": [
            "New appender: implement LogAppender — file, syslog, remote without changing Logger.",
            "Custom formatter: pluggable Formatter per appender.",
        ],
        "notification-system": [
            "New channel: implement ChannelSender for Slack, webhook, etc.",
            "User prefs: Subscriber chooses channels per notification type.",
        ],
        "rag-orchestrator": [
            "Hybrid retriever: combine keyword + vector behind composite Retriever.",
            "GuardrailChain wraps Generator output — Chain of Responsibility.",
        ],
    }
    return custom.get(slug, [
        f"New `{iface}` implementation plugs in at runtime — no change to `{service}`.",
        f"Add new `{e0}` subtypes or enum values for new categories — Open-Closed.",
    ])


def build_tradeoffs(slug: str, iface: str) -> list[tuple[str, str, str, str]]:
    custom = {
        "lru-cache": [
            ("Structure", "LinkedHashMap", "HashMap + DLL", "DLL — explicit O(1) control"),
            ("Eviction", "FIFO", "LRU", "LRU per requirement"),
            ("Thread safety", "None", "synchronized", "sync for MVP concurrent"),
            ("Capacity", "fixed", "dynamic resize", "fixed at construction"),
        ],
        "chess": [
            ("Piece rules", "switch type", "polymorphism", "polymorphism — OCP"),
            ("Move validation", "in Piece", "MoveValidator", "split — SRP"),
            ("Board", "2D array", "Map of squares", "2D array — simple"),
            ("Undo", "none", "Command", "Command extension"),
        ],
        "vending-machine": [
            ("State", "enum", "State pattern", "State — side effects per state"),
            ("Change", "greedy coins", "DP optimal", "greedy — US coin standard"),
            ("Inventory", "per slot", "central", "per slot — realistic"),
            ("Payment", "coins only", "multi-method", "coins MVP"),
        ],
        "messenger-1to1": [
            ("Storage", "in-memory list", "Repository", "Repository interface"),
            ("Ordering", "timestamp", "sequence ID", "sequence — strict order"),
            ("Group chat", "extend Conversation", "new model", "extend with type enum"),
            ("Delivery", "fire-and-forget", "ack/retry", "status enum MVP"),
        ],
    }
    return custom.get(slug, [
        ("Variation", "if/else", iface, f"{iface} — 2+ behaviors"),
        ("State", "enum", "State pattern", "enum for simple lifecycles"),
        ("Storage", "in-memory", "Repository", "in-memory MVP"),
        ("API return", "primitive", "domain object", "domain object — type safety"),
    ])


def build_functional(slug: str, service: str, problem: str, entities: list[tuple[str, str]]) -> list[str]:
    custom = {
        "library-management": [
            "Checkout BookItem to Member if available and under loan limit",
            "Return item and compute overdue fine",
            "Reserve book when all copies checked out — FIFO queue",
            "Librarian catalog add/remove operations",
        ],
        "chess": [
            "Validate and execute legal moves for current player",
            "Detect check, checkmate, and stalemate",
            "Alternate turns between white and black",
            "Reject illegal moves with clear exception",
        ],
        "lru-cache": [
            "get(key) returns value and marks entry most-recently-used",
            "put(key, value) inserts or updates; evicts LRU when at capacity",
            "O(1) time for get and put",
            "Reject or handle null key per API contract",
        ],
    }
    if slug in custom:
        return custom[slug]
    return [
        f"{service} orchestrates end-to-end {problem.split('.')[0].lower()}",
        "Validate all inputs before mutating domain state",
        f"Delegate variable behavior to strategy/interface collaborators",
        "Return typed domain objects; throw exceptions on rule violations",
        "Support primary happy path and explicit failure modes",
    ]


def build_clarify(slug: str, title: str, problem: str, iface: str, track: str) -> list[tuple[str, str]]:
    base = [
        (f"What is MVP scope for {title}?", "Core entities + 2 primary user flows"),
        ("Persistence required?", "In-memory; Repository interface if interviewer asks"),
        ("Multi-threaded access?", "Yes if multiple users/gates — else single-threaded"),
        (f"Main extension point?", f"`{iface}` interface for swappable behavior"),
        ("Error handling?", "Domain exceptions — fail fast on invalid input"),
    ]
    extra = CLARIFY_EXTRA.get(slug, [
        (f"Key business rule?", f"Derived from problem: {problem[:70]}..."),
        ("Distributed deployment?", "Single JVM for LLD; HLD if scale required"),
        ("Authentication?", "Out of scope unless core to problem"),
    ])
    combined = base + extra
    return combined[:8]


def enrich_spec(spec: dict, override_keys: set | None = None) -> dict:
    """Add Parking Lot-level fields to a spec dict from make_spec."""
    from _bulk_slug_data import METHODS as BMETHODS, CLARIFY as BCLARIFY, PATTERNS as BPATTERNS, SCRIPT as BSCRIPT, FUNCTIONAL as BFUNCT  # noqa: WPS433

    slug = spec["slug"]
    title = spec["title"]
    service = spec["service"]
    entities = spec["entities"]
    track = spec["track"]
    problem = spec["problem"]
    override_keys = override_keys or set()

    iface = spec["patterns"][0][0] if spec.get("patterns") else "Strategy"
    if track == "patterns" and "—" in title:
        iface = title.split("—")[0].strip()

    patterns = PATTERN_MAP.get(slug) or BPATTERNS.get(slug) or spec.get("patterns", [(iface, f"Core pattern for {title}")])
    methods = METHODS_MAP.get(slug) or BMETHODS.get(slug) or spec.get("methods", [f"void execute({entities[0][0]} request)"])
    verbs = ", ".join(f"`{m.split('(')[0].split()[-1]}()`" for m in methods[:4])

    happy, fail = build_happy_fail(slug, service, entities, methods)

    updates = {
        "patterns": patterns,
        "methods": methods,
        "verbs": verbs,
        "happy_seq": happy,
        "fail_seq": fail,
        "concurrency": build_concurrency(slug, track, entities),
        "followups": build_followups(slug, patterns[0][0], title),
        "extensibility": build_extensibility(slug, patterns[0][0], service, entities),
        "tradeoffs": build_tradeoffs(slug, patterns[0][0]),
        "mermaid_class": build_mermaid_class(service, methods, entities, ""),
    }
    if "clarify" not in override_keys:
        if slug in CLARIFY_EXTRA:
            updates["clarify"] = (build_clarify(slug, title, problem, patterns[0][0], track)[:3]
                                  + CLARIFY_EXTRA[slug])[:8]
        elif slug in BCLARIFY:
            updates["clarify"] = BCLARIFY[slug][:8]
        else:
            updates["clarify"] = build_clarify(slug, title, problem, patterns[0][0], track)
    if "functional" not in override_keys:
        updates["functional"] = BFUNCT.get(slug) or build_functional(slug, service, problem, entities)
    if "script" not in override_keys:
        updates["script"] = BSCRIPT.get(slug) or build_script(slug, title, service, entities, patterns[0][0], track, problem)

    spec.update(updates)
    return spec
