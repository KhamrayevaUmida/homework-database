from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('car/', car),
    path('fruit/', fruit),
    path('animal/', animal),
    path('telephone/', telephone),
    path('computer/', computer),
    path('color/', color),
    path('mebel/', mebel),
    path('book/', book),
    path('texnika/', texnika),
]
