from django.conf.urls import url

from user import views

app_name = 'user'
urlpatterns = [
    url(r'^login_api/', views.login_api, name='login_api'),
    url(r'^logout_api/', views.logout_api, name='logout_api'),
]