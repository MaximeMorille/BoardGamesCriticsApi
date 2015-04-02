from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


from editors.models import Editor
from editors.serializers import EditorSerializer
from editors.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


class EditorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'update', 'create',
    'retrieve', and 'destroy' actions
    """
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

from django.contrib.auth.models import User
from editors.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
