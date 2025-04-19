# ASYNCHRONOUS
import asyncio

class AsyncCar:
    def __init__(self, model: str, engine: str, color: str)->None:
        self.model = model
        self.engine = engine
        self.color = color

    def __str__(self)->str:
        return f"AsyncCar(Model: {self.model}, Engine: {self.engine}, Color: {self.color})"

class AsyncCarBuilder:
    def __init__(self):
        self.model = None
        self.engine = None
        self.color = None

    async def set_model(self, model: str):
        self.model = model
        return self
    
    async def set_engine(self, engine: str):
        self.engine = engine
        return self
    
    async def set_color(self, color: str):
        self.color = color
        return self
    
    async def build(self):
        return AsyncCar(self.model, self.engine, self.color)
    
async def main():
    builder = AsyncCarBuilder()
    builder = await builder.set_model("Tesla Model X")
    builder = await builder.set_engine("Electric")
    builder = await builder.set_color("Blue")
    
    car = await builder.build()
    print(car)

asyncio.run(main())


# OUTPUT
# AsyncCar(Model: Tesla Model X, Engine: Electric, Color: Blue)
