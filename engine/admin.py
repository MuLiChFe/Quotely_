from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Subtitles, Films

# Register your models here.
admin.site.register(Subtitles, ImportExportModelAdmin)
admin.site.register(Films, ImportExportModelAdmin)
