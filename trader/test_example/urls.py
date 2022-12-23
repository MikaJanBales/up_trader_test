from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^my_app/', include('my_app.urls')),
    re_path(r'^admin/', admin.site.urls),
]
