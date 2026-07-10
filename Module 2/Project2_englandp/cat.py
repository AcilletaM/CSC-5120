class Cat:
    numberOfCats = 0
    # self is first parameter
    def __init__(self, name, color):
        """Initialize name and color attributes."""
        self.name = name
        self.color = color
        self.temper = "it's a cat so..."
        self._shhh = "it's a secret!"
        Cat.numberOfCats += 1 #  Cat.numberOfCats = Cat.numberOfCats + 1
        # these self.whatever are instance variables
        # an instance variable is a value associated with
        # a particular cat


    def hisses_at(self, other):
        print(f"{self.name} hisses at {other.name}.")


# declaring __str__() method
    def __str__(self) -> str:
        result = f"Cat named {self.name} and has {self.color} fur and {self.temper}"
        return result

    # printable representation (when it is being printed from a list
    def __repr__(self):
        #return self.__str__()
        result = f"I'm in a list!!! Cat named {self.name} and has {self.color} fur and {self.temper}"
        return result



