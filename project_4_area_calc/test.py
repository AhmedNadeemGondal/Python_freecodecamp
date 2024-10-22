class Parent:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr

    def parent_method(self):
        print("This is a method of the Parent class.")

class Subclass(Parent):
    def __init__(self, parent_attr, subclass_attr):
        super().__init__(parent_attr)
        self.subclass_attr = subclass_attr

    def subclass_method(self):
        print("This is a method of the Subclass.")

p = Parent("parent_attr_value")
s = Subclass("parent_attr_value", "subclass_attr_value")

print(s.parent_attr)  # outputs "parent_attr_value"
print(s.subclass_attr)  # outputs "subclass_attr_value"
s.parent_method()  # outputs "This is a method of the Parent class."
s.subclass_method()  # outputs "This is a method of the Subclass."
