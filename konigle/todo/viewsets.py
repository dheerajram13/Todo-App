from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

#creating viewset for the model. This is actually a controller for the model.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer