from django.urls import path
from new_app.views import my_view

urlpatterns = [
     path('', my_view)
]