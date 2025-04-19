"""Async Double-Checked Locking Singleton"""
import asyncio
from pathlib import Path

class ConfigurationManager:
    """Singleton class for connection manager using async double-checked locking."""

    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Use 'ConfigurationManager.get_instance()' instead.")
    
    @classmethod
    async def get_instance(cls):
        """Returns the singleton instance of ConfigurationManager."""
        if cls._instance is None:
            async with cls._lock:
                """
                Calls cls._lock.__aenter__() → Acquires the lock.
                Runs the block of code inside async with.
                Calls cls._lock.__aexit__() → Releases the lock.
                """
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.filepath = Path(ConfigurationManager.credentials.yaml) # type: ignore
        return cls._instance
    
    async def load_configuration_from_file(self)->dict:
        """Load configurations from a file."""


    

async def test_connection_manager():
    cfmgr_1 = await ConfigurationManager.get_instance()
    cfmgr_2 = await ConfigurationManager.get_instance()
    print("Id of cfmgr_1:",id(cfmgr_1))
    print("Id of cfmgr_2:",id(cfmgr_2))
    print("Same or not :", cfmgr_1 is cfmgr_2)

asyncio.run(test_connection_manager())
