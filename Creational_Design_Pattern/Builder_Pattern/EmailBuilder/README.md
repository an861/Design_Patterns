USE:
1. Asynchronous Immutable Builder class [NO THREADING]
    Immutable builder creates a new instance for each operation instead of modifying the existing one.
    1. Uses immutable approach (return a new object instead of modifying self).
    2. Uses 'asyncio' for async execution.
    3. Best for high-performance applications. 
    4. Avoids thread safety issues completely
    5. Faster Performance, async workloads
    6. Highly Scalable
    7. More Complex
    8. Encouraged (pure functions)
    8. Scenarios
        1. Async FastAPI app (notification service)
        2. High-volume email sending


sync -> thread + mutable
async -> no thread(new instance create each method) + immutable(can't modify the existing instance, need to create new instance each time)


Why is This the Best Approach?
    Feature	            Sync Mutable Builder	Async Immutable Builder
    Performance	        ✅ Faster	            🚫 Slower (creates new instances)
    Memory Usage	    ✅ Lower	                🚫 Higher (creates new objects)
    Thread Safety	    ✅ Uses threading.Lock	✅ Inherently safe (no shared state)
    Async Compatibility	🚫 Not ideal	         ✅ Fully async-friendly
    Best For	        Small-scale apps	     High-performance FastAPI services


🔹 When to Use Which?
Scenario	                        Use Sync Builder?	Use Async Builder?
Single-threaded scripts	            ✅ Yes	                🚫 No
Multi-threaded email processing	    ✅ Yes (thread locks)	🚫 No
Async FastAPI notification service	🚫 No	                 ✅ Yes
High-volume email sending (RabbitMQ, Celery)	🚫 No	    ✅ Yes
Performance-sensitive apps	        ✅ Yes	                🚫 No


🚀 Final Takeaway
✔ If your email service is synchronous (Django, Flask, basic script) → use Sync Mutable Builder (efficient, fast).
✔ If your email service is async (FastAPI, Celery, distributed email queue) → use Async Immutable Builder (scalable, safe).
✔ Hybrid Approach (sync for scripts, async for APIs) is the most flexible.