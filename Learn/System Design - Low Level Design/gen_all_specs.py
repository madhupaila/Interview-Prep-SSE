#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-shot generator: writes _specs_*.py batch files with all 114 problem-specific specs."""

from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _cl(*pairs):
    return list(pairs)


# (num, slug, title, companies, diff, problem, service, entities_names, iface, hld, impl)
# entities_names: list of (name, role_short)
META: dict[str, list] = {
    "classic_rest": [
        (3,"library-management","Library Management System","Amazon, Google, Microsoft","Medium",
         "Design a library: catalog books, member accounts, checkout/return, reservations, fines.",
         "LendingService",[("Library","Catalog root"),("Book","Metadata"),("BookItem","Physical copy"),("Member","Borrower"),("ReservationQueue","FIFO waitlist"),("FineStrategy","Overdue fees")],
         "FineStrategy",None,"full"),
        (4,"hotel-booking","Hotel Booking System","Airbnb, Amazon, Booking.com","Medium",
         "Design hotel room booking: search availability, reserve, cancel, check-in/out.",
         "BookingService",[("Hotel","Property"),("Room","Inventory unit"),("Guest","Customer"),("Booking","Reservation record"),("RoomType","Single/Double/Suite"),("AvailabilityCalendar","Date index")],
         "PricingStrategy",None,"full"),
        (5,"restaurant-food-ordering","Restaurant / Food Ordering","DoorDash, Uber, Swiggy","Medium",
         "Design in-restaurant ordering: menu, cart, kitchen queue, order status.",
         "OrderService",[("Restaurant","Venue"),("Menu","Items"),("Order","Customer order"),("OrderItem","Line item"),("KitchenQueue","Prep queue"),("OrderStatus","State enum")],
         "OrderState",None,"full"),
        (6,"chess","Chess Game","Microsoft, Google, Meta","Hard",
         "Design a two-player chess game with move validation, check/checkmate, turn management.",
         "ChessGame",[("Board","8x8 grid"),("Piece","Abstract piece"),("Move","From/to squares"),("Player","Color side"),("MoveValidator","Legal move rules"),("GameState","ACTIVE/CHECKMATE")],
         "MoveValidator",None,"full"),
        (7,"tic-tac-toe","Tic-Tac-Toe","Amazon, Google","Easy",
         "Design tic-tac-toe for two players with win/draw detection on NxN board.",
         "GameService",[("Board","NxN grid"),("Player","X or O"),("Game","Match state"),("WinChecker","Row/col/diag scan")],
         "WinChecker",None,"full"),
        (8,"snake-and-ladder","Snake and Ladder","Amazon, Flipkart","Medium",
         "Design snake-and-ladder board game with dice rolls, snakes, ladders, and win condition.",
         "GameEngine",[("Board","Cells with jumps"),("Player","Position"),("Dice","Random 1-6"),("Snake","Down jump"),("Ladder","Up jump")],
         "Dice",None,"full"),
        (9,"deck-of-cards","Deck of Cards","Amazon, Microsoft","Medium",
         "Design a deck of cards supporting shuffle, deal, and card games (blackjack MVP).",
         "DeckService",[("Card","Suit + rank"),("Deck","52 cards"),("Hand","Player cards"),("ShuffleStrategy","Randomize order"),("Game","Blackjack rules")],
         "ShuffleStrategy",None,"full"),
        (10,"vending-machine","Vending Machine","Amazon, Coca-Cola","Medium",
         "Design vending machine: select item, insert coins, dispense, return change.",
         "VendingMachine",[("Machine","Inventory + cash"),("Slot","Product row"),("Product","Item"),("Coin","Denomination"),("Inventory","Stock count"),("DispenseState","Idle/selection/payment")],
         "State",None,"full"),
        (11,"atm","ATM Machine","Citibank, Amazon, Wells Fargo","Medium",
         "Design ATM: card auth, PIN, balance, withdraw, deposit, transfer.",
         "ATMService",[("ATM","Terminal"),("BankAccount","Balance"),("Card","Auth token"),("Transaction","Audit record"),("CashDispenser","Notes out"),("AuthenticationService","PIN check")],
         "TransactionStrategy",None,"full"),
        (12,"coffee-machine","Coffee Machine","Starbucks, Nestlé","Medium",
         "Design coffee machine with recipes, ingredients inventory, and brew states.",
         "CoffeeMaker",[("Machine","Hardware facade"),("Recipe","Espresso/latte steps"),("Ingredient","Beans/milk/water"),("Beverage","Output"),("BrewState","Idle/heating/brewing")],
         "Recipe",None,"skeleton"),
        (13,"lru-cache","LRU Cache","Amazon, Google, Meta","Medium",
         "Design in-memory LRU cache with O(1) get/put and capacity eviction.",
         "LRUCache",[("LRUCache","Capacity-bound store"),("Node","Key-value DLL node"),("DoublyLinkedList","Recency order"),("HashMap","Key to node")],
         "EvictionPolicy",None,"full"),
        (14,"rate-limiter","Rate Limiter","Amazon, Stripe, Cloudflare","Medium",
         "Design rate limiter: allow N requests per window per client key.",
         "RateLimiter",[("RateLimiter","Facade"),("ClientKey","User/IP id"),("TokenBucket","Burst control"),("SlidingWindow","Time buckets"),("RateLimitRule","N per window")],
         "RateLimitAlgorithm",None,"full"),
        (15,"logger","Logger / Log Aggregator","Splunk, Datadog, Amazon","Medium",
         "Design leveled logger with multiple appenders (console, file) and formatting.",
         "Logger",[("Logger","Facade"),("LogLevel","DEBUG..ERROR"),("LogAppender","Output sink"),("ConsoleAppender","Stdout"),("FileAppender","Disk"),("Formatter","Pattern layout")],
         "LogAppender",None,"full"),
        (16,"task-scheduler","Task Scheduler","Amazon, Google, Microsoft","Medium",
         "Design task scheduler executing jobs by priority or cron expression.",
         "TaskScheduler",[("Scheduler","Job runner"),("Task","Runnable unit"),("JobQueue","Priority queue"),("Worker","Execution thread"),("CronExpression","Schedule parser")],
         "SchedulingPolicy",None,"full"),
        (17,"in-memory-file-system","In-Memory File System","Amazon, Google","Hard",
         "Design Unix-like in-memory FS: mkdir, ls, cd, touch, cat, find.",
         "FileSystem",[("FileSystem","Root /"),("INode","File or directory"),("Directory","Children map"),("File","Byte content"),("PathResolver","Normalize paths")],
         "INode",None,"full"),
        (18,"splitwise","Splitwise Expense Sharing","Splitwise, Amazon","Medium",
         "Design expense sharing: add bill, split equally/percent, settle balances.",
         "ExpenseService",[("User","Member"),("Group","Expense group"),("Expense","Bill record"),("Split","Per-user share"),("BalanceSheet","Who owes whom")],
         "SplitStrategy",None,"full"),
        (19,"movie-ticket-booking","Movie Ticket Booking","BookMyShow, Amazon","Medium",
         "Design cinema booking: shows, seats, lock seats, payment, confirm.",
         "BookingService",[("Cinema","Theater"),("Show","Movie + time"),("Screen","Hall"),("Seat","Row/col status"),("Booking","Confirmed tickets"),("SeatLock","Temporary hold")],
         "PricingStrategy",None,"full"),
        (20,"car-rental","Car Rental System","Hertz, Amazon, Enterprise","Medium",
         "Design car rental: fleet, reservations, pickup/return, pricing.",
         "RentalService",[("RentalAgency","Fleet owner"),("Vehicle","Rentable car"),("Reservation","Date range booking"),("Customer","Renter"),("Invoice","Charges")],
         "PricingStrategy",None,"full"),
        (21,"ride-sharing-uber","Ride Sharing (Uber)","Uber, Lyft, Amazon","Hard",
         "Design ride matching: request ride, match driver, trip lifecycle, fare.",
         "RideService",[("Rider","Passenger"),("Driver","Supply side"),("Trip","Active ride"),("Location","GPS point"),("FareCalculator","Pricing"),("MatchingStrategy","Driver selection")],
         "MatchingStrategy","03-classic-hld/questions/Q12-ride-sharing.md","full"),
        (22,"shopping-cart","Shopping Cart","Amazon, Walmart, Shopify","Medium",
         "Design e-commerce cart: add/remove items, quantity, apply coupon, checkout.",
         "CartService",[("ShoppingCart","Session cart"),("CartItem","SKU + qty"),("Product","Catalog item"),("Customer","Shopper"),("Coupon","Discount rule")],
         "DiscountStrategy",None,"full"),
        (23,"inventory-management","Inventory Management","Amazon, Walmart","Medium",
         "Design warehouse inventory: SKUs, stock levels, reserve, reorder alerts.",
         "InventoryService",[("Warehouse","Storage site"),("SKU","Product id"),("StockLevel","Quantity on hand"),("Reservation","Allocated stock"),("ReorderPolicy","Low stock alert")],
         "ReorderPolicy",None,"full"),
        (24,"messenger-1to1","Messenger (1:1 Chat)","Meta, WhatsApp, Slack","Medium",
         "Design 1:1 messaging: send, deliver, read receipts, conversation threads.",
         "MessageService",[("User","Participant"),("Conversation","Two-user thread"),("Message","Text payload"),("DeliveryStatus","Sent/delivered/read"),("Inbox","Conversation list")],
         "MessageStore",None,"full"),
        (25,"notification-system","Notification System","Amazon, Twilio, Slack","Medium",
         "Design multi-channel notifications: email, SMS, push with templates.",
         "NotificationService",[("Notification","Payload"),("Channel","EMAIL/SMS/PUSH"),("Template","Message body"),("Subscriber","Recipient prefs"),("ChannelSender","Delivery adapter")],
         "ChannelSender",None,"full"),
        (26,"meeting-scheduler","Meeting Scheduler","Google, Microsoft, Zoom","Medium",
         "Design meeting scheduler: propose slots, check conflicts, book room.",
         "SchedulerService",[("Meeting","Event"),("Participant","Attendee"),("Calendar","Availability"),("TimeSlot","Start/end"),("Room","Physical resource"),("ConflictChecker","Overlap detection")],
         "ConflictChecker",None,"full"),
        (27,"calendar","Calendar Application","Apple, Google, Microsoft","Medium",
         "Design personal calendar: events, recurring rules, reminders, views.",
         "CalendarService",[("Calendar","Event container"),("Event","Title/time/location"),("RecurrenceRule","RRULE pattern"),("Reminder","Alert before event"),("EventView","Day/week/month")],
         "RecurrenceRule",None,"full"),
        (28,"stackoverflow-qa","Stack Overflow Q&A","Stack Overflow, Google","Medium",
         "Design Q&A platform object model: questions, answers, votes, tags, reputation.",
         "QAService",[("Question","Post"),("Answer","Response"),("User","Reputation holder"),("Vote","Up/down"),("Tag","Topic label"),("ReputationService","Score updates")],
         "VotePolicy",None,"skeleton"),
        (29,"pubsub-event-bus","Pub/Sub Event Bus","Amazon, Google, Kafka","Medium",
         "Design in-process pub/sub: topics, subscribers, async delivery.",
         "EventBus",[("EventBus","Broker"),("Topic","Channel name"),("Event","Payload"),("Subscriber","Listener"),("Subscription","Topic binding")],
         "EventHandler",None,"full"),
        (30,"parking-meter","Parking Meter","City apps, Amazon","Easy",
         "Design parking meter: pay for duration, expire, fine extension.",
         "ParkingMeter",[("Meter","Street device"),("Vehicle","Plate id"),("Payment","Coins/card"),("ParkingSession","Active timer"),("RateTable","Price per hour")],
         "RateTable",None,"skeleton"),
        (31,"hotel-key-card","Hotel Key Card System","Marriott, Hilton","Medium",
         "Design hotel key card: encode room access, expiry, revoke on checkout.",
         "KeyCardService",[("KeyCard","RFID token"),("Room","Access target"),("Guest","Holder"),("AccessPolicy","Time-bound rules"),("Encoder","Write card")],
         "AccessPolicy",None,"skeleton"),
        (32,"warehouse-locker","Warehouse Locker Service","Amazon, UPS","Medium",
         "Design parcel lockers: allocate compartment, deposit, pickup code.",
         "LockerService",[("LockerBank","Kiosk cluster"),("Compartment","Sized bin"),("Parcel","Package"),("PickupCode","One-time token"),("AllocationStrategy","Size fit")],
         "AllocationStrategy",None,"full"),
        (33,"delivery-dispatch","Delivery Dispatch","DoorDash, Amazon, FedEx","Medium",
         "Design last-mile dispatch: assign orders to drivers by proximity.",
         "DispatchService",[("Order","Delivery request"),("Driver","Courier"),("Route","Stop sequence"),("DispatchStrategy","Assignment algo"),("DeliveryStatus","Lifecycle enum")],
         "DispatchStrategy",None,"full"),
        (34,"course-registration","Course Registration","Coursera, Amazon","Medium",
         "Design university registration: courses, seats, waitlist, prerequisites.",
         "RegistrationService",[("Student","Enrollee"),("Course","Offering"),("Section","Time slot"),("Enrollment","Seat record"),("Waitlist","FIFO queue"),("PrerequisiteChecker","Rules")],
         "PrerequisiteChecker",None,"full"),
        (35,"hospital-management","Hospital Management","Epic, Cerner, Amazon","Hard",
         "Design hospital system: patients, doctors, appointments, medical records.",
         "HospitalService",[("Patient","Medical record owner"),("Doctor","Provider"),("Appointment","Scheduled visit"),("Department","Ward"),("MedicalRecord","History"),("BillingAccount","Charges")],
         "SchedulingStrategy",None,"skeleton"),
        (36,"gym-membership","Gym Membership","Amazon, Planet Fitness","Medium",
         "Design gym: memberships, check-in, class booking, billing.",
         "GymService",[("Member","Subscription holder"),("MembershipPlan","Tier"),("CheckIn","Facility access"),("FitnessClass","Scheduled session"),("Payment","Monthly fee")],
         "MembershipPlan",None,"skeleton"),
        (37,"auction-system","Auction System","eBay, Amazon","Medium",
         "Design auction: place bid, anti-sniping, highest bidder wins.",
         "AuctionService",[("Auction","Listing + end time"),("Bid","Amount + bidder"),("Bidder","User"),("AuctionStatus","OPEN/CLOSED"),("BidValidator","Min increment")],
         "BidValidator",None,"full"),
        (38,"parking-garage","Parking Garage Multi-Entry","Amazon, Simon","Hard",
         "Design multi-entry garage with per-entrance displays and central occupancy.",
         "GarageService",[("Garage","Multi-floor structure"),("EntryGate","Ingress point"),("ExitGate","Egress + payment"),("OccupancyBoard","Live counts"),("CentralRegistry","Cross-gate sync")],
         "ParkingStrategy","03-classic-hld/questions/Q30-parking-lot-elevator.md","skeleton"),
        (39,"traffic-light","Traffic Light System","City systems, Siemens","Medium",
         "Design intersection traffic lights with timed phases and pedestrian crossing.",
         "TrafficController",[("Intersection","Road junction"),("TrafficLight","Red/yellow/green"),("Phase","Signal sequence"),("Timer","Phase duration"),("PedestrianButton","Walk request")],
         "PhaseSequence",None,"skeleton"),
        (40,"toll-booth","Toll Booth System","Highway authorities","Medium",
         "Design toll plaza: vehicle classification, fee, gate open, FASTag.",
         "TollService",[("TollBooth","Lane"),("Vehicle","Class type"),("TollRate","Price table"),("Transponder","FASTag id"),("Gate","Barrier control")],
         "TollRate",None,"skeleton"),
        (41,"board-game-framework","Board Game Framework","EA, Hasbro","Medium",
         "Design extensible board game framework: board, players, turns, rules engine.",
         "GameFramework",[("Game","Match coordinator"),("Board","Grid/graph"),("Player","Participant"),("RuleEngine","Move validation"),("TurnManager","Next player"),("GameAction","Command")],
         "RuleEngine",None,"full"),
        (42,"playlist-manager","Playlist Manager","Apple Music, Spotify","Medium",
         "Design playlist CRUD, shuffle, repeat, collaborative editing.",
         "PlaylistService",[("Playlist","Ordered tracks"),("Song","Track metadata"),("User","Owner"),("PlaybackQueue","Current order"),("ShuffleStrategy","Random order")],
         "ShuffleStrategy",None,"full"),
        (43,"news-feed-object-model","News Feed Object Model","Meta, Twitter, LinkedIn","Medium",
         "Design feed object model: posts, reactions, ranking stub, pagination.",
         "FeedService",[("Feed","Post list"),("Post","Content item"),("User","Author"),("Reaction","Like/emoji"),("FeedRanker","Ordering strategy"),("Cursor","Pagination token")],
         "FeedRanker",None,"skeleton"),
        (44,"social-graph","Social Graph","Meta, LinkedIn","Medium",
         "Design social graph: follow/friend edges, suggestions, BFS reach.",
         "GraphService",[("User","Node"),("Relationship","Edge type"),("SocialGraph","Adjacency store"),("Follow","Directed edge"),("SuggestionEngine","Friend-of-friend")],
         "SuggestionEngine",None,"skeleton"),
        (45,"friend-request","Friend Request Flow","Meta, LinkedIn","Medium",
         "Design friend requests: send, accept, reject, block, pending state.",
         "FriendService",[("User","Account"),("FriendRequest","Pending invite"),("Friendship","Mutual link"),("BlockList","Blocked users"),("RequestStatus","PENDING/ACCEPTED")],
         "RequestValidator",None,"skeleton"),
        (46,"comment-thread","Comment Thread","Reddit, YouTube","Medium",
         "Design nested comments: post, reply, edit, delete, sort top/new.",
         "CommentService",[("Post","Parent content"),("Comment","Tree node"),("CommentThread","Root collection"),("SortStrategy","Top/new ordering"),("ModerationFlag","Report")],
         "SortStrategy",None,"skeleton"),
        (47,"bookmark-manager","Bookmark Manager","Browser, Pinterest","Easy",
         "Design bookmarks: folders, tags, URL validation, search.",
         "BookmarkService",[("Bookmark","URL + title"),("Folder","Hierarchy"),("Tag","Label"),("BookmarkStore","Persistence"),("SearchIndex","Title lookup")],
         "SearchIndex",None,"skeleton"),
        (48,"wishlist","Wishlist","Amazon, Etsy","Easy",
         "Design product wishlist: add, remove, share, price drop notify.",
         "WishlistService",[("Wishlist","Item collection"),("WishlistItem","Product ref"),("User","Owner"),("Product","Catalog ref"),("PriceAlert","Notification rule")],
         "PriceAlert",None,"skeleton"),
        (49,"coupon-engine","Coupon Engine","Amazon, Shopify","Medium",
         "Design coupon engine: percent/fixed off, min cart, expiry, stack rules.",
         "CouponService",[("Coupon","Code + rules"),("Cart","Order context"),("Discount","Applied amount"),("CouponValidator","Eligibility"),("PromotionRule","Business logic")],
         "PromotionRule",None,"full"),
        (50,"loyalty-points","Loyalty Points","Airlines, Starbucks","Medium",
         "Design loyalty program: earn on purchase, redeem, tier levels.",
         "LoyaltyService",[("Member","Account"),("PointsLedger","Earn/burn log"),("Transaction","Purchase event"),("RewardTier","Silver/gold"),("Redemption","Points to discount")],
         "EarningRule",None,"skeleton"),
        (51,"table-reservation","Table Reservation","OpenTable, Yelp","Medium",
         "Design restaurant table booking: slots, party size, no-show policy.",
         "ReservationService",[("Restaurant","Venue"),("Table","Capacity"),("Reservation","Booking record"),("TimeSlot","Available window"),("Guest","Customer")],
         "AvailabilityChecker",None,"skeleton"),
        (52,"kitchen-order-queue","Kitchen Order Queue","Restaurant POS","Medium",
         "Design kitchen display queue: order priority, prep stations, bump bar.",
         "KitchenService",[("KitchenQueue","Order pipeline"),("OrderTicket","Kitchen card"),("Station","Grill/salad"),("PriorityStrategy","Rush first"),("OrderStatus","PREP/DONE")],
         "PriorityStrategy",None,"skeleton"),
        (53,"drive-thru","Drive-Thru System","Chick-fil-A, McDonald's","Medium",
         "Design drive-thru lane: order post, payment, pickup window sequencing.",
         "DriveThruService",[("DriveThruLane","Single lane"),("OrderPost","Menu board"),("VehicleQueue","FIFO cars"),("Order","Meal order"),("PickupWindow","Handoff point")],
         "LaneSequence",None,"skeleton"),
        (54,"bus-transit","Bus Transit System","City transit","Medium",
         "Design bus routes, stops, schedules, real-time ETA stub.",
         "TransitService",[("Route","Line path"),("Bus","Vehicle"),("Stop","Station"),("Schedule","Timetable"),("Trip","Active run"),("ETAEstimator","Arrival calc")],
         "ETAEstimator",None,"skeleton"),
        (55,"flight-seat-map","Flight Seat Map","Airlines, Expedia","Medium",
         "Design airline seat map: seat types, selection, hold, confirm.",
         "SeatMapService",[("Flight","Segment"),("SeatMap","Layout grid"),("Seat","Row/letter"),("SeatType","Economy/business"),("SeatHold","Temporary lock"),("Passenger","Traveler")],
         "SeatPricing",None,"full"),
        (56,"baggage-carousel","Baggage Carousel","Airports","Easy",
         "Design baggage carousel: load bags, notify passenger, claim verification.",
         "BaggageService",[("Carousel","Belt system"),("Bag","Tagged luggage"),("Flight","Arrival"),("Passenger","Owner"),("BagTag","Barcode id")],
         "ClaimValidator",None,"skeleton"),
        (57,"hotel-housekeeping","Hotel Housekeeping","Marriott, Hilton","Medium",
         "Design housekeeping: room status, task assignment, inspect, DND.",
         "HousekeepingService",[("Room","Status dirty/clean"),("Housekeeper","Staff"),("CleaningTask","Assignment"),("RoomStatus","VACANT/OCCUPIED/DND"),("Inspection","QC check")],
         "TaskAssigner",None,"skeleton"),
        (58,"parking-spot-allocation","Parking Spot Allocation","Amazon, Google","Medium",
         "Design optimal spot allocation service decoupled from payment and gates.",
         "AllocationService",[("SpotRegistry","All spots"),("AllocationRequest","Vehicle type + prefs"),("AllocationStrategy","Algorithm"),("SpotAssignment","Result"),("VehicleType","Size enum")],
         "AllocationStrategy","03-classic-hld/questions/Q30-parking-lot-elevator.md","skeleton"),
        (59,"linkedin-post","LinkedIn Post","LinkedIn, Meta","Medium",
         "Design professional post: text, mentions, visibility, engagement counts.",
         "PostService",[("Post","Content"),("Author","User"),("Mention","@user ref"),("Visibility","PUBLIC/CONNECTIONS"),("Engagement","Like/comment counts")],
         "VisibilityPolicy",None,"skeleton"),
        (60,"digital-wallet","Digital Wallet","PayPal, Apple Pay","Medium",
         "Design wallet: balance, P2P transfer, transaction history, KYC stub.",
         "WalletService",[("Wallet","Balance holder"),("User","Owner"),("Transaction","Ledger entry"),("Transfer","P2P move"),("PaymentMethod","Linked bank/card")],
         "FraudChecker",None,"full"),
        (61,"online-judge","Online Judge","LeetCode, HackerRank","Hard",
         "Design code judge: submit solution, compile, run tests, verdict.",
         "JudgeService",[("Submission","Code + problem"),("Problem","Test cases"),("TestCase","Input/expected"),("Verdict","AC/WA/TLE"),("Sandbox","Isolated runner")],
         "TestRunner",None,"skeleton"),
        (62,"pastebin-ood","Pastebin (OOD)","Pastebin, GitHub Gist","Medium",
         "Design pastebin: create paste, short URL, expiry, privacy.",
         "PastebinService",[("Paste","Content blob"),("ShortUrl","Key mapping"),("Author","Optional user"),("ExpiryPolicy","TTL"),("AccessLevel","PUBLIC/UNLISTED")],
         "ExpiryPolicy",None,"skeleton"),
        (63,"cache-aside-ood","Cache-Aside Pattern (Object)","Amazon, Redis Labs","Medium",
         "Design cache-aside loader: read-through, write-invalidate, stampede guard.",
         "CacheAsideService",[("Cache","Fast store"),("DataStore","Authoritative DB"),("CacheLoader","Miss handler"),("CacheKey","Lookup id"),("InvalidationPolicy","TTL/event")],
         "CacheLoader",None,"full"),
        (64,"config-manager","Config Manager","Netflix, Spring","Medium",
         "Design dynamic config: key-value, environment overrides, change listeners.",
         "ConfigManager",[("ConfigStore","KV source"),("ConfigKey","Namespaced key"),("ConfigSnapshot","Immutable view"),("ConfigListener","Change callback"),("Environment","dev/prod overlay")],
         "ConfigSource",None,"full"),
    ],
    "patterns": [
        (1,"strategy-payment","Strategy — Payment Gateways","Stripe, Amazon, PayPal","Medium",
         "Design payment processing with swappable gateways (Stripe, PayPal, Apple Pay).",
         "PaymentProcessor",[("PaymentProcessor","Strategy interface"),("StripeProcessor","Stripe impl"),("PayPalProcessor","PayPal impl"),("PaymentRequest","Amount + method"),("PaymentResult","Success/fail")],
         "PaymentProcessor",None,"full"),
        (2,"factory-vehicle","Factory — Vehicle Creator","Tesla, Ford, Toyota","Medium",
         "Design factory creating Car, Truck, Motorcycle from VehicleType enum.",
         "VehicleFactory",[("Vehicle","Abstract product"),("Car","4-wheel"),("Truck","Heavy"),("Motorcycle","2-wheel"),("VehicleFactory","Creator")],
         "VehicleFactory",None,"full"),
        (3,"abstract-factory-ui","Abstract Factory — UI Themes","Adobe, Microsoft","Hard",
         "Design abstract factory for Light/Dark UI component families (Button, Checkbox).",
         "UIFactory",[("UIFactory","Abstract factory"),("LightThemeFactory","Light widgets"),("DarkThemeFactory","Dark widgets"),("Button","Widget"),("Checkbox","Widget")],
         "UIFactory",None,"full"),
        (4,"builder-meal","Builder — Meal Combo","McDonald's, Starbucks","Medium",
         "Design builder for meal combos: burger, drink, fries step-by-step.",
         "MealBuilder",[("Meal","Product"),("MealBuilder","Fluent builder"),("Burger","Item"),("Drink","Item"),("MealDirector","Preset combos")],
         "MealBuilder",None,"full"),
        (5,"singleton-thread-safe","Singleton — Thread-Safe Config","Amazon, Spring","Medium",
         "Design thread-safe singleton config holder with lazy initialization.",
         "AppConfig",[("AppConfig","Singleton"),("ConfigProperty","KV entry"),("ConfigLoader","Load from file")],
         "AppConfig",None,"full"),
        (6,"prototype-game-board","Prototype — Game Board Clone","EA, Unity","Medium",
         "Design prototype pattern to clone complex game boards for save/replay.",
         "BoardPrototype",[("GameBoard","Prototype"),("Cell","Board cell"),("BoardRegistry","Template cache"),("Cloneable","Copy interface")],
         "GameBoard",None,"full"),
        (7,"adapter-legacy-payment","Adapter — Legacy Payment API","Banks, Stripe","Medium",
         "Design adapter wrapping legacy XML payment API behind modern interface.",
         "PaymentAdapter",[("ModernPaymentGateway","Target interface"),("LegacyPaymentAPI","Adaptee"),("LegacyPaymentAdapter","Adapter"),("PaymentRequest","DTO")],
         "ModernPaymentGateway",None,"full"),
        (8,"decorator-coffee","Decorator — Coffee Shop","Starbucks","Medium",
         "Design decorator adding milk, whip, caramel to base coffee with dynamic price.",
         "CoffeeDecorator",[("Beverage","Component interface"),("Espresso","Concrete"),("MilkDecorator","Add-on"),("WhipDecorator","Add-on"),("PriceCalculator","Sum cost")],
         "Beverage",None,"full"),
        (9,"facade-home-theater","Facade — Home Theater","Sony, Samsung","Medium",
         "Design facade orchestrating amp, projector, screen, lights for watchMovie().",
         "HomeTheaterFacade",[("HomeTheaterFacade","Simplified API"),("Amplifier","Device"),("Projector","Device"),("Screen","Device"),("Lights","Device")],
         "HomeTheaterFacade",None,"full"),
        (10,"proxy-image-loader","Proxy — Image Loader","Google, Meta","Medium",
         "Design virtual proxy lazy-loading high-res images with placeholder.",
         "ImageProxy",[("Image","Interface"),("HighResImage","Real subject"),("ImageProxy","Lazy loader"),("ImageCache","Memoization")],
         "Image",None,"full"),
        (11,"composite-org-chart","Composite — Org Chart","Workday, SAP","Medium",
         "Design composite for org chart: Employee leaf and Department composite.",
         "OrgComposite",[("OrgComponent","Component"),("Employee","Leaf"),("Department","Composite"),("OrgChart","Root tree")],
         "OrgComponent",None,"full"),
        (12,"bridge-remote-control","Bridge — Remote Control","Samsung, LG","Medium",
         "Design bridge separating remote abstraction from device implementation.",
         "RemoteBridge",[("Remote","Abstraction"),("Device","Implementor"),("TV","Device impl"),("Radio","Device impl"),("AdvancedRemote","Extended abstraction")],
         "Device",None,"full"),
        (13,"observer-stock-ticker","Observer — Stock Price Feed","Bloomberg, Robinhood","Medium",
         "Design observer for stock price updates to multiple display widgets.",
         "StockTicker",[("StockTicker","Subject"),("Observer","Listener"),("PriceDisplay","Concrete observer"),("Stock","Symbol + price")],
         "Observer",None,"full"),
        (14,"command-undo-redo","Command — Undo/Redo","Adobe, Microsoft","Medium",
         "Design command pattern with undo/redo stack for text editor actions.",
         "CommandManager",[("Command","Execute/undo"),("InsertCommand","Concrete"),("CommandHistory","Undo stack"),("Editor","Receiver")],
         "Command",None,"full"),
        (15,"state-vending-machine","State — Vending Machine","Amazon, Coca-Cola","Medium",
         "Design state pattern for vending machine phases: idle, coin, dispense.",
         "VendingStateMachine",[("VendingContext","Context"),("VendingState","State interface"),("IdleState","No coin"),("HasCoinState","Selection"),("DispenseState","Release item")],
         "VendingState",None,"full"),
        (16,"template-method-parser","Template Method — Data Parser","Apache, Elastic","Medium",
         "Design template method for CSV/JSON parsers sharing open-read-parse-close skeleton.",
         "DataParser",[("DataParser","Abstract template"),("CsvParser","Concrete"),("JsonParser","Concrete"),("ParseContext","Input source")],
         "DataParser",None,"full"),
        (17,"iterator-playlist","Iterator — Playlist","Spotify, Apple","Medium",
         "Design custom iterator traversing playlist forward/backward/shuffle.",
         "PlaylistIterator",[("Playlist","Aggregate"),("Iterator","Interface"),("SequentialIterator","Forward"),("ShuffleIterator","Random order")],
         "Iterator",None,"full"),
        (18,"chain-support-tickets","Chain of Responsibility — Support","Amazon, Zendesk","Medium",
         "Design support ticket escalation: L1 → L2 → L3 handler chain.",
         "SupportChain",[("SupportHandler","Abstract handler"),("L1Handler","Tier 1"),("L2Handler","Tier 2"),("Ticket","Request"),("EscalationPolicy","Routing rules")],
         "SupportHandler",None,"full"),
        (19,"mediator-chat-room","Mediator — Chat Room","Discord, Slack","Medium",
         "Design mediator so users send messages through chat room, not peer-to-peer.",
         "ChatMediator",[("ChatRoom","Mediator"),("User","Colleague"),("Message","Payload"),("ChatRoomMediator","Routes messages")],
         "ChatRoom",None,"full"),
        (20,"memento-text-editor","Memento — Text Editor","Microsoft, Adobe","Medium",
         "Design memento for editor snapshots enabling undo to prior document state.",
         "EditorMemento",[("Editor","Originator"),("Memento","Snapshot"),("HistoryCaretaker","Stack of mementos"),("Document","State")],
         "Editor",None,"full"),
        (21,"flyweight-forest","Flyweight — Forest Scene","Unity, EA","Medium",
         "Design flyweight sharing tree intrinsic state (type) across thousands of instances.",
         "TreeFlyweight",[("TreeType","Flyweight"),("Tree","Extrinsic position"),("Forest","Object pool"),("TreeFactory","Cache flyweights")],
         "TreeType",None,"full"),
        (22,"visitor-shopping-cart-tax","Visitor — Cart Tax","Amazon, Intuit","Medium",
         "Design visitor computing tax for mixed cart item types without double dispatch mess.",
         "TaxVisitor",[("CartItem","Element"),("TaxVisitor","Visitor"),("BookItem","Element"),("ElectronicsItem","Element"),("TaxCalculator","Context")],
         "TaxVisitor",None,"full"),
        (23,"strategy-shipping","Strategy — Shipping Calculator","Amazon, FedEx","Medium",
         "Design shipping cost strategies: standard, express, overnight by weight/zone.",
         "ShippingCalculator",[("ShippingStrategy","Interface"),("StandardShipping","Impl"),("ExpressShipping","Impl"),("Package","Weight + zone")],
         "ShippingStrategy",None,"full"),
        (24,"factory-document","Factory — Document Creator","Microsoft, Google","Medium",
         "Design factory method creating PDF, Word, Markdown documents.",
         "DocumentFactory",[("Document","Product"),("PdfDocument","Concrete"),("WordDocument","Concrete"),("DocumentFactory","Creator")],
         "DocumentFactory",None,"full"),
        (25,"combo-parking-payment","Combo — Parking + Payment","Amazon, Stripe","Hard",
         "Combine Strategy (allocation + payment) and Factory (vehicle) in parking lot.",
         "ParkingPaymentFacade",[("ParkingLotService","Orchestrator"),("ParkingStrategy","Spot pick"),("PaymentProcessor","Charge"),("VehicleFactory","Create vehicle"),("Ticket","Park token")],
         "ParkingStrategy","03-classic-hld/questions/Q30-parking-lot-elevator.md","full"),
    ],
    "concurrency": [
        (1,"thread-safe-singleton","Thread-Safe Singleton","Amazon, Google, Microsoft","Medium",
         "Implement thread-safe singleton with double-checked locking or enum idiom.",
         "SingletonHolder",[("Singleton","Single instance"),("InstanceHolder","DCL holder"),("ConfigManager","Use case")],
         "Singleton",None,"full"),
        (2,"bounded-blocking-queue","Bounded Blocking Queue","Amazon, LinkedIn","Hard",
         "Design bounded blocking queue with put/take blocking on full/empty.",
         "BoundedBlockingQueue",[("BoundedBlockingQueue","Buffer"),("Condition","Not full/not empty"),("Node","Queue element")],
         "BlockingQueue",None,"full"),
        (3,"producer-consumer","Producer-Consumer","Amazon, Oracle","Medium",
         "Design producer-consumer with shared bounded buffer and wait/notify.",
         "ProducerConsumer",[("Producer","Adds items"),("Consumer","Removes items"),("SharedBuffer","Bounded queue"),("Coordinator","Start/stop")],
         "SharedBuffer",None,"full"),
        (4,"reader-writer-lock","Reader-Writer Lock","Amazon, Google","Hard",
         "Design read-write lock allowing concurrent readers OR exclusive writer.",
         "ReadWriteLock",[("ReadWriteLock","Sync primitive"),("ReadLock","Shared"),("WriteLock","Exclusive"),("Resource","Protected data")],
         "ReadWriteLock",None,"full"),
        (5,"dining-philosophers","Dining Philosophers","Amazon, Microsoft","Hard",
         "Design deadlock-free dining philosophers with fork acquisition ordering.",
         "DiningTable",[("Philosopher","Thread"),("Fork","Shared resource"),("Table","Seat arrangement"),("Waiter","Arbitrator optional")],
         "Fork",None,"full"),
        (6,"concurrent-lru-cache","Concurrent LRU Cache","Amazon, Meta","Hard",
         "Design thread-safe LRU cache with fine-grained locking or ConcurrentHashMap.",
         "ConcurrentLRUCache",[("ConcurrentLRUCache","Facade"),("Segment","Lock shard"),("Node","DLL entry"),("EvictionPolicy","LRU order")],
         "ConcurrentLRUCache",None,"full"),
        (7,"thread-pool-executor","Thread Pool Executor","Amazon, Google","Hard",
         "Design fixed thread pool with task queue, worker threads, rejection policy.",
         "ThreadPoolExecutor",[("ThreadPool","Worker set"),("TaskQueue","Pending work"),("Worker","Runnable loop"),("RejectedExecutionHandler","Overflow policy")],
         "ThreadPool",None,"full"),
        (8,"rate-limiter-concurrent","Rate Limiter (Concurrent)","Stripe, Cloudflare","Medium",
         "Design distributed-safe token bucket rate limiter with atomic updates.",
         "ConcurrentRateLimiter",[("RateLimiter","Facade"),("TokenBucket","Atomic tokens"),("Clock","Time source"),("ClientKey","Limiter key")],
         "TokenBucket",None,"full"),
        (9,"print-foobar","Print FooBar Alternating","Amazon, Google","Medium",
         "Design two threads printing foo/bar alternately n times using locks.",
         "FooBarPrinter",[("FooBar","Coordinator"),("Lock","Sync"),("Condition","Turn signal")],
         "FooBar",None,"full"),
        (10,"h2o-barrier","H2O Barrier","Google, Amazon","Medium",
         "Design barrier synchronizing H, O threads to form H2O molecules.",
         "H2OSynchronizer",[("H2O","Barrier"),("HydrogenThread","H atom"),("OxygenThread","O atom"),("Molecule","Output unit")],
         "H2O",None,"full"),
        (11,"web-crawler-multithreaded","Web Crawler (Multithreaded)","Google, Microsoft","Hard",
         "Design multi-threaded crawler with visited set, URL frontier, politeness.",
         "WebCrawler",[("Crawler","Coordinator"),("UrlFrontier","BFS queue"),("VisitedSet","Dedup"),("Worker","Fetch thread"),("PageParser","Link extractor")],
         "UrlFrontier",None,"full"),
        (12,"download-manager","Download Manager","Microsoft, Apple","Medium",
         "Design concurrent download manager with chunks, progress, pause/resume.",
         "DownloadManager",[("DownloadTask","File job"),("Chunk","Byte range"),("WorkerPool","Parallel fetch"),("ProgressTracker","Status")],
         "DownloadManager",None,"full"),
        (13,"job-scheduler-pool","Job Scheduler with Worker Pool","Amazon, Airbnb","Hard",
         "Design scheduler dispatching cron jobs to worker pool with at-least-once semantics.",
         "JobSchedulerPool",[("Scheduler","Cron trigger"),("Job","Unit of work"),("WorkerPool","Executors"),("JobStore","Persistence stub")],
         "Scheduler",None,"full"),
        (14,"bank-transfer-deadlock","Bank Transfer Deadlock","Goldman, Citibank","Hard",
         "Design deadlock-free concurrent transfers between bank accounts.",
         "TransferService",[("Account","Balance"),("Transfer","Move funds"),("LockOrdering","Consistent lock order"),("TransactionLog","Audit")],
         "LockOrdering",None,"full"),
        (15,"concurrent-hashmap-patterns","ConcurrentHashMap Usage Patterns","Amazon, Google","Medium",
         "Design patterns using ConcurrentHashMap: computeIfAbsent, size, iteration safety.",
         "ConcurrentMapPatterns",[("ConcurrentHashMap","Map"),("CacheLoader","computeIfAbsent"),("Counter","Atomic increment"),("StripedLock","Segment sync")],
         "ConcurrentHashMap",None,"full"),
    ],
    "genai": [
        (1,"rag-orchestrator","RAG Orchestrator","OpenAI, Anthropic, Google","Hard",
         "Design in-process RAG orchestrator: retrieve, rerank, assemble context, generate.",
         "RAGOrchestrator",[("RAGOrchestrator","Pipeline"),("Retriever","Fetch chunks"),("Reranker","Score order"),("ContextAssembler","Prompt build"),("Generator","LLM interface")],
         "Retriever","02-genai-llm-hld/questions/Q02-rag-document-qa.md","full"),
        (2,"agent-tool-registry","Agent Tool Registry","Anthropic, OpenAI","Hard",
         "Design tool registry for LLM agents: register, describe, invoke, validate args.",
         "ToolRegistry",[("ToolRegistry","Catalog"),("Tool","Callable"),("ToolSchema","JSON params"),("Agent","Invoker"),("ToolResult","Output")],
         "Tool","02-genai-llm-hld/questions/Q08-multi-agent-workflow.md","full"),
        (3,"prompt-template-engine","Prompt Template Engine","LangChain, OpenAI","Medium",
         "Design prompt templates with variables, conditionals, and partials.",
         "PromptEngine",[("PromptTemplate","String template"),("TemplateContext","Variables"),("PromptRenderer","Fill slots"),("PromptValidator","Schema check")],
         "PromptRenderer","02-genai-llm-hld/questions/Q13-prompt-management.md","skeleton"),
        (4,"conversation-memory-manager","Conversation Memory Manager","Character.AI, OpenAI","Medium",
         "Design sliding-window + summary memory for multi-turn chat context.",
         "MemoryManager",[("Conversation","Session"),("Message","Turn"),("MemoryBuffer","Window"),("SummaryCompressor","Long context"),("TokenCounter","Budget")],
         "MemoryBuffer",None,"full"),
        (5,"token-budget-manager","Token Budget Manager","OpenAI, Anthropic","Medium",
         "Design token budget allocator across system, history, retrieval, response.",
         "TokenBudgetManager",[("TokenBudget","Limits"),("BudgetAllocator","Split tokens"),("TokenCounter","Estimate"),("TruncationStrategy","Trim policy")],
         "TruncationStrategy",None,"skeleton"),
        (6,"llm-provider-abstraction","LLM Provider Abstraction","Anthropic, OpenAI","Medium",
         "Design provider interface swapping OpenAI, Anthropic, local models.",
         "LLMProvider",[("LLMProvider","Interface"),("OpenAIProvider","Impl"),("AnthropicProvider","Impl"),("CompletionRequest","Prompt"),("CompletionResponse","Text")],
         "LLMProvider","02-genai-llm-hld/questions/Q05-llm-api-gateway.md","full"),
        (7,"evaluation-pipeline","Evaluation Pipeline","OpenAI, HuggingFace","Hard",
         "Design LLM eval pipeline: dataset, metrics, judge model, report.",
         "EvalPipeline",[("EvalPipeline","Runner"),("EvalCase","Input/expected"),("Metric","Score"),("JudgeModel","LLM grader"),("EvalReport","Results")],
         "Metric","02-genai-llm-hld/questions/Q14-llm-evaluation-platform.md","skeleton"),
        (8,"guardrail-safety-chain","Guardrail / Safety Filter Chain","Anthropic, OpenAI","Hard",
         "Design chain of input/output guardrails: PII, toxicity, policy filters.",
         "GuardrailChain",[("Guardrail","Filter interface"),("PIIGuardrail","Redact"),("ToxicityGuardrail","Block"),("GuardrailChain","Pipeline"),("SafetyResult","Pass/fail")],
         "Guardrail","02-genai-llm-hld/questions/Q15-content-moderation-llm.md","full"),
        (9,"streaming-response-aggregator","Streaming Response Aggregator","OpenAI, Google","Medium",
         "Design aggregator collecting streamed LLM tokens into final response + callbacks.",
         "StreamAggregator",[("StreamAggregator","Collector"),("TokenChunk","Delta"),("StreamCallback","Listener"),("CompletionBuffer","Assembly")],
         "StreamCallback",None,"skeleton"),
        (10,"multi-agent-coordinator","Multi-Agent Coordinator","OpenAI, Microsoft","Hard",
         "Design coordinator routing tasks between specialist agents with shared state.",
         "AgentCoordinator",[("Coordinator","Orchestrator"),("Agent","Specialist"),("Task","Work unit"),("SharedState","Blackboard"),("RoutingPolicy","Agent pick")],
         "RoutingPolicy","02-genai-llm-hld/questions/Q08-multi-agent-workflow.md","skeleton"),
    ],
}


