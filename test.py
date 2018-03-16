# s = 'Helloworldllkjjjjj'
# a = slice(5, 10 ,2)
# a = {'x':1, 'Z':3}
# b = {"y":2, "Z":3}
#

# from collections import ChainMap
# c = ChainMap(a, b)
# print(c.keys())
# print(list(c.keys()))
# print(ord('\t'))
# print(format('t', '=>10s'))
# s = '{name}'
# print(s.format(name='d'))
# from datetime import datetime
# print(datetime.today())

# class test():
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __getattr__(self, item):
#         return getattr(self.obj, name)
#
#     def __setattr__(self, instance, value):
#         setattr(self.obj, name, value)
#
# setattr(test, 'age', 10)
# # print(getattr(test, 'age'))
# # print(test.__class__)
# # print(dir(test))
#
# class A:
#     a = 0
# x = A()
# y = A()
# # x.a = 1
#
# class B:
#     b = None
#     def __init__(self):
#         self.b = list()
#         print(self.__class__.__name__)
#
#
#
# # class Parent(object):
# #     def __init__(self, data):
# #         self.data = data
# #         print("create an instance of:", self.__class__.__name__)
# #         print("data attribute is:", self.data)
# #
# #
# # class Child(Parent):
# #     pass
# #
# #
# # # c = Child("init Child")
#
#
#
#
# class Parent(object):
#     __slots__ = ("name", "age")
#     fooValue = "Hi, Parent foo value"
#
#     def foo(self):
#         print("This is foo from Parent")
#
#
#
# class Child(Parent):
#     fooValue = "Hi, Child foo value"
#
#     def foo(self):
#         print("This is foo from Child")
#         # use super to access Parent attribute
#         print(super(Child, self).fooValue)
#         super(Child, self).foo()
#
#
# c = Child()
# c.foo()


# class Student(object):
#     __slots__ = ("name", "age")
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# s = Student("Wilber", 28)
#
# print("%s is %d years old" % (s.name, s.age))
# s.score = 96
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# n = 2
# Xtest = np.linspace(-5, 5, n).reshape(-1, 1)
# # print(Xtest)
#
# def kernel(a, b, param):
#     sqdist = np.sum(a**2, 1).reshape(-1, 1) + np.sum(b**2, 1) - 2*np.dot(a, b.T)
#     return np.exp(-0.5*(1/param)*sqdist)
#
#
# param = 0.1
# K_ss = kernel(Xtest, Xtest, param)
# print(K_ss)
# L = np.linalg.cholesky(K_ss+1e-15*np.eye(n))
# f_prior = np.dot(L, np.random.normal(size=(n,6)))
# plt.plot(Xtest, f_prior)
# # plt.show()
#
#
# Xtrain = np.array([-4, -3, -2, -1, 1]).reshape(5, 1)
# Ytrain = np.sin(Xtrain)
#
# K = kernel(Xtrain, Xtrain, param)
# L = np.linalg.cholesky(K+0.00005*np.eye(len(Xtrain)))
#
# K_s = kernel(Xtrain, Xtest, param)
# Lk = np.linalg.solve(L, K_s)
# # print((Lk))
# mu = np.dot(Lk.T, np.linalg.solve(L, Ytrain)).reshape((n,))
# s2 = np.diag(K_ss) - np.sum(Lk**2, axis=0)
#
# stdv = np.sqrt(s2)
# L = np.linalg.cholesky(K_ss + 1e-6*np.eye(n)-np.dot(Lk.T, Lk))
# f_post = mu.reshape(-1, 1) + np.dot(L, np.random.normal(size=(n, 3)))
#
# plt.plot(Xtrain, Ytrain, 'bs', ms=8)
# plt.plot(Xtest, f_post)
# plt.gca().fill_between(Xtest.flat, mu-2*stdv, mu+2*stdv, color='#dddddd')
# # plt.show()


class FatherA:
    def __init__(self):
        print('init action in father class A')


class FatherB(FatherA):
    def __init__(self):
        print('init action in father class B')
        super().__init__()


class SubClassC(FatherB):
    def __init__(self):
        print('init action in subclass C')
        super(SubClassC, SubClassC).__init__(self)
print(type(FatherA))
c =SubClassC()



