from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    paze_size=1


class LargePagination(PageNumberPagination):
    paze_size=2