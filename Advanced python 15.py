
import gc

class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "object destroyed")

gc.disable()

a = Demo("Object A")
b = Demo("Object B")

a.ref = b
b.ref = a

del a
del b

print("Garbage collected:", gc.collect())

gc.enable()

print("Automatic garbage collection enabled.")
