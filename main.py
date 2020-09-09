from Equations import Equations
from people.Human import Human
from people.Woman import Woman

print(Equations.linear(4, 5), Equations.square(1, -4, 4), Equations.cube(3, -0.75, -3, 0.75))

man = Human('Богдан')
woman = Woman('Наталья')
man.work()
children = Woman.sex(man, woman)
