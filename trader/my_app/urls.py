from django.urls import re_path

from my_app.views import IndexView
app_name = 'my_app'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
