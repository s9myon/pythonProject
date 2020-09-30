from random import randint

from application.modules.people.Human import Human


class Woman(Human):

    def __init__(self, name='Masha'):
        super().__init__(name)
        self.hairColor = 'blond'

    def shopping(self, man):
        if isinstance(man, Human):
            if man.money > 0:
                print(self.name + 'say: Дай денег!!!')
            else:
                print(self.name + 'say: Научись зарабатывать!!!')

    @staticmethod
    def sex(father, mother, name='Не выбрали'):
        if isinstance(father, Human) and isinstance(mother, Woman):
            genders = ['Мужчина', 'Женщина']
            gender = genders[randint(0, 1)]
            if gender == 'Мужчина':
                names = ['Алексей', 'Василий', 'Влас', 'Демьян', 'Гордей',
                         'Евгений', 'Кузьма', 'Макар', 'Николай', 'Прохор']
            else:
                names = ['Анна', 'Алина', 'Дарья', 'Екатерина', 'Софья', 'Анастасия',
                         'Елена', 'Елизавета', 'Ирина', 'Мария', 'Лукерья', 'Маргарита']
            name = names[randint(0, len(names) - 1)]
            print('Имя ребёнка: ' + name)
            print('Пол ребёнка: ' + gender)
            return Human(name)
        else:
            print('Детей не будет!!!')
