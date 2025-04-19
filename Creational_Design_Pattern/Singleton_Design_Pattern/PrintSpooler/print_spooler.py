import asyncio

class AsyncPrintSpooler:
    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Use 'await PrintSpooler.get_instance()' instead")
    
    @classmethod
    async def get_instance(cls):
        """Class methos to create instance handling the concurrency issue and race conditions initially."""
        if cls._instance is None:
            async with cls._lock:
                """
                Calls cls._lock.__aenter__() → Acquires the lock.
                Runs the block of code inside async with.
                Calls cls._lock.__aexit__() → Releases the lock.
                """
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.job_queue = []
        return cls._instance
    
    async def add_print_job(self, job: str):
        """Add job to the queue.
        
        param job: A job.
        return type: str
        """
        if job:
            self.job_queue.append(job)

    async def process_next_job(self)->str:
        """Return the next job from the queue, or notify if empty."""
        if not self.job_queue:
            return "No jobs in the queue."
        return self.job_queue.pop(0)


async def test_print_spooler():
    ps1 = await AsyncPrintSpooler.get_instance()
    ps2 = await AsyncPrintSpooler.get_instance()
    print("Id of ps1", id(ps1))
    print("Id of ps2", id(ps2))
    print("Id of ps1 and ps2 are same:", id(ps1) == id(ps2))
    print("Id of ps1 and ps2 are same:", ps1 is ps2)

    await ps1.add_print_job("Hi")
    await ps1.add_print_job("How you doing today?")
    await ps1.add_print_job("I am doing wonderful.")
    await ps1.add_print_job("How about you?")

    print(await ps1.process_next_job())


asyncio.run(test_print_spooler())



# OUTPUT
"""
Id of ps1 4381600656
Id of ps2 4381600656
Id of ps1 and ps2 are same: True
Id of ps1 and ps2 are same: True
Hi
"""