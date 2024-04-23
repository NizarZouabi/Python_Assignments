local_val = "magical unicorns"
def square(x):
    return x * x

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

class User:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        return "hello"

print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("the file is being executed because it is imported by another file. the file is called", __name__)