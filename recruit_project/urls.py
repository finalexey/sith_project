from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recruit_app/', include('recruit_app.urls')),
    path('recruit_polls/', include('recruit_polls.urls')),
]
