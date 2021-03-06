# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from editors.views import EditorViewSet, UserViewSet
from board_games.views import BoardGameViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'editors', EditorViewSet)
router.register(r'board-games', BoardGameViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api-token-auth/',
        'rest_framework_jwt.views.obtain_jwt_token',
        name='login'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
