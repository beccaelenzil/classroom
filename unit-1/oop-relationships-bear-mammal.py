# class Mammal:
#     def __init__(self, name, region):
#         self.name = name
#         self.region = region

#     def make_noise(self):
#         print("AHHHHHHH")

# class Bear(Mammal):
#     def __init__(self, name, region, color):
#         # self.name = name
#         # self.region = region
#         super().__init__(name, region)
#         self.color = color

#     def make_noise(self):
#         #mammal = super() # make an instance of the mammal class using super
#         super().make_noise() # call the mammals instance method `make_noise`
#         print("ROOOOAARRRR")


# bear = Bear("yogi", "PNW", "brown")
# bear.make_noise()


class Money:
    def __init__(self, value, currency_type):
        self.value = value
        self.currency_type = currency_type

    def __lt__(self, other): #<
        if self.value < other.value:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.value} {self.currency_type}"
        
    
dollar = Money(1, "dollar")

print(str(dollar))