def _clarify_for(slug: str, title: str, iface: str) -> list[tuple[str, str]]:
    base = [
        (f"What is the MVP scope for {title}?", "Core entities + 2 primary flows; extensions deferred"),
        (f"Persistence layer?", "In-memory; Repository interface if interviewer asks"),
        (f"Concurrency requirements?", "Thread-safe shared state if multi-user/access specified"),
        (f"Primary variation point?", f"Inject {iface} interface — Strategy/State/Adapter as appropriate"),
        (f"Error handling style?", "Domain exceptions with clear messages; fail fast on invalid input"),
        (f"Testing approach?", f"Unit test {iface} implementations in isolation with mocks"),
    ]
    extras = {
        "chess": [("Draw by repetition?", "Extension — threefold repetition counter"),
                  ("AI opponent?", "Out of scope — two human players MVP")],
        "lru-cache": [("Thread-safe?", "Single-threaded MVP; concurrent variant is separate Q"),
                      ("Max capacity?", "Fixed at construction; dynamic resize extension")],
        "rag-orchestrator": [("Vector DB?", "HLD concern — stub Retriever interface in LLD"),
                              ("Streaming response?", "Extension via StreamAggregator")],
        "dining-philosophers": [("Deadlock prevention?", "Ordered fork acquisition or waiter arbitrator"),
                                ("Number of philosophers?", "Configurable N at table")],
        "thread-safe-singleton": [("Lazy or eager init?", "Lazy with double-checked locking"),
                                    ("Serialization safety?", "Enum singleton or readResolve")],
    }
    extra = extras.get(slug, [
        (f"Scale expectations?", "Single JVM object model; HLD for distributed scale"),
        (f"Authentication?", "Stub or extension unless core to problem"),
    ])
    return base + extra[:2]


