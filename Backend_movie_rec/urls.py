
from django.contrib import admin
from django.urls import path
from .views import Movies,signup,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',Movies),
    path('signup/', signup),
    path('login/',login),

]
