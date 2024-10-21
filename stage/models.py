from django.db import models
from users.models import User
from uuid import uuid4


class Stage (models.Model) :
    id = models.UUIDField(default=uuid4, primary_key=True)
    owner = models.ForeignKey(User, related_name='stage_owner', on_delete=models.CASCADE)
    visitor_counter = models.IntegerField(default=0)
    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title