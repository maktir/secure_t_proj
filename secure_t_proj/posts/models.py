from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.text


class CommentToPost(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_to_post"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments_to_post"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class CommentToComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_to_comment"
    )
    parent_comment = models.ForeignKey(
        CommentToPost, on_delete=models.CASCADE, related_name="comments_to_comment"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )
