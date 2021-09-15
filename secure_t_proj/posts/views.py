from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .models import Post, CommentToPost
from .serializers import (PostSerializer, CommentToPostSerializer,
                          CommentToCommentSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly | permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentToPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly | permissions.IsAdminUser]
    serializer_class = CommentToPostSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments_to_post.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user,
                        post_id=post.id)


class CommentToCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly | permissions.IsAdminUser]
    serializer_class = CommentToCommentSerializer

    def get_queryset(self):
        parent_comment = get_object_or_404(CommentToPost,
                                           pk=self.kwargs['comment_id'])
        return parent_comment.comments_to_comment.all()

    def perform_create(self, serializer):
        parent_comment = get_object_or_404(CommentToPost,
                                           id=self.kwargs['comment_id'])
        serializer.save(author=self.request.user,
                        parent_comment=parent_comment)
