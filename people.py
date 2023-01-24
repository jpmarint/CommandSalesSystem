

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    

if __name__ == '__main__':
    person1 =  Person('Juan Pa', 23)

    print(f'Age: {person1.age}')

    person1.say_hello()
