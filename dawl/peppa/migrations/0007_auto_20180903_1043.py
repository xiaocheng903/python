# Generated by Django 2.0.6 on 2018-09-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peppa', '0006_apply_applyenv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.IntegerField(choices=[(0, '待审核'), (1, '架构师待审核'), (2, '待发布'), (3, '发布中'), (4, '发布成功待测试'), (5, '生产验证通过'), (6, '作废'), (7, '驳回'), (8, '正在重启'), (9, '重启完成'), (10, '回滚中'), (11, '回滚完成'), (12, '发布失败'), (13, '回滚失败')], default=0, verbose_name='状态'),
        ),
    ]