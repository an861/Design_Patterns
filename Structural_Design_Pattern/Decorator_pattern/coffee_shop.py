"""
Coffee Shop - Decorator Pattern Problem Statement

Problem Statement:
You are tasked with developing a flexible and extensible coffee ordering system for a local coffee shop.
The system must support various base beverages (like Espresso, House Blend, Dark Roast, Decaf) and allow customers
to customize their drinks by adding multiple condiments (like milk, soy, mocha, whipped cream, etc.).
Each condiment should add to the cost and optionally change the description of the final beverage.
Customers can mix and match any number of condiments.

Requirements:
You must represent beverages (like Espresso, House Blend, etc.) as base objects.
You must allow condiments (like Mocha, Soy, etc.) to be added dynamically at runtime.
The total cost of a drink should reflect the base drink plus any condiments added.
You should be able to retrieve a full description of the beverage with its condiments (e.g., “Dark Roast, Mocha, Whip”).

Provide the beverage description and cost.
"""


from abc import ABC, abstractmethod
from typing import final


# single inheritance to implemnet interface/ABC
class Coffee(ABC):
    """Abstract base class for Coffee Entity."""

    @abstractmethod
    def get_cost(self)->float:
        """Provide the cost of the coffee."""
        pass
    
    @abstractmethod
    def get_description(self)->str:
        """Provide the description of the coffee."""
        pass


# composition
class CoffeeBase(Coffee):
    pass

# composition
class CoffeeCondiment(Coffee):

    def __init__(self, coffee: Coffee):
        self._coffee = coffee

@final
class EspressoBase(CoffeeBase):
    
    def get_cost(self):
        return 100
    
    def get_description(self):
        return "Espresso"
    
@final
class HouseBlendBase(CoffeeBase):
    
    def get_cost(self):
        return 100
    
    def get_description(self):
        return "House Blend"
    
@final
class DarkRoastBase(CoffeeBase):
    
    def get_cost(self):
        return 100
    
    def get_description(self):
        return "Dark Roast"
    
@final
class DecafBase(CoffeeBase):
    
    def get_cost(self):
        return 100
    
    def get_description(self):
        return "Decaf"
    

class MilkCondiment(CoffeeCondiment):

    def get_cost(self):
        return self._coffee.get_cost() + 30
    
    def get_description(self):
        return self._coffee.get_description() + " ,With Milk"


class Soy(CoffeeCondiment):

    def get_cost(self):
        return self._coffee.get_cost() + 50
    
    def get_description(self):
        return self._coffee.get_description() + " ,With Soy"
    
class Mocha(CoffeeCondiment):

    def get_cost(self):
        return self._coffee.get_cost() + 70
    
    def get_description(self):
        return self._coffee.get_description() + " ,With Mocha"
    
class WhippedCream(CoffeeCondiment):

    def get_cost(self):
        return self._coffee.get_cost() + 20
    
    def get_description(self):
        return self._coffee.get_description() + " ,With WhippedCream"
    



# Input

# w = MilkCondiment(Mocha(WhippedCream(EspressoBase())))
# print("Cost of Coffee: {}".format(w.get_cost()))
# print("Description: {}".format(w.get_description()))


# Output
"""
Cost of Coffee: 220
Description: Espresso ,With WhippedCream ,With Mocha ,With Milk
"""


# INPUT
# w = WhippedCream(Mocha(DarkRoastBase()))
# print("Cost of Coffee: {}".format(w.get_cost()))
# print("Description: {}".format(w.get_description()))


# Output
"""
Cost of Coffee: 190
Description: Dark Roast ,With Mocha ,With WhippedCream
"""




# CLI for the coffee shop

def choose_base_coffee():
    print("Choose your base coffee:")
    coffee_bases: dict = {
        "1": EspressoBase,
        "2": HouseBlendBase,
        "3": DarkRoastBase,
        "4": DecafBase,
    }
    for k, v in coffee_bases.items():
        print(f"{k}.{v().__class__.__name__}")
    base = input("\n Please select any option between 1 to 4: \n").strip()
    return coffee_bases.get(base, EspressoBase)()

def choose_condiments(coffee):
    print("\n Choose your coffee condiments else press Enter to skip:")
    condiment_options: dict = {
        "1": MilkCondiment,
        "2": Soy,
        "3": Mocha,
        "4": WhippedCream,
    }
    for k, v in condiment_options.items():
        print(f"{k}.{v.__name__}")
    condiments = input("\n Enter your choices (e.g., 1,3): ").strip().split(",")
    for c in condiments:
        cond = condiment_options.get(c.strip())
        if cond:
            coffee = cond(coffee)
    return coffee



def main():
    print("Welcome to your local coffee shop. \n")
    base_coffee = choose_base_coffee()
    final_coffee = choose_condiments(base_coffee)
    print("Your coffee order summary is here: \n")
    print("Description:", final_coffee.get_description())
    print("Price: ₹{}".format(final_coffee.get_cost()))



if __name__ == "__main__":
    main()


# OUTPUT 1 with single condiment selection
"""
Welcome to your local coffee shop. 

Choose your base coffee:
1.EspressoBase
2.HouseBlendBase
3.DarkRoastBase
4.DecafBase

 Please select any option between 1 to 4: 
2

 Choose your coffee condiments else press Enter to skip:
1.MilkCondiment
2.Soy
3.Mocha
4.WhippedCream

 Enter your choices (e.g., 1,3): 
['']
Your coffee order summary is here: 

Description: House Blend
Price: 100

"""


# OUTPUT 2 with multiple condiment selection
"""
Welcome to your local coffee shop. 

Choose your base coffee:
1.EspressoBase
2.HouseBlendBase
3.DarkRoastBase
4.DecafBase

 Please select any option between 1 to 4: 
1

 Choose your coffee condiments else press Enter to skip:
1.MilkCondiment
2.Soy
3.Mocha
4.WhippedCream

 Enter your choices (e.g., 1,3): 2, 4
Your coffee order summary is here: 

Description: Espresso ,With Soy ,With WhippedCream
Price: ₹170
"""
