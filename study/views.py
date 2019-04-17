from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from user.models import Profile
from post.models import PostStudy


@login_required
def study_detail(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    try:
        post_obj = PostStudy.objects.get(pk=post_id)
        post_obj.hit += 1
        post_obj.save()

        if post_obj.parent is None:
            comment = PostStudy.objects.filter(parent=post_obj).values()
            list_var = list(comment)
            depth = 0

            while True:
                temp = 0
                depth += 1
                check = False

                for i in range(len(list_var)):
                    if list_var[i]['depth'] == depth:
                        check = True
                        sub_comment = list(PostStudy.objects.filter(parent_id=list_var[i]['id']).values())

                        list_var = list_var[:i + temp + 1] + sub_comment + list_var[i + temp + 1:]
                        temp += len(sub_comment)

                if check == False:
                    break

            print(list_var)

            return render(request, 'study_post.html', {
                'post': post_obj,
                'comments': list_var
            })
        else:
            raise PermissionDenied
    except PostStudy.DoesNotExist:
        return Http404


@login_required
def study_list(request, page=1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    post_obj = PostStudy.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num - 1) // 5) + 1
    list_var = post_obj[(page - 1) * 5:page * 5]
    return render(request, 'study_list.html', {
        'posts': list_var,
        'page': page,
        'pages': pages
    })

