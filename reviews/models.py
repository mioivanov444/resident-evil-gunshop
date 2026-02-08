from django.db import models
from guns.models import Gun


class Review(models.Model):
    gun = models.ForeignKey(
        Gun,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional name (leave blank to post anonymously)"
    )
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        help_text="Rating from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.gun.name}"
