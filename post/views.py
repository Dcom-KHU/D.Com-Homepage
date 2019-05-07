from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed
from user.models import Profile
from post.models import PostNotice, PostFree, PostJokbo, PostShare, PostStudy
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

            print(list_var)

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

    if profile.isVerified != 2:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                postobj = PostNotice.objects.create(
                    title=request.POST['title'],
                    content=request.POST['content'],
                    userIdx=request.user,
                    tag=request.POST['tag']
                )
                return redirect('/post/notice/{}'.format(postobj.pk))
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

    if profile.isVerified == 0:
        raise PermissionDenied

    if request.method == "POST":
        try:
            require_keys = ('content', 'rootId')
            if all(i in request.POST for i in require_keys):
                parentPost = PostNotice.objects.get(pk=post_id)

                post = PostNotice.objects.create(
                    content=request.POST['content'],
                    parent=parentPost,
                    userIdx=request.user
                )
                return redirect('/post/notice/{}'.format(request.POST['rootId']))
            else:
                return HttpResponseBadRequest("Key Error")
        except PostNotice.DoesNotExist:
            raise Http404
    else:
        raise HttpResponseNotAllowed


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

                if check is False:
                    break

            print(list_var)

            return render(request, 'notice_post.html', {
                'post': post_obj,
                'comments': list_var,
                'commentForm': PostForm()
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

    if profile.isVerified == 0:
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
                'commentForm': PostForm()
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
                'commentForm': PostForm()
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
                'commentForm': PostForm()
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
def free_post(request, parents=-1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    if parents == -1:
        params = ""
    else:
        params = str(parents)

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                if parents == -1:
                    postobj = PostFree.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user
                    )
                    return redirect('/post/notice/{}'.format(postobj.pk))
                elif 'next' in request.POST:
                    parentPost = PostFree.objects.get(pk=parents)
                    postobj = PostFree.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        parent=parentPost
                    )
                    return redirect(request.POST['next'])
        except PostFree.DoesNotExist:
            raise Http404
    else:
        return render(request, "posts.html", {
            'link': '/post/notice/write/' + params,
            'form': PostForm()
        })

@login_required
def jokbo_post(request, parents=-1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    if parents == -1:
        params = ""
    else:
        params = str(parents)

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                if parents == -1:
                    postobj = PostJokbo.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag']
                    )
                    return redirect('/post/notice/{}'.format(postobj.pk))
                elif 'next' in request.POST:
                    parentPost = PostJokbo.objects.get(pk=parents)
                    postobj = PostJokbo.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag'],
                        parent=parentPost
                    )
                    return redirect(request.POST['next'])
        except PostJokbo.DoesNotExist:
            raise Http404
    else:
        return render(request, "posts.html", {
            'link': '/post/notice/write/' + params,
            'form': PostForm()
        })

@login_required
def share_post(request, parents=-1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    if parents == -1:
        params = ""
    else:
        params = str(parents)

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                if parents == -1:
                    postobj = PostShare.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag']
                    )
                    return redirect('/post/notice/{}'.format(postobj.pk))
                elif 'next' in request.POST:
                    parentPost = PostShare.objects.get(pk=parents)
                    postobj = PostShare.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag'],
                        parent=parentPost
                    )
                    return redirect(request.POST['next'])
        except PostShare.DoesNotExist:
            raise Http404
    else:
        return render(request, "posts.html", {
            'link': '/post/notice/write/' + params,
            'form': PostForm()
        })

@login_required
def study_post(request, parents=-1):
    profile = Profile.objects.get(pk=request.user)

    if profile.isVerified == False:
        raise PermissionDenied

    if parents == -1:
        params = ""
    else:
        params = str(parents)

    if request.method == "POST":
        try:
            require_keys = ('title', 'content', 'tag')
            if all(i in request.POST for i in require_keys):
                if parents == -1:
                    postobj = PostStudy.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag']
                    )
                    return redirect('/post/notice/{}'.format(postobj.pk))
                elif 'next' in request.POST:
                    parentPost = PostStudy.objects.get(pk=parents)
                    postobj = PostStudy.objects.create(
                        title=request.POST['title'],
                        content=request.POST['contents'],
                        userIdx=request.user,
                        tag=request.POST['tag'],
                        parent=parentPost
                    )
                    return redirect(request.POST['next'])
        except PostStudy.DoesNotExist:
            raise Http404
    else:
        return render(request, "posts.html", {
            'link': '/post/notice/write/' + params,
            'form': PostForm()
        })
