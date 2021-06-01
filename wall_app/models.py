from django.db import models
from login_reg_app.models import User

# ONE
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="message_by_user", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments - OTM

# MANY
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="comment_by_user", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)