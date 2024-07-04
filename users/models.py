from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    LANGUAGE_CHOICES = {
        'kz': 'Kazakh',
        'ru': 'Russian',
    }
    telegram_id = models.IntegerField()
    language = models.CharField(max_length=2, default='kz', choices=LANGUAGE_CHOICES)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.telegram_id
    
class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    bot_feedback = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment