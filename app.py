from aiohttp import web
from application.modules.db.DB import DB
from application.modules.mediator.Mediator import Mediator
from application.router.Router import Router
from settings import SETTINGS

# user
# chat
# audio ?
# pirates
db = DB(SETTINGS['DB'])
print(Mediator)
mediator = Mediator(SETTINGS['MEDIATOR']['EVENTS'])

app = web.Application()
Router(app, web, mediator)

web.run_app(app)
# ДЗ
# 1. В медиатор необходимо добавить триггеры
# 2. Надо написать модуль user. Реализовать логин, логоут, регистрацию
# 3. Создать таблицу с users
# 4. Создать api routes с логином, логаутом, регистрацией
# 5. На клиенте реализовать логин, логаут, регистрацию
# 6. Написать тесты на все методы
# 7. Продумать структуру данных для пиратов, описать сущности
