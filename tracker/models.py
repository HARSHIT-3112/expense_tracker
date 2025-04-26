from django.db import models
import uuid
# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    


class Transaction(BaseModel):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("description",)
       
