from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Subtitles

# Register your models here.
admin.site.register(Subtitles,ImportExportModelAdmin)
