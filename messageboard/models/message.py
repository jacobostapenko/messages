from django.db import models

#from c4c.models import Recipe, Ingredient


class message(models.Model):
    message = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='aynonomous')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'message'