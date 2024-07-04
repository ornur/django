from django.contrib import admin
from .models import Message, MessageTranslation
# Register your models here.
class MessageTranslationInline(admin.TabularInline):
    model = MessageTranslation
    extra = 0
    
class MessageAdmin(admin.ModelAdmin):
    inlines = [ MessageTranslationInline]
    
admin.site.register(Message, MessageAdmin)