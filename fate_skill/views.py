from rest_framework import viewsets
from fate_skill.models import *


class SkillViewSet(viewsets.ModelViewSet):
    model = Skill
