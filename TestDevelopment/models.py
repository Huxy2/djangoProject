from django.db import models


# Create your models here.

class People(models.Model):
    """
    数据库模型类
    """
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    # gender = models.CharField(max_length=2)
    score = models.IntegerField()

    class Meta:
        db_table = 'tb_people'
        verbose_name = ''


class TestDevelopment(models.Model):
    name = models.CharField(max_length=200, verbose_name='项目名称', help_text='项目名称', unique=True)
    leader = models.CharField(max_length=50, verbose_name='项目负责人', help_text='项目负责人')
    desc = models.TextField(verbose_name='项目描述', help_text='项目描述', blank=True, null=True, default='')

    class Meta:
        db_table = 'tb_testdevelopment'
