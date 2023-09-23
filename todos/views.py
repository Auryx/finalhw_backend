from .models import Cheese
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer


class CheeseViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Cheese.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]