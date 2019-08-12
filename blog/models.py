# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    """
    分类Categery
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签Tag
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    """
    文章post
    """
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)

    # 分类和标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