def _functional_for(slug: str, service: str, verbs: str) -> list[str]:
    return [
        f"Primary flow orchestrated by {service}",
        f"Validate inputs and enforce domain rules before state mutation",
        f"Expose core API: {verbs}",
        "Return typed results or throw domain exceptions on failure",
    ]


def _nfr_for(track: str, iface: str) -> list[str]:
    nfr = [
        "Clear separation of concerns (SOLID)",
        f"Open-Closed via {iface} interface at variation points",
        "Constructor injection for testability",
    ]
    if track == "concurrency":
        nfr.extend(["Correctness under concurrent access — no data races",
                     "Avoid deadlock — consistent lock ordering where multiple locks"])
    elif track == "genai":
        nfr.extend(["Swappable pipeline stages behind interfaces",
                     "Explicit boundary to HLD for vector DB, model serving, queues"])
    else:
        nfr.append("Thread-safe if concurrent access is in clarifying assumptions")
    return nfr


def _happy_fail(service: str, slug: str) -> tuple[str, str]:
    happy = _seq(
        "participant U as User", f"participant S as {service}", "participant D as Domain",
        f"U->>S: primaryAction()", "S->>D: validate / process", "D-->>S: success", "S-->>U: result",
    )
    fail = _seq(
        "participant U as User", f"participant S as {service}",
        f"U->>S: primaryAction(invalid)", "S-->>U: DomainException",
    )
    special = {
        "lru-cache": (
            _seq("participant C as Client", "participant L as LRUCache", "C->>L: put(k,v)", "C->>L: get(k)", "L-->>C: v"),
            _seq("participant C as Client", "participant L as LRUCache", "C->>L: put(k4,v4) at capacity", "L->>L: evict LRU", "C->>L: get(k1)", "L-->>C: null"),
        ),
        "rag-orchestrator": (
            _seq("participant U as User", "participant R as RAGOrchestrator", "participant Ret as Retriever", "participant G as Generator",
                 "U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: chunks", "R->>G: generate(context)", "G-->>R: answer", "R-->>U: answer"),
            _seq("participant U as User", "participant R as RAGOrchestrator", "participant Ret as Retriever",
                 "U->>R: answer(query)", "R->>Ret: retrieve(query)", "Ret-->>R: empty", "R-->>U: NoContextException"),
        ),
    }
    return special.get(slug, (happy, fail))


