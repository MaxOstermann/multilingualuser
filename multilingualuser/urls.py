from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
)
