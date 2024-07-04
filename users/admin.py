from django.contrib import admin
from .models import User, Role, UserFeedback

# Register your models here.
admin.site.register(Role)

class UserFeedbackInline(admin.TabularInline):
    model = UserFeedback
    extra = 0
    
class UserAdmin(admin.ModelAdmin):
    inlines = [ UserFeedbackInline]

admin.site.register(User, UserAdmin)