def _seq(*lines: str) -> str:
    return "\n".join(lines)


def _script_paras(title: str, service: str, entities: list, iface: str, track: str) -> list[str]:
    names = ", ".join(f"`{e[0]}`" for e in entities[:5])
    paras = [
        f"I'll start by clarifying scope for {title} — in-memory, single JVM, MVP flows.",
        f"Entities: {names}. I'll group into domain model plus {service} facade.",
        f"The variation point is {iface} — swap behavior without changing orchestration.",
        f"Core API on {service} with validation first, then delegate to domain objects.",
        "For extensibility, new behavior equals new interface implementation — Open-Closed.",
        "Tradeoff: enum for simple states; State pattern only when transitions have side effects.",
        "I'll sketch the service method in Java with constructor injection for testability.",
    ]
    if track == "concurrency":
        paras.append("Key concurrency: identify shared mutable state, choose lock granularity, avoid deadlock.")
    elif track == "genai":
        paras.append("LLD covers pipeline object model; vector DB and model serving are HLD concerns.")
    else:
        paras.append("If scale-out needed, pivot to HLD — cache, queue, DB — object model stays.")
    return paras


def _followups(slug: str, iface: str) -> list[str]:
    return [
        f"How would you unit test {iface} in isolation?",
        "How would you add persistence behind a Repository?",
        "How would you make this thread-safe?",
        "How does this map to a distributed HLD?",
    ]


