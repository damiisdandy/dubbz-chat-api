from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=200)
    source = models.CharField(max_length=255)  # ipv4 Address
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source}'s Message"
