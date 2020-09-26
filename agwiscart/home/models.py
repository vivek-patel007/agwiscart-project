from django.db import models

# Create your models here.
class Contact(models.Model):
    cid=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=255)
    subject=models.CharField(max_length=50)
    email=models.CharField(max_length=10)
    msg=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)

    class meta:
        db_table='"contact"'

    def __str__(self):
        return self.full_name