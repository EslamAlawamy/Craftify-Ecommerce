from django.contrib import admin
from authentication.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)