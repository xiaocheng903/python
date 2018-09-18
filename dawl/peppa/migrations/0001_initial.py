# Generated by Django 2.0.6 on 2018-08-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, verbose_name='项目名称')),
                ('tags', models.CharField(max_length=50, verbose_name='分支名称')),
                ('nowdate', models.CharField(max_length=50, verbose_name='时间')),
                ('repertory', models.TextField()),
                ('jsleader', models.CharField(max_length=50, verbose_name='技术负责人')),
                ('csleader', models.CharField(max_length=50, verbose_name='测试负责人')),
                ('cpleader', models.CharField(max_length=50, verbose_name='产品负责人')),
                ('applydate', models.CharField(max_length=50, verbose_name='上线时间')),
                ('applysql', models.TextField()),
                ('applysql1', models.TextField(default='')),
                ('applyconfig', models.TextField()),
                ('beizhu', models.TextField()),
                ('dbname', models.CharField(default='abc', max_length=50, verbose_name='库名')),
                ('dbname1', models.CharField(default='aaa', max_length=50, verbose_name='库名1')),
                ('status', models.IntegerField(choices=[(0, '待审核'), (1, '架构师待审核'), (2, '待发布'), (3, '发布中'), (4, '发布成功待测试'), (5, '生产验证通过'), (6, '作废'), (7, '驳回'), (8, '正在重启'), (9, '重启完成'), (10, '回滚中'), (11, '回滚完成'), (12, '发布失败'), (13, '回滚失败')], default=0, verbose_name='状态')),
                ('applyuserId', models.IntegerField(verbose_name='关联user表')),
                ('version', models.CharField(default='未发布', max_length=50, verbose_name='版本号')),
                ('type', models.IntegerField(default=0, verbose_name='发布状态标识')),
                ('checkmachine', models.CharField(default=0, max_length=100, verbose_name='选中发布机器列表')),
                ('release_status', models.IntegerField(choices=[(0, '准备发布'), (1, '压缩完成'), (2, '传输完成'), (3, '发布完成'), (4, '执行发布失败'), (5, '驳回')], default=0, verbose_name='状态')),
            ],
            options={
                'db_table': 'apply',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('writer', models.CharField(max_length=20, null=True)),
                ('create_date', models.DateField()),
                ('modify_date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('is_show', models.BooleanField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Grpup_update_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, verbose_name='组')),
                ('update_project', models.CharField(max_length=50, verbose_name='项目')),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='projectname')),
                ('role', models.CharField(default='None', max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='project_gitaddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, verbose_name='projectname')),
                ('name', models.CharField(default='None', max_length=50, verbose_name='name')),
                ('gitaddress', models.CharField(max_length=100, verbose_name='gitaddress')),
            ],
        ),
        migrations.CreateModel(
            name='projectToMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, verbose_name='项目名称')),
                ('machine', models.CharField(max_length=60, verbose_name='服务器IP')),
                ('mastatus', models.CharField(max_length=30, verbose_name='服务器发布状态')),
                ('start_release_time', models.CharField(max_length=50, verbose_name='服务发布时间')),
                ('succ_release_time', models.CharField(max_length=50, verbose_name='发布完成时间')),
                ('port', models.CharField(default='8080', max_length=30, verbose_name='端口号')),
            ],
        ),
        migrations.CreateModel(
            name='sqlapply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beizhu', models.TextField()),
                ('dbname', models.CharField(default='abc', max_length=50, verbose_name='库名')),
                ('dbname1', models.CharField(default='2', max_length=50, verbose_name='库名')),
                ('title', models.CharField(default='测试标题', max_length=50, verbose_name='标题')),
                ('status', models.IntegerField(choices=[(0, '待审核'), (1, 'DBA待执行'), (2, '待测试'), (3, '验证通过'), (4, '作废'), (5, '驳回')], default=0, verbose_name='状态')),
                ('applysql', models.TextField()),
                ('applysql2', models.TextField(default='')),
                ('applydate', models.CharField(max_length=50, verbose_name='上线时间')),
                ('applyuserId', models.IntegerField(verbose_name='关联user表')),
                ('nowdate', models.CharField(default='2018-07-22', max_length=50, verbose_name='时间')),
                ('version', models.CharField(default='未发布', max_length=50, verbose_name='版本号')),
                ('type', models.IntegerField(default=0, verbose_name='发布状态标识')),
            ],
        ),
        migrations.CreateModel(
            name='User_Grpup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户')),
                ('name', models.CharField(default='0', max_length=50, verbose_name='中文名字')),
                ('role', models.CharField(max_length=50, verbose_name='角色')),
                ('group', models.CharField(max_length=50, verbose_name='组')),
                ('level', models.CharField(default='0', max_length=20, verbose_name='leader')),
                ('mail', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('groupuser', models.CharField(max_length=30, verbose_name='所属组')),
                ('quanxian', models.CharField(max_length=30, verbose_name='权限')),
                ('email', models.CharField(default=0, max_length=50, verbose_name='email')),
                ('passwd', models.CharField(default=0, max_length=50, verbose_name='passwd')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
