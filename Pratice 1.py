# instance
# Static,Global,Class
# local

# class Naveen:
#     def __init__(self):
#         self.a=10
#         self.b="ram"
#     def func1(self):
#         print(self.b)
#
#     def func2(self):
#         print(self.a)
#
# class Anil(Naveen):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def func1(self):
#         print("Method Overriding")
#
# # obj = Anil()
# # obj.func1()
#
# obj=Naveen()
# obj.func1()
# obj.func2()

# class Naveen:
#     def __init__(self,a1,b1):
#         self.a=a1
#         self.b=b1
#         print(self.a)
#         print(self.b)
#     def func1(self):
#         print(self.b)
#
#     def func2(self):
#         print(self.a)
#
# obj=Naveen(20,30)

#INHERITANCE
#Single inheritance

# class Parent:
#     def __init__(self):
#         self.a="anil"
#         self.b="vamsi"
# class Child(Parent):
#     pass
#
# obj=Child()
# print(obj.a,obj.b)

# multilevel
# class grand:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
# class Parent(grand):
#     def __init__(self,a,b,c,d):
#         super().__init__(a,b,c)
#         self.d=d
# class Child(Parent):
#     pass
#
# obj=Child(1,2,3,4)
# print(obj.a)
# print(obj.b)
# print(obj.c)
# print(obj.d)

# OOPS topic
# class vamsi:
#     def __init__(self):
#         self.a=10
#         self.b="anil"
#     def __func1(self):
#         print(self.a)
#
#     def __func2(self):
#         print(self.b)
#     def func1(self):
#         self.__func1()
#     def func2(self):
#         self.__func2()
#
#
# obj=vamsi()
# obj.func1()
# obj.func2()

# class navya:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __func1(self):
#         print(self.a)
#
#     def __func2(self):
#         print(self.b)
#
#     # Expose methods to allow calling the private functions
#     def func1(self):
#         self.__func1()
#
#     def func2(self):
#         self.__func2()
#
# obj = navya(2003, 2024)
# obj.func1()
# obj.func2()



