# print('hello, world')
# a = [1,2,3,4,5]
# str(a)
# b = {'name': 'zm', 'age': 16, 'class': 'class1'}
# bb = str(b)
# print(len(bb))
# print(f"{bb}", end=" @@@ ")
# a = f'{bb} is test'
# print(a)
#
# site = {"name": "w3cschool教程", "url": "www.w3cschool.cn"}
#
# print("网站名：{name}, 地址 {url}".format(**site))
#
#
# status = 500
# match status:
#     case 400:
#         print(400)
#     case 500:
#         print(500)
#     case 600:
#         print(600)
#     case _:
#         print("_")
#
# # edibles = ["ham", "spam","eggs","nuts"]
# edibles = []
# for food in edibles:
#     if food == "spam":
#         print("No more spam please!")
#         break
#     print("Great, delicious " + food)
# else:
#     print("I am so glad: No spam!")
# print("Finally, I finished stuffing myself")
#
#
# print(type(list(range(5))))
#
# a = 0
# while True:
#     a += 1
#     print(a)
#     pass
#
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)
# print(str(hello))
# raise NameError('HiThere')

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
finally:
    print("finally")
else:
    print("else")