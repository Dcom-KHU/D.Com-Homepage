from django.contrib import admin
from post.models import PostNotice, PostActivity, PostFree, PostShare, PostStudy, PostStudyMember, PostJokbo


admin.site.register(PostNotice)
admin.site.register(PostActivity)
admin.site.register(PostFree)
admin.site.register(PostShare)
admin.site.register(PostStudy)
admin.site.register(PostStudyMember)
admin.site.register(PostJokbo)

