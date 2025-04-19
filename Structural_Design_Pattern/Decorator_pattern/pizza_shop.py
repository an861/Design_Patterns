"""
Pizza Shop — Problem Statement

Objective:
    Design and implement a modular and extensible Pizza Ordering System that allows users to:
        Choose a base pizza
        Add one or more toppings (in any order)
        Calculate the final price
        Get a complete description of the pizza (base + toppings)

Key Requirements:
    Base Pizzas (each with its own base cost and name):
        Margherita
        Farmhouse
        Peppy Paneer
        Veg Extravaganza
    Toppings (can be added on top of any pizza):
        Extra Cheese
        Olives
        Jalapenos
        Mushrooms
        Pepperoni (non-veg)
        Onion
        Capsicum
    Behavior:
        Users can create any combination of pizza + toppings.
        Cost should update correctly with every topping.
        Description should build up based on choices.
    Extensibility:
        Easily add new base pizzas or toppings without modifying existing logic.

"""
from abc import ABC, abstractmethod
from typing import final

class PizzaOrderingSystem(ABC):

    @abstractmethod
    def get_price(self)->float:
        pass

    @abstractmethod
    def get_description(self)->str:
        pass

class PizzaBase(PizzaOrderingSystem):
    pass

class PizzaToppings(PizzaOrderingSystem):
    def __init__(self, pizza_base: PizzaOrderingSystem):
        self._pizza_base = pizza_base


@final
class Margherita(PizzaBase):

    def get_price(self):
        return 100
    
    def get_description(self):
        return "Margherita base"
    
    def get_name(self):
        return "Margherita"
    
@final
class Farmhouse(PizzaBase):

    def get_price(self):
        return 100
    
    def get_description(self):
        return "Farmhouse base"
    
    def get_name(self):
        return "Farmhouse"
    
@final
class PeppyPaneer(PizzaBase):

    def get_price(self):
        return 100
    
    def get_description(self):
        return "PeppyPaneer base"
    
    def get_name(self):
        return "PeppyPaneer"
    
@final
class VegExtravaganza(PizzaBase):

    def get_price(self):
        return 100
    
    def get_description(self):
        return "VegExtravaganza base"
    
    def get_name(self):
        return "VegExtravaganza"
    

class ExtraCheese(PizzaToppings):

    def get_price(self):
        return self._pizza_base.get_price() + 30
    
    def get_description(self):
        return self._pizza_base.get_description() + ", with extra cheese"
    
class Olives(PizzaToppings):

    def get_price(self):
        return self._pizza_base.get_price() + 40
    
    def get_description(self):
        return self._pizza_base.get_description() + ", with olives"
    
class Jalapenos(PizzaToppings):

    def get_price(self):
        return self._pizza_base.get_price() + 50
    
    def get_description(self):
        return self._pizza_base.get_description() + ", with Jalapenos"
    
class Mushrooms(PizzaToppings):

    def get_price(self):
        return self._pizza_base.get_price() + 70
    
    def get_description(self):
        return self._pizza_base.get_description() + ", with Mushrooms"
    

# CLI for the pizza ordering system


def choose_pizza_base():
    print("Kindly select your prefered base for the pizza.")
    base_options = {
        "1": Margherita,
        "2": Farmhouse,
        "3": PeppyPaneer,
        "4": VegExtravaganza,
    }
    for k, v in base_options.items():
        print(f"{k}.{v().__class__.__name__}")
    base = input("\n Enter any number between 1 to 4: \n").strip()
    return base_options.get(base, Margherita)()

def choose_toppings(pizza_base: object):
    print("Please choose your preferred toppings.")
    toppings_options= {
        "1": ExtraCheese,
        "2": Olives,
        "3": Jalapenos,
        "4": Mushrooms,
    }
    for k , v in toppings_options.items():
        print(f"{k}.{v.__name__}")
    toppings = input("\n Choose the toppings of your choice(eg: 1,3): \n").strip().split(",")
    final_pizza = pizza_base
    for top in toppings:
        tp = toppings_options.get(top.strip())
        if tp:
            final_pizza = tp(final_pizza)
    return final_pizza




def main():
    print("Welcome to Ankita's Pizza Shop.\n")
    base = choose_pizza_base()
    final_pizza = choose_toppings(base)
    print("Here's the overall summary: \n")
    print("Description: {}".format(final_pizza.get_description()))
    print("Final Price: {}".format(final_pizza.get_price()))

if __name__ == "__main__":
    main()


# OUTPUT with multiple toppings
"""
Welcome to Ankita's Pizza Shop.

Kindly select your prefered base for the pizza.
1.Margherita
2.Farmhouse
3.PeppyPaneer
4.VegExtravaganza

 Enter any number between 1 to 4: 
1
Please choose your preferred toppings.
1.ExtraCheese
2.Olives
3.Jalapenos
4.Mushrooms

 Choose the toppings of your choice(eg: 1,3): 
2, 4
Here's the overall summary: 

Description: Margherita base, with olives, with Mushrooms
Final Price: 210
"""