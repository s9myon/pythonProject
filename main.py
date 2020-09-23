from Equations import Equations
from db.DB import DB
# from people.Human import Human
# from people.Woman import Woman

print(Equations.linear(1, 9), Equations.square(1, -4, 4), Equations.cube(1, -4, 4, 0))

# man = Human('Богдан')
# man2 = Human('Степан')
# woman = Woman('Наталья')
# woman2 = Woman('Маша')
# man.work()
# children = Woman.sex(woman, woman2)

db = DB()

users = db.getAllUsers()

print(users)
