from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin

from .serializers import *


class AppApiView(RetrieveAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    lookup_field = 'slug'
