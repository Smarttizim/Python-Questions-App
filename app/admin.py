from django.contrib import admin
from .models import *

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)

class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'quest_num', 'theme')
    list_filter = ('theme',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact')
    search_fields = ('name', 'contact')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Quest, QuestAdmin)
