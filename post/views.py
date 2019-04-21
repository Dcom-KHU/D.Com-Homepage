from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from user.models import Profile
from post.models import PostNotice, PostFree, PostJokbo, PostShare, PostStudy
from post.form import PostNoticeForm, PostJokboForm, PostFreeForm, PostShareForm, PostStudyForm, CommentForm


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
                'commentForm': CommentForm()
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


def share_detail(request, post_id):
    try:
        post_obj = PostShare.objects.get(pk=post_id)
        post_obj.hit += 1
        post_obj.save()

        if post_obj.parent is None:
            comment = PostShare.objects.filter(parent=post_obj).values()
            list_var = list(comment)
            depth = 0

            while True:
                temp = 0
                depth += 1
                check = False

                for i in range(len(list_var)):
                    if list_var[i]['depth'] == depth:
                        check = True
                        sub_comment = list(PostShare.objects.filter(parent_id=list_var[i]['id']).values())

                        list_var = list_var[:i+temp+1] + sub_comment + list_var[i+temp+1:]
                        temp += len(sub_comment)

                if check == False:
                    break

            print(list_var)

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var,
                'commentForm': CommentForm()
            })
        else:
            raise PermissionDenied
    except PostNotice.DoesNotExist:
        raise Http404


def share_list(request, page=1):
    post_obj = PostShare.objects.filter(parent=None).order_by('-id')
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
        raise PermissionDenied

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
                'comments': list_var,
                'commentForm': CommentForm()
            })
        else:
            raise PermissionDenied
    except PostFree.DoesNotExist:
        raise Http404


@login_required
def free_list(request, page=1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

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
        raise PermissionDenied

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
                'comments': list_var,
                'commentForm': CommentForm()
            })
        else:
            raise PermissionDenied
    except PostJokbo.DoesNotExist:
        raise Http404


@login_required
def jokbo_list(request, page=1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    post_obj = PostJokbo.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num - 1) // 5) + 1
    list_var = post_obj[(page - 1) * 5:page * 5]
    return render(request, 'notice_list.html', {
        'posts': list_var,
        'page': page,
        'pages': pages
    })

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
                'comments': list_var,
                'commentForm': CommentForm()
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


@login_required
def notice_post(request, parents=-1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    if parents == -1:
        params = ""
    else:
        params = str(parents)

    if request.method == "POST":
        try:
            require_keys = ('title', 'content')
            if all(i in request.POST for i in require_keys):
                if parents != -1:
                    parentPost = PostNotice.objects.get(pk=parents)
                    postobj = PostNotice.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag'],
                        parent=parentPost
                    )
                else:
                    postobj = PostNotice.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag']
                    )
        except PostNotice.DoesNotExist:
            pass
    else:
        return render(request, "posts.html", {
            'link': '/post/notice/write/' + params,
            'form': PostNoticeForm()
        })




@login_required
def free_post(request, parents=-1):
    return

@login_required
def jokbo_post(request, parents=-1):
    return

@login_required
def share_post(request, parents=-1):
    return

@login_required
def study_post(request, parents=-1):
    return