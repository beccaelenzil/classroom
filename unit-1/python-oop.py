
class ExampleClass:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def example_method():
        print("I'm inside the static method, example_method!")
        print(f"I'm accessing an instance variable, {self.name}")

example_instance = ExampleClass("Hello, World!")

example_instance.example_method()