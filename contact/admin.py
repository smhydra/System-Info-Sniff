from django.contrib import admin
from .models import TextUpload

@admin.register(TextUpload)
class TextUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'char_count', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'char_count_display')

    fieldsets = (
        ('Text Information', {
            'fields': ('title', 'content')
        }),
        ('Statistics', {
            'fields': ('char_count_display',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def char_count(self, obj):
        return len(obj.content)
    char_count.short_description = 'Characters'

    def char_count_display(self, obj):
        return f"{len(obj.content)} characters"
    char_count_display.short_description = 'Character Count'
