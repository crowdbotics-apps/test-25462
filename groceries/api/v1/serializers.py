from rest_framework import serializers
from groceries.models import Item, List, Run


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"
