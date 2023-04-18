from django.db.models import *
from .admin import admin


class Stage(Model):
    title = CharField(max_length=60)
    status = IntegerField()

    def __str__(self):
        return self.title  + f" {self.status}"

class Sale(Model):
    client = CharField(max_length=10)
    team = CharField(max_length=150)
    deadline = IntegerField()
    stage_id = ForeignKey(Stage, on_delete=CASCADE)
    price = IntegerField(default=0)
    def __str__(self):
        return self.team


admin.site.register([Stage,Sale])