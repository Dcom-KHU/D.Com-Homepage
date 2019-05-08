from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed
from user.models import Profile
from post.models import PostNotice, PostActivity, PostFree, PostJokbo, PostShare, PostStudy, PostStudyMember
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

                if check is False:
                    break

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var,
                'commentForm': PostForm()
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

    if page <= 3:
        start_page = 1
        if pages > 5:
            end_page = 5
        else:
            end_page = pages
    elif page > pages - 2:
        end_page = pages
        if pages <= 5:
            start_page = 1
        else:
            start_page = page - 2
    else:
        start_page = page - 2
        end_page = page + 2

    return render(request, 'notice_list.html', {
        'posts': list_var,
        'current_page': page,
        'pages': pages,
        'start_page': start_page,
        'end_page': end_page,
        'range': range(start_page, end_page + 1)
    })


@login_required
def notice_post(request):
    profile = Profile.objects.get(pk=request.user)

    if profile.group != 2:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                post_obj = PostNotice.objects.create(
                    title=request.POST['title'],
                    content=request.POST['content'],
                    userIdx=request.user,
                    tag=request.POST['tag']
                )
                return redirect('/post/notice/{}'.format(post_obj.pk))
            else:
                return HttpResponseBadRequest("Error During Error Processing")
        except PostNotice.DoesNotExist:
            raise Http404
    else:
        return render(request, "notice_write.html", {
            'form': PostForm()
        })


@login_required
def notice_comment(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.group == 0:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('content',)
            if all(i in request.POST for i in require_keys):
                parent_post = PostNotice.objects.get(pk=post_id)

                post = PostNotice.objects.create(
                    content=request.POST['content'],
                    parent=parent_post,
                    userIdx=request.user
                )

                # root 찾는 코드
                root = post.parent

                while root.parent is not None:
                    root = root.parent

                return redirect('/post/notice/{}'.format(root.pk))
            else:
                return HttpResponseBadRequest("Key Error")
        except PostNotice.DoesNotExist:
            raise Http404
    else:
        raise HttpResponseNotAllowed


@login_required
def notice_delete(request, post_id):
    try:
        post = PostNotice.objects.get(pk=post_id)

        if post.userIdx == request.user:
            post.delete()
        else:
            raise PermissionDenied

    except PostNotice.DoesNotExist:
        raise Http404


@login_required
def study_detail(request, post_id):
    profile = Profile.objects.get(pk=post_id)

    if profile.group == 0:
        raise PermissionDenied

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

                        list_var = list_var[:i+temp+1] + sub_comment + list_var[i+temp+1:]
                        temp += len(sub_comment)

                if check is False:
                    break

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var,
                'commentForm': PostForm()
            })
        else:
            raise PermissionDenied
    except PostStudy.DoesNotExist:
        raise Http404


def study_list(request, page=1):
    post_obj = PostStudy.objects.filter(parent=None).order_by('-id')
    obj_num = post_obj.count()

    pages = ((obj_num-1) // 5) + 1
    list_var = post_obj[(page-1)*5:page*5]

    if page <= 3:
        start_page = 1
        if pages > 5:
            end_page = 5
        else:
            end_page = pages
    elif page > pages - 2:
        end_page = pages
        if pages <= 5:
            start_page = 1
        else:
            start_page = page - 2
    else:
        start_page = page - 2
        end_page = page + 2

    return render(request, 'notice_list.html', {
        'posts': list_var,
        'current_page': page,
        'pages': pages,
        'start_page': start_page,
        'end_page': end_page,
        'range': range(start_page, end_page + 1)
    })


@login_required
def study_post(request):
    profile = Profile.objects.get(pk=request.user)

    if profile.group == 0:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                post_obj = PostStudy.objects.create(
                    title=request.POST['title'],
                    content=request.POST['content'],
                    userIdx=request.user,
                    tag=request.POST['tag']
                )
                return redirect('/post/study/{}'.format(post_obj.pk))
            else:
                return HttpResponseBadRequest("Error During Error Processing")
        except PostStudy.DoesNotExist:
            raise Http404
    else:
        return render(request, "notice_write.html", {
            'form': PostForm()
        })


@login_required
def study_comment(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.group == 0:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('content',)
            if all(i in request.POST for i in require_keys):
                parent_post = PostStudy.objects.get(pk=post_id)

                post = PostStudy.objects.create(
                    content=request.POST['content'],
                    parent=parent_post,
                    userIdx=request.user
                )

                # root 찾는 코드
                root = post.parent

                while root.parent is not None:
                    root = root.parent

                return redirect('/post/study/{}'.format(root.pk))
            else:
                return HttpResponseBadRequest("Key Error")
        except PostStudy.DoesNotExist:
            raise Http404
    else:
        raise HttpResponseNotAllowed


@login_required
def study_delete(request, post_id):
    try:
        post = PostStudy.objects.get(pk=post_id)

        if post.userIdx == request.user:
            post.delete()
        else:
            raise PermissionDenied

    except PostStudy.DoesNotExist:
        raise Http404


@login_required
def study_join(request, post_id):
    profile = Profile.objects.get(pk=request.user)

    if profile.group == 0:
        raise PermissionDenied

    try:
        post = PostStudy.objects.get(pk=post_id)
        study_member = PostStudyMember.objects.create(
            userIdx=request.user,
            studyIdx=post
        )
        return redirect('/post/study/{}'.format(post.pk))
    except PostStudy.DoesNotExist:
        raise Http404
