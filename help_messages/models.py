from django.db import models

# Create your models here.
class HelpMessage(models.Model):
    role = models.ForeignKey('users.Role', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
    
class HelpMessageTranslation(models.Model):
    LANGUAGE_CHOICES = {
        'kz': 'Kazakh',
        'ru': 'Russian',
    }
    help_message = models.ForeignKey(HelpMessage, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content