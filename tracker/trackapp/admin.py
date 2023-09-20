from django.contrib import admin
from .models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'type', 'amount', 'date')  # Fields to display in the admin list view

admin.site.register(Track, TrackAdmin)