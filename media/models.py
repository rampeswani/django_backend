from django.db import models
from LoginUtility.models import User
class File(models.Model):
    id = models.AutoField(primary_key=True)
    file_url = models.CharField(max_length=1000, blank = True, null= True)
    user = models.ForeignKey(User,related_name='File_user', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='File_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,related_name='File_updated_by',on_delete=models.CASCADE , null=True, blank= True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default= True)

    role = models.CharField(max_length=10, choices=User.ROLE_CHOICES, default='user')


    class Meta :
        ordering = ['id']

    def __str__(self):
        return str(self.id)










