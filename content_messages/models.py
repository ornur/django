from django.db import models

# Create your models here.
class Message(models.Model):
    role = models.ForeignKey('users.Role', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
    
class MessageTranslation(models.Model):
    LANGUAGE_CHOICES = {
        'kz': 'Kazakh',
        'ru': 'Russian',
    }
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content