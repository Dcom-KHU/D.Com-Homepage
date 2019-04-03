from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from post.models import PostNotice


def notice_detail(request, post_id):
    post_obj = PostNotice.objects.get(pk=post_id)
    post_obj.hit += 1
    post_obj.save()

    if post_obj.parent is None:
        comment = PostNotice.objects.filter(parent=post_obj).values()
        list_var = list(comment)
        depth = 0

        while True:
            temp = 0
            depth += 1
            check = False

            for i in range(len(comment)):
                if comment[i].depth == depth:
                    check = True


            if check == False:
                break
        return render(request, 'posts_notice.html', {
            'post': post_obj
        })
    else:
        raise PermissionDenied
