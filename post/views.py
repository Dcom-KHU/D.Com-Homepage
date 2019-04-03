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

            for i in range(len(list_var)):
                if list_var[i]['depth'] == depth:
                    check = True
                    sub_comment = list(PostNotice.objects.filter(parent_id=list_var[i]['id']).values())

                    list_var = list_var[:i+temp+1] + sub_comment + list_var[i+temp+1:]
                    temp += len(sub_comment)

            if check == False:
                break

        print(list_var)

        return render(request, 'posts_notice.html', {
            'post': post_obj,
            'comments': list_var
        })
    else:
        raise PermissionDenied
