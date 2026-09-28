class Burger:
    def __init__(self, sauce:str, has_cheese:bool):
        self.sauce = sauce
        self.has_cheese = has_cheese
    def describe(self):
        return f"Burger with {self.sauce} sauce and {'cheese' if self.has_cheese else 'no cheese'}."
    