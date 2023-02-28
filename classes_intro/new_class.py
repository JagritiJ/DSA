class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # executed itself when the object is created, just like init
    def __str__(self):
        return f"{self.name}({self.age})"

    def saysHi(self, name, age):
        # without the self keyword -> Sumit 32 says Hi
        print(name+" "+ age + " says Hi") 
        # below statement prints -> a 31 says Hi, these are the values with which I initailized the object
        print(self.name+" "+ self.age + " says Hi")

# p1 = Person("Aryan", "31")
p1 = Person("a", "31")
# if I use the print statement then the __str__ method in the class is also executed
print(p1)

# weird, why this isn't getting called with given ?
p1.saysHi("Sumit", "32")  

# the below way we can change the variables - prints Conor(31)
p1.name ="Conor"

print(p1)

