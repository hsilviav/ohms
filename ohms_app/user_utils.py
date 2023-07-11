from django.http import HttpRequest


def is_logged_in(request: HttpRequest) -> bool:
    return request.user.is_authenticated

