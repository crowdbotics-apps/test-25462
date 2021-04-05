from rest_framework import authentication
from groceries.models import Item, List, Run
from .serializers import ItemSerializer, ListSerializer, RunSerializer
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Item.objects.all()


class RunViewSet(viewsets.ModelViewSet):
    serializer_class = RunSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Run.objects.all()


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = List.objects.all()
