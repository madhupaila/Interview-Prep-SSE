#!/usr/bin/env python3
"""Generate _bulk_slug_data.py with per-slug METHODS, CLARIFY, PATTERNS, SCRIPT for all META questions."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(ROOT))
from gen_all_specs import META

def camel(s):
    return "".join(w.capitalize() for w in re.sub(r"[^a-z0-9]+", " ", s.lower()).split())

def infer_methods(service, slug, entities, problem):
    p = problem.lower()
    primary = entities[0][0] if entities else "Request"
    e1 = entities[1][0] if len(entities) > 1 else primary

    rules = [
        (r"checkout|borrow|lend", ["Loan checkout(Member member, String id)", "void returnItem(String id)", "void reserve(String isbn)"]),
        (r"bookmark", ["Bookmark addBookmark(String url, String title, String folderId)", "Folder createFolder(String name, String parentId)", "List<Bookmark> search(String query)", "void addTag(String bookmarkId, String tag)"]),
        (r"\bbook\b|reserv", ["Booking create(Guest guest, Room room, LocalDateRange dates)", "void cancel(String bookingId)", "List<Room> searchAvailable(RoomType type, LocalDateRange dates)"]),
        (r"chess|move", ["boolean makeMove(Move move)", "GameState getState()", "List<Move> getLegalMoves()"]),
        (r"cache|lru", ["V get(K key)", "void put(K key, V value)", "int size()"]),
        (r"rate limit", ["boolean allowRequest(String clientKey)", "void reset(String clientKey)"]),
        (r"log", ["void log(LogLevel level, String message)", "void addAppender(LogAppender appender)"]),
        (r"vending|dispense", ["void insertCoin(Coin coin)", "Product selectItem(String code)", "void dispense()"]),
        (r"wishlist", ["void addItem(String productId)", "void removeItem(String productId)", "void shareWishlist(String userId)"]),
        (r"auction|bid", ["void placeBid(String lotId, BigDecimal amount)", "Bid getHighestBid(String lotId)", "void closeAuction(String lotId)"]),
        (r"calendar|event", ["void addEvent(Event event)", "List<Event> getEvents(LocalDate day)", "void setRecurrence(String eventId, RecurrenceRule rule)"]),
        (r"meeting|schedul", ["Meeting schedule(Meeting meeting)", "List<TimeSlot> findAvailability(List<Participant> users)", "void cancelMeeting(String meetingId)"]),
        (r"notification", ["void notify(User user, Notification notification)", "void registerChannel(User user, Channel channel)"]),
        (r"messenger|message|chat", ["Message sendMessage(String conversationId, String text)", "Conversation getOrCreate(User a, User b)", "void markRead(String messageId)"]),
        (r"cart|shopping", ["void addItem(String sku, int qty)", "void removeItem(String sku)", "CheckoutResult checkout()"]),
        (r"inventory|stock|warehouse", ["void reserve(String sku, int qty)", "void release(String sku, int qty)", "int getAvailable(String sku)"]),
        (r"split|expense", ["void addExpense(Expense expense)", "Map<User, BigDecimal> getBalances(Group group)", "void settle(User from, User to, BigDecimal amount)"]),
        (r"file system|mkdir|unix", ["void mkdir(String path)", "void cd(String path)", "List<String> ls()", "String cat(String path)"]),
        (r"ticket|seat|cinema", ["SeatLock holdSeats(Show show, List<Seat> seats)", "Booking confirm(SeatLock lock)", "void releaseHold(SeatLock lock)"]),
        (r"ride|uber|trip", ["Trip requestRide(Rider rider, Location pickup, Location dropoff)", "void acceptTrip(Driver driver, String tripId)", "void completeTrip(String tripId)"]),
        (r"playlist|song", ["void addSong(String playlistId, String songId)", "void shuffle(String playlistId)", "List<Song> playNext()"]),
        (r"feed|post", ["Feed getFeed(User user, Cursor cursor)", "Post createPost(User author, String content)", "void addReaction(String postId, Reaction reaction)"]),
        (r"comment|thread", ["Comment addComment(String postId, String text, String parentId)", "List<Comment> getThread(String postId)", "void upvote(String commentId)"]),
        (r"coupon|discount", ["Discount applyCoupon(Cart cart, String code)", "boolean validateCoupon(String code, Cart cart)"]),
        (r"loyalty|points", ["void earnPoints(String memberId, int points)", "void redeemPoints(String memberId, int points)", "RewardTier getTier(String memberId)"]),
        (r"locker|parcel", ["PickupCode deposit(Parcel parcel)", "Parcel pickup(String code)", "Compartment allocate(Size size)"]),
        (r"dispatch|deliver", ["void assignOrder(Order order)", "Driver findNearestDriver(Location loc)", "void updateStatus(String orderId, DeliveryStatus status)"]),
        (r"registration|enroll|course", ["Enrollment enroll(Student student, Section section)", "void joinWaitlist(Student student, Section section)", "boolean checkPrerequisites(Student student, Course course)"]),
        (r"hospital|patient|appointment", ["Appointment book(Patient patient, Doctor doctor, TimeSlot slot)", "void cancelAppointment(String id)", "MedicalRecord getRecord(String patientId)"]),
        (r"gym|check-in|membership", ["void checkIn(String memberId)", "void bookClass(String memberId, String classId)", "void renewMembership(String memberId)"]),
        (r"traffic|intersection", ["void tick()", "void requestPedestrianCrossing()", "Phase getCurrentPhase()"]),
        (r"toll|fastag", ["TollTransaction processToll(Vehicle vehicle)", "void openGate(String laneId)", "BigDecimal calculateFee(VehicleClass vc)"]),
        (r"board game|turn", ["void playTurn(GameAction action)", "boolean isGameOver()", "Player getCurrentPlayer()"]),
        (r"config", ["String get(String key)", "void set(String key, String value)", "void addListener(ConfigListener listener)"]),
        (r"judge|submission|verdict", ["Verdict submit(Submission submission)", "List<TestResult> runTests(Submission submission)"]),
        (r"paste", ["Paste create(String content, Duration ttl)", "Optional<Paste> get(String id)", "void delete(String id)"]),
    ]
    for pat, meths in rules:
        if re.search(pat, p) or re.search(pat, slug.replace("-", " ")):
            return meths

    # Generic from service name
    base = primary.replace("Service", "")
    return [
        f"void create({base} entity)",
        f"Optional<{base}> getById(String id)",
        f"List<{base}> listAll()",
        f"void delete(String id)",
    ]


def infer_patterns(slug, title, entities, track):
    if track == "patterns" and "—" in title:
        pname = title.split("—")[0].strip()
        return [(pname, f"Demonstrate {pname} pattern in {slug}")]
    if track == "concurrency":
        return [("Concurrency", f"Thread-safe design for {title}"), ("Synchronization", "Locks, volatile, or concurrent collections")]
    if track == "genai":
        return PATTERN_GENAI.get(slug, [("Strategy", "Swappable pipeline components"), ("Chain of Responsibility", "Sequential processing stages")])

    names = " ".join(e[0] + " " + e[1] for e in entities).lower()
    found = []
    checks = [
        ("strategy" in names or "policy" in names or "algorithm" in names, "Strategy", "Swappable algorithms"),
        ("state" in names or "status" in names, "State", "Lifecycle state transitions"),
        ("queue" in names, "Queue", "FIFO ordering of work items"),
        ("observer" in names or "subscriber" in names or "listener" in names, "Observer", "Event notification"),
        ("factory" in names, "Factory", "Object creation abstraction"),
        ("composite" in names or "folder" in names or "tree" in names or "hierarch" in names, "Composite", "Tree structures"),
        ("command" in names or "action" in names, "Command", "Encapsulated operations"),
        ("repository" in names or "store" in names, "Repository", "Persistence abstraction"),
        ("mediator" in names or "bus" in names, "Mediator", "Decoupled communication"),
        ("decorator" in names, "Decorator", "Dynamic behavior stacking"),
    ]
    for cond, pat, why in checks:
        if cond:
            found.append((pat, why))
    if not found:
        found = [("Strategy", f"Variation point in {title}")]
    return found[:3]


PATTERN_GENAI = {
    "rag-orchestrator": [("Pipeline", "Retrieve → rerank → generate"), ("Strategy", "Swappable Retriever/Generator")],
    "agent-tool-registry": [("Registry", "Tool lookup"), ("Strategy", "Tool execution")],
    "guardrail-safety-chain": [("Chain of Responsibility", "Filter pipeline")],
    "multi-agent-coordinator": [("Mediator", "Supervisor routes tasks")],
}

def infer_clarify(slug, title, problem, entities, track):
    p = problem.lower()
    qs = [
        (f"What is MVP scope for {title}?", "Core entities + 2 primary flows; extensions deferred"),
        ("Persistence?", "In-memory; Repository interface if interviewer asks"),
        ("Multi-threaded?", "Synchronize shared state if concurrent users assumed"),
    ]
    if "book" in p and "hotel" in p or "room" in p:
        qs += [("Overbooking?", "No — reject overlapping dates"), ("Cancellation?", "Policy-based cancel window"), ("Room types?", "Enum RoomType")]
    elif "bookmark" in slug:
        qs += [("Nested folders?", "Yes — folder tree"), ("Tags?", "Many-to-many on bookmarks"), ("Duplicate URLs?", "Reject or merge per policy"), ("Search?", "By title and tag")]
    elif "chess" in slug:
        qs += [("Two players?", "Human vs human"), ("Special moves?", "Castling, en passant in scope"), ("Undo?", "Command pattern extension")]
    elif "wishlist" in slug:
        qs += [("Share wishlist?", "Read-only link to friends"), ("Price alerts?", "Observer on price drop"), ("Multiple lists?", "One per user MVP")]
    elif "auction" in slug:
        qs += [("Bid increment?", "Minimum raise rule"), ("Anti-sniping?", "Extend end time on late bid"), ("Reserve price?", "Optional hidden minimum")]
    elif track == "concurrency":
        qs += [("Lock vs synchronized?", "Justify choice"), ("Deadlock prevention?", "Ordering or timeout"), ("Fairness?", "Document starvation risk")]
    elif track == "genai":
        qs += [("Vector DB?", "HLD — stub interface in LLD"), ("Streaming?", "Extension"), ("Token limits?", "Budget manager or truncate")]
    else:
        # Extract key phrases from problem
        parts = [s.strip() for s in re.split(r"[:,]", problem) if len(s.strip()) > 5][:3]
        for i, part in enumerate(parts):
            qs.append((f"Requirement: {part[:40]}?", f"Include in MVP — {part[:50]}"))
    while len(qs) < 8:
        qs.append(("Scale to distributed?", "Single JVM LLD; pivot HLD if asked"))
    return qs[:8]


def infer_script(slug, title, service, entities, problem, track):
    names = ", ".join(f"`{e[0]}`" for e in entities[:6])
    paras = [
        f"I'll design {title} — clarify in-memory scope and MVP flows first.",
        f"Entities: {names}. Domain structure separate from `{service}` orchestration.",
        f"Problem: {problem}",
    ]
    for e, role in entities[:3]:
        paras.append(f"`{e}` — {role.lower()}; owns its own invariants.")
    paras += [
        f"`{service}` validates input, coordinates entities, returns typed results.",
        "Identify variation points — inject interfaces for Open-Closed extensibility.",
        "Walk happy path on whiteboard, then failure case with domain exception.",
        "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification.",
    ]
    if track == "concurrency":
        paras.append("Call out shared mutable state, lock granularity, and deadlock prevention explicitly.")
    elif track == "genai":
        paras.append("LLD = pipeline objects; vector DB, GPUs, queues are HLD extensions.")
    elif track == "patterns":
        paras.append("Name the pattern early, show why it fits — avoid pattern soup.")
    else:
        paras.append("If scale-out needed, pivot to HLD — this object model still holds.")
    return paras[:10]


def infer_functional(service, problem, entities, slug=""):
    p = problem.lower()
    if "bookmark" in slug:
        return [
            "Add bookmark with URL validation and folder placement",
            "Organize bookmarks in nested folder tree (Composite)",
            "Tag bookmarks for multi-label classification",
            "Search bookmarks by title, URL, or tag",
        ]
    items = []
    for kw, action in [
        ("checkout", "Checkout and return items with business rules"),
        ("search", "Search and filter matching resources"),
        ("reserv", "Create and cancel reservations with conflict checks"),
        ("bid", "Place bids with validation and winner selection"),
        ("send", "Send messages with delivery status tracking"),
        ("notify", "Deliver notifications via configured channels"),
        ("split", "Split expenses and track balances"),
        ("park", "Park and unpark with spot assignment"),
        ("play", "Execute game turns with rule validation"),
    ]:
        if kw in p and not (kw == "book" and "bookmark" in p):
            items.append(action)
    if not items:
        items = [
            f"{service} handles primary workflow described in requirements",
            "Validate inputs before state changes",
            "Enforce domain constraints with exceptions",
            "Support listing and lookup of core entities",
        ]
    return items[:5]


bulk = {"METHODS": {}, "CLARIFY": {}, "PATTERNS": {}, "SCRIPT": {}, "FUNCTIONAL": {}}

for track_key, rows in META.items():
    tk = "classic" if track_key == "classic_rest" else track_key.replace("_rest", "")
    for row in rows:
        num, slug, title, companies, diff, problem, service, entities, iface, hld, impl = row
        bulk["METHODS"][slug] = infer_methods(service, slug, entities, problem)
        bulk["CLARIFY"][slug] = infer_clarify(slug, title, problem, entities, tk)
        bulk["PATTERNS"][slug] = infer_patterns(slug, title, entities, tk)
        bulk["SCRIPT"][slug] = infer_script(slug, title, service, entities, problem, tk)
        bulk["FUNCTIONAL"][slug] = infer_functional(service, problem, entities, slug)

out = ROOT / "_bulk_slug_data.py"
out.write_text(
    "# Auto-generated bulk per-slug content\n"
    f"METHODS = {repr(bulk['METHODS'])}\n\n"
    f"CLARIFY = {repr(bulk['CLARIFY'])}\n\n"
    f"PATTERNS = {repr(bulk['PATTERNS'])}\n\n"
    f"SCRIPT = {repr(bulk['SCRIPT'])}\n\n"
    f"FUNCTIONAL = {repr(bulk['FUNCTIONAL'])}\n",
    encoding="utf-8",
)
print(f"Wrote {out} with {len(bulk['METHODS'])} slugs")
