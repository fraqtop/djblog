# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
cats_choise = (
    ('Sciense','Sciense'),
    ('Sport','Sport'),
    ('Economics','Economics'),
    ('Other','Other')
)

class Article (models.Model):
    class Meta:
        db_table = "Article"
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Date = models.DateTimeField(default=datetime.now())
    Pic = models.CharField(max_length=100, default="defaultarticle.jpeg")
    Likes = models.IntegerField(default=0)
    Category = models.CharField(max_length=10, choices=cats_choise, default='Other')

class Comment (models.Model):
    class Meta:
        db_table = 'Comment'
    Text = models.TextField(verbose_name="Добавить комментарий")
    Owner_article = models.ForeignKey(Article)
