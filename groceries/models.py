from django.conf import settings
from django.db import models


class Item(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    description = models.TextField()


class Run(models.Model):
    "Generated Model"
    planned_date = models.DateField()
    actual_date = models.DateField()
    list = models.ForeignKey(
        "groceries.List",
        on_delete=models.PROTECT,
        related_name="run_list",
    )
    managers = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="run_managers",
    )
    viewers = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="run_viewers",
    )


class List(models.Model):
    "Generated Model"
    item = models.ManyToManyField(
        "groceries.Item",
        related_name="list_item",
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()


# Create your models here.
