from rest_framework import routers
from todo.viewsets import TodoViewSet


router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet) #/todo(router) linked to TodoViewSet.
# this routers.py will be included in the urls.py