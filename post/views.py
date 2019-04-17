from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from user.models import Profile
from post.models import PostNotice, PostFree, PostJokbo
from post.form import PostForm


def notice_detail(request, post_id):
    try:
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

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var,
                'form': PostForm()
            })
        else:
            raise PermissionDenied
    except PostNotice.DoesNotExist:
        raise Http404


def notice_list(request, page=1):
    post_obj = PostNotice.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num-1) // 5) + 1
    list_var = post_obj[(page-1)*5:page*5]
    return render(request, 'notice_list.html', {
        'posts': list_var,
        'page': page,
        'pages': pages
    })


@login_required
def free_detail(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    try:
        post_obj = PostFree.objects.get(pk=post_id)
        post_obj.hit += 1
        post_obj.save()

        if post_obj.parent is None:
            comment = PostFree.objects.filter(parent=post_obj).values()
            list_var = list(comment)
            depth = 0

            while True:
                temp = 0
                depth += 1
                check = False

                for i in range(len(list_var)):
                    if list_var[i]['depth'] == depth:
                        check = True
                        sub_comment = list(PostFree.objects.filter(parent_id=list_var[i]['id']).values())

                        list_var = list_var[:i+temp+1] + sub_comment + list_var[i+temp+1:]
                        temp += len(sub_comment)

                if check == False:
                    break

            print(list_var)

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var
            })
        else:
            raise PermissionDenied
    except PostFree.DoesNotExist:
        raise Http404


@login_required
def free_list(request, page=1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    post_obj = PostFree.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num-1) // 5) + 1
    list_var = post_obj[(page-1)*5:page*5]
    return render(request, 'notice_list.html', {
        'posts': list_var,
        'page': page,
        'pages': pages
    })


@login_required
def jokbo_detail(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    try:
        post_obj = PostJokbo.objects.get(pk=post_id)
        post_obj.hit += 1
        post_obj.save()

        if post_obj.parent is None:
            comment = PostJokbo.objects.filter(parent=post_obj).values()
            list_var = list(comment)
            depth = 0

            while True:
                temp = 0
                depth += 1
                check = False

                for i in range(len(list_var)):
                    if list_var[i]['depth'] == depth:
                        check = True
                        sub_comment = list(PostJokbo.objects.filter(parent_id=list_var[i]['id']).values())

                        list_var = list_var[:i + temp + 1] + sub_comment + list_var[i + temp + 1:]
                        temp += len(sub_comment)

                if check == False:
                    break

            print(list_var)

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var
            })
        else:
            raise PermissionDenied
    except PostJokbo.DoesNotExist:
        raise Http404


@login_required
def jokbo_list(request, page=1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        return PermissionDenied

    post_obj = PostJokbo.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num - 1) // 5) + 1
    list_var = post_obj[(page - 1) * 5:page * 5]
    return render(request, 'notice_list.html', {
        'posts': list_var,
        'page': page,
        'pages': pages
    })
