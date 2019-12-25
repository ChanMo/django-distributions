from django.views.generic.detail import DetailView

from .models import *


class AppView(DetailView):
    model = App
    lookup_field = 'slug'
    template_name = 'distribution/index.html'
