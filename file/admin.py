from django.contrib import admin
from file.models import FileNotice, FileActivity, FileFree, FileShare, FileStudy, FileJokbo


admin.site.register(FileNotice)
admin.site.register(FileActivity)
admin.site.register(FileFree)
admin.site.register(FileShare)
admin.site.register(FileStudy)
admin.site.register(FileJokbo)
