from datetime import datetime


def function_middleware(get_response):
    def middleware(request):
        start = datetime.now()
        print("*** [INFO] func-middleware - Before request processing ***", start)
        response = get_response(request)
        end = datetime.now()
        print("*** [INFO] func-middleware - After request processing ***", end)
        return response
    return middleware


class ClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = datetime.now()
        print("*** [INFO] class-middleware - Before request processing ***",)
        response = self.get_response(request)
        end = datetime.now() - start
        print("*** [INFO] class-middleware - After request processing ***")
        print("time required to execute the request: ", end)
        return response