def make_spec(track: str, meta_row) -> dict:
    from _slug_details import enrich_generic, OVERRIDES  # noqa: WPS433

    num, slug, title, companies, diff, problem, service, entities, iface, hld, impl = meta_row
    track_key = track if track != "classic_rest" else "classic"
    ent_names = [e[0] for e in entities]
    nouns = ", ".join(f"`{n}`" for n in ent_names)

    patterns = [(iface, f"Primary pattern for {title}")]
    if track == "patterns":
        pname = title.split("—")[0].strip() if "—" in title else iface
        patterns = [(pname, f"Core pattern demonstration in {slug}")]

    solid = [("S", f"{service} orchestrates; entities hold state"),
             ("O", f"New behavior via new {iface} impl"),
             ("D", f"Depend on {iface} interface")]

    base = {
        "track": track_key,
        "num": num, "slug": slug, "title": title, "companies": companies,
        "difficulty": diff, "problem": problem,
        "non_functional": _nfr_for(track_key, iface),
        "entities": entities, "nouns": nouns,
        "service": OVERRIDES.get(slug, {}).get("service", service),
        "patterns": OVERRIDES.get(slug, {}).get("patterns", patterns),
        "solid": solid,
        "extensibility": OVERRIDES.get(slug, {}).get("extensibility", [
            f"New {iface} implementation plugs in without editing {service}.",
            f"Add features via composition — new entity types implementing same interfaces.",
        ]),
        "tradeoffs": OVERRIDES.get(slug, {}).get("tradeoffs", [
            ("Variation", "if/else", iface, f"{iface} — 2+ behaviors"),
            ("State", "enum", "State pattern", "enum for simple lifecycles"),
            ("Storage", "in-memory", "Repository", "in-memory MVP"),
            ("API return", "primitive", "domain object", "domain object — type safety"),
        ]),
        "concurrency": OVERRIDES.get(slug, {}).get("concurrency", [
            "Synchronize on shared mutable entities or use concurrent collections",
            "Invalid input → domain exception",
            "Duplicate operations → idempotent where applicable",
            "Null references → Optional or explicit validation",
        ]),
        "followups": OVERRIDES.get(slug, {}).get("followups", _followups(slug, iface)),
        "hld": OVERRIDES.get(slug, {}).get("hld", hld),
        "impl": impl, "skip": False,
    }

    enriched = enrich_generic(slug, title, service, entities, iface, track_key, problem)
    base.update({k: enriched[k] for k in (
        "clarify", "functional", "methods", "verbs", "happy_seq", "fail_seq", "script", "nouns"
    ) if k in enriched})
    if "service" in OVERRIDES.get(slug, {}):
        base["service"] = OVERRIDES[slug]["service"]

    from _content_builder import enrich_spec  # noqa: WPS433
    ov_keys = set(OVERRIDES.get(slug, {}).keys())
    base = enrich_spec(base, override_keys=ov_keys)
    # Hand overrides on top (preserve OVERRIDES depth for key slugs)
    for k, v in OVERRIDES.get(slug, {}).items():
        base[k] = v
    # Rebuild mermaid if override didn't supply custom diagram
    if "mermaid_class" not in ov_keys and "ascii" not in ov_keys:
        from _content_builder import build_mermaid_class  # noqa: WPS433
        base["mermaid_class"] = build_mermaid_class(
            base["service"], base["methods"], base["entities"], ""
        )
    return base


def render_batch(var_name: str, track: str, rows: list) -> str:
    specs = [make_spec(track, r) for r in rows]
    lines = [f"# Auto-generated by gen_all_specs.py — do not edit manually", f"{var_name} = ["]
    for s in specs:
        lines.append("    " + repr(s) + ",")
    lines.append("]")
    return "\n".join(lines) + "\n"


def main():
    mapping = {
        "_specs_classic_rest.py": ("CLASSIC_REST", "classic_rest", META["classic_rest"]),
        "_specs_patterns.py": ("PATTERNS_SPECS", "patterns", META["patterns"]),
        "_specs_concurrency.py": ("CONCURRENCY_SPECS", "concurrency", META["concurrency"]),
        "_specs_genai.py": ("GENAI_SPECS", "genai", META["genai"]),
    }
    for fname, (var, track, rows) in mapping.items():
        (ROOT / fname).write_text(render_batch(var, track, rows), encoding="utf-8")
        print(f"Wrote {fname} ({len(rows)} specs)")


if __name__ == "__main__":
    main()
