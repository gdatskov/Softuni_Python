from django.contrib import admin

from mymusic.mymusicapp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
