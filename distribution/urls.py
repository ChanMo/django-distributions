from django.urls import path

from .views import *

urlpatterns = [
        path('<slug:slug>/', AppView.as_view()),
        #path('api/<slug:slug>/', AppApiView.as_view())
]
