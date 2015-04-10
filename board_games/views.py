from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


from board_games.models import BoardGame
from board_games.serializers import BoardGameSerializer
from editors.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


class BoardGameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'update', 'create',
    'retrieve', and 'destroy' actions
    """
    queryset = BoardGame.objects.all()
    serializer_class = BoardGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
