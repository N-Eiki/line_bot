from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('linebot_app/', include('linebot_app.urls')),
    path('admin/', admin.site.urls),
]
