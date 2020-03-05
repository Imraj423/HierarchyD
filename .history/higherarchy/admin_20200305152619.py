from .models import File
from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin

admin.site.register(File,
DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)