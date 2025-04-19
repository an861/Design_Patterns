# SYNCHRONOUS
class Car:
    """Core class with multiple attributes for object creation."""
    def __init__(self, model: str, engine: str, color: str)->None:
        """Parameterized constructor."""
        self.model= model
        self.engine = engine
        self.color = color
    
    def __str__(self)->str:
        return f"Car(Model: {self.model}, Engine: {self.engine}, Color: {self.color})"
    
class CarBuilder:
    """Builder class for configuration of the Car class attributes and build Car objects."""
    def __init__(self)->None:
        """Default constructor."""
        self.model = None
        self.engine = None
        self.color = None

    def set_model(self, model: str):
        self.model = model
        return self # method chaining (fluent interface)
    
    def set_engine(self, engine: str):
        self.engine= engine
        return self
    
    def set_color(self, color: str):
        self.color = color
        return self
    
    def build(self):
        return Car(self.model, self.engine, self.color)
    

carbuilder_1 = CarBuilder()
carbuilder_1.set_model("Volkswagon").set_engine("Electric").set_color("Black").build()
print("Car builder 1:", carbuilder_1.build())

carbuilder_2 = CarBuilder()
carbuilder_2.set_model("Tesla Model S").set_engine("Electric").set_color("Red").build()
print("Car builder 2:",carbuilder_2.build())


# IDEAL APPROACH
carbuilder_3 = (CarBuilder()
                .set_model("Model")
                .set_engine("Engine")
                .set_color("Color")
                .build())
print("Car builder 3:", carbuilder_3)
                


#  CASE 1
# print(carbuilder_1.build())

# OUTPUT
# Car(Model: Volkswagon, Engine: Electric, Color: Black)




# CASE 2
# print("Car builder 1:", carbuilder_1)
# print("Car builder 2:",carbuilder_2)

# OUTPUT
# Car builder 1: <__main__.CarBuilder object at 0x10312b010>
# Car builder 2: <__main__.CarBuilder object at 0x103008310>




# CASE 3
# print("Car builder 1:", carbuilder_1.build())
# print("Car builder 2:",carbuilder_2.build())

# OUTPUT
# Car builder 1: Car(Model: Volkswagon, Engine: Electric, Color: Black)
# Car builder 2: Car(Model: Tesla Model S, Engine: Electric, Color: Red)



# CASE 4
# print("Car builder 1:", carbuilder_1.build())
# print("Car builder 2:", carbuilder_2.build())
# print("Car builder 3:", carbuilder_3)

# OUTPUT
# Car builder 1: Car(Model: Volkswagon, Engine: Electric, Color: Black)
# Car builder 2: Car(Model: Tesla Model S, Engine: Electric, Color: Red)
# Car builder 3: Car(Model: Model, Engine: Engine, Color: Color)


# IMMUTATBILITY(DONT RETURN SELF)

class ImmutableCarBuilder:
    def __init__(self, model=None, engine=None, color=None):
        self.model = model
        self.engine = engine
        self.color = color

    def set_model(self, model):
        return ImmutableCarBuilder(model, self.engine, self.color)  # Returns new object

    def set_engine(self, engine):
        return ImmutableCarBuilder(self.model, engine, self.color)

    def set_color(self, color):
        return ImmutableCarBuilder(self.model, self.engine, color)