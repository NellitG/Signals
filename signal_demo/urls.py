from django.contrib import admin
from django.urls import path
from accounts.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
]
