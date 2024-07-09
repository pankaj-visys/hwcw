from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser

# Create your models here.
class Status(models.Model):
    statusText = models.CharField(max_length = 200)
    statusDate = models.DateTimeField()
    statusClient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.statusText
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)