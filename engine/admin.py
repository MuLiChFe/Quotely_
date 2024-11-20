from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Subtitles, Film

# Register your models here.
admin.site.register(Subtitles, ImportExportModelAdmin)
admin.site.register(Film, ImportExportModelAdmin)
