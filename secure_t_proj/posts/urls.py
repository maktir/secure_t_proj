from django.urls import include, path
from rest_framework import routers
from .views import (PostViewSet,
                    CommentToPostViewSet,
                    CommentToCommentViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentToPostViewSet, basename='comments')
router.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/nested_comments',
                CommentToCommentViewSet, basename='nested_comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]