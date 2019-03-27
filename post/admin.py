from django.contrib import admin
from post.models import PostStudy, PostJokbo, PostAlbum, PostFree, PostStudyMember, PostNotice
# Register your models here.

admin.site.register(PostStudyMember)
admin.site.register(PostStudy)
admin.site.register(PostFree)
admin.site.register(PostJokbo)
admin.site.register(PostAlbum)
admin.site.register(PostNotice)

