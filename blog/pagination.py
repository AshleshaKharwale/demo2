from rest_framework.pagination import (
    PageNumberPagination, CursorPagination, LimitOffsetPagination
)


class MyNumberPagination(PageNumberPagination):
    page_size = 2


class AuthorCursorPagination(CursorPagination):
    page_size = 3


# have to provide limit and offset values as path params
class BlogLimitOffsetPagination(LimitOffsetPagination):
    pass
