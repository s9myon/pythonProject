from Equations import Equations
from db.DB import DB

print(Equations.linear(1, 9), Equations.square(1, -4, 4), Equations.cube(1, -4, 4, 0))

db = DB()

users = db.getAllUsers()

print(users)
