class A():
    def method_1(self):
        print("hello world")

class B (A):
    def method_1(self):
        print("Python")    # here the child class modified the method on its own.
