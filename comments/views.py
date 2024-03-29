# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Post
from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def post_comment(request, post_pk):
    # 获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        # 从request.POST获取表单
        form = CommentForm(request.POST)
        # 判断表单是否可用
        if form.is_valid():
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post
            # 保存数据到数据库
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
        # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
        return redirect(post)



