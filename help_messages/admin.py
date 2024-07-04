from django.contrib import admin
from .models import HelpMessage, HelpMessageTranslation
# Register your models here.
class HelpMessageTranslationInline(admin.TabularInline):
    model = HelpMessageTranslation
    extra = 0
    
class HelpMessageAdmin(admin.ModelAdmin):
    inlines = [ HelpMessageTranslationInline]

admin.site.register(HelpMessage, HelpMessageAdmin)
