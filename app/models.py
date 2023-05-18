from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(
        verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    # 时间 允许为空
    created_at = models.DateTimeField(null=True, blank=True)

    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(
        verbose_name='性别', choices=gender_choices)

    # 关联表
    # article = models.ForeignKey(to='article',to_field='id')

    # 如果删除 关联的数据也会删除
    # article = models.ForeignKey(to='article',to_field='id',on_delete=models.CASCADE)
    # 如果删除 置空（前提允许为空）
    # article = models.ForeignKey(
    #     to='article', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
