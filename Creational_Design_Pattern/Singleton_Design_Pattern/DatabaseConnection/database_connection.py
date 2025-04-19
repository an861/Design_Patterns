"""Async Double-Checked Locking Singleton"""
import asyncio

class AsyncDatabaseConnection:
    """Singleton class for database connection using async double-checked locking."""

    # class variables
    _instance = None 
    _lock = asyncio.Lock()

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Use 'AsyncDatabaseConnection.get_instance()' instead")
    
    @classmethod
    async def get_instance(cls):
        """Returns the singleton instance of DatabaseConnection."""
        if cls._instance is None: # first check before lock
            async with cls._lock: # Acquire lock
                """
                Calls cls._lock.__aenter__() → Acquires the lock.
                Runs the block of code inside async with.
                Calls cls._lock.__aexit__() → Releases the lock.
                """
                if cls._instance is None:  # second check after lock
                    cls._instance = super().__new__(cls)
        return cls._instance
    

    async def connect(self)->str:
        """Simulate connecting to the database"""
        return "Connected to the database"


    async def execute_query(self, query: str)->str:
        """Simulate executing a query on the database"""
        return ("Executing query: '%s':" %query)

    

async def test_database_connection():
    # singleton test
    db_conn_1 = await AsyncDatabaseConnection.get_instance()
    db_conn_2 = await AsyncDatabaseConnection.get_instance()
    print("Id of db1 :", id(db_conn_1))
    print("Id of db2 :", id(db_conn_2))
    print("DB1 and DB2 are same :", db_conn_1 is db_conn_2)

    # method tests
    print(await db_conn_2.connect())
    print(await db_conn_2.execute_query("Select * from customers;"))


asyncio.run(test_database_connection())



# OUTPUT
"""
Id of db1 : 4302807440
Id of db2 : 4302807440
DB1 and DB2 are same : True
Connected to the database
Executing query 'Select * from customers;':
"""
