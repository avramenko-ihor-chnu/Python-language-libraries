def outer_method(self):
    print('I am a method of object', self)
class MyClass:
    method = outer_method
obj = MyClass(); obj.method()
print(type(obj.method()))
#print(type(outer_method()))
