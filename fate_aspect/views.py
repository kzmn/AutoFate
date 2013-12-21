from rest_framework import viewsets
from fate_aspect.models import *

class AspectViewSet(viewsets.ModelViewSet):
    model = Aspect
