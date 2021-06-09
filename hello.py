import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="mysecret",
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ),
)

from django.urls import path
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")


urlpatterns = [path("", index)]

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)