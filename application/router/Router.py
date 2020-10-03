class Router:
    def __init__(self, app, web, mediator):
        self.web = web
        routes = [
            ('GET', '/api/test', self.testHandler),
            ('GET', '/api/sqr/{value}', self.sqrHandler),
            ('*', '/', self.staticHandler)
        ]
        # прописать доступность статики из папки js
        app.router.add_static('/js/', path=str('./public/js/'))
        # прописать роуты
        for route in routes:
            app.router.add_route(route[0], route[1], route[2])
        print('Я тут!!!')

    def testHandler(self, request):
        return self.web.json_response(dict(result='ROMA!!!!!'))

    def sqrHandler(self, request):
        value = request.match_info.get('value')
        return self.web.json_response(dict(result=float(value) ** 2))

    def staticHandler(self, request):
        return self.web.FileResponse('./public/index.html')
