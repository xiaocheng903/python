from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Article(models.Model):
    title=models.CharField("标题",max_length=50)
    writer=models.CharField(max_length=20,null=True)
    create_date=models.DateField()
    modify_date=models.DateField(auto_now=True)
    content=models.TextField()
    is_show=models.BooleanField()

    class Meta:
        db_table="article"

    def  __str__(self):
        return self.title

STATE_CHOICES = (

    (0, u'待审核'),
    (1, u'架构师待审核'),
    (2, u'待发布'),
    (3, u'发布中'),
    (4, u'发布成功待测试'),
    (5, u'生产验证通过'),
    (6, u'作废'),
    (7, u'驳回'),
    (8, u'正在重启'),
    (9, u'重启完成'),
    (10, u'回滚中'),
    (11, u'回滚完成'),
    (12, u'发布失败'),
    (13, u'回滚失败'),
)
SQlSTATE_CHOICES = (

    (0, u'待审核'),
    (1, u'DBA待执行'),
    (2, u'待测试'),
    (3, u'验证通过'),
    (4, u'作废'),
    (5, u'驳回'),

)

RELEASE_CHOICES = (
    (0, u'准备发布'),
    (1, u'压缩完成'),
    (2, u'传输完成'),
    (3, u'发布完成'),
    (4, u'执行发布失败'),
    (5, u'驳回'),

)
class Apply(models.Model):
    project=models.CharField("项目名称",max_length=50)
    tags=models.CharField("标签",max_length=50)
    branchname=models.CharField("分支名称",max_length=50,default='default')
    nowdate=models.CharField("时间",max_length=50)
    repertory=models.TextField()
    jsleader=models.CharField("技术负责人",max_length=50)
    csleader=models.CharField("测试负责人",max_length=50)
    cpleader=models.CharField("产品负责人",max_length=50)
    applydate=models.CharField("上线时间",max_length=50)
    applysql=models.TextField()
    applysql1=models.TextField(default="")
    applyEnv = models.CharField("环境",max_length=40,default="0")
    applyconfig=models.TextField()
    beizhu=models.TextField()
    dbname=models.CharField("库名",max_length=50,default="abc")
    dbname1=models.CharField("库名1",max_length=50,default="aaa")
    status=models.IntegerField("状态",choices=STATE_CHOICES,default=0)
    applyuserId=models.IntegerField("关联user表")
    version=models.CharField("版本号",max_length=50,default="未发布")
    type=models.IntegerField("发布状态标识",default=0)
    checkmachine=models.CharField("选中发布机器列表",max_length=100,default=0)
    release_status=models.IntegerField("状态",choices=RELEASE_CHOICES,default=0)



    class Meta:
        db_table="apply"


class userinfo(models.Model):
    name=models.CharField("姓名",max_length=30)
    groupuser=models.CharField("所属组",max_length=30)
    quanxian=models.CharField("权限",max_length=30)
    email=models.CharField("email",max_length=50,default=0)
    passwd=models.CharField("passwd",max_length=50,default=0)


    class Meta:
        db_table="userinfo"

class sqlapply(models.Model):
    beizhu = models.TextField()
    dbname = models.CharField("库名", max_length=50, default="abc")
    dbname1 = models.CharField("库名", max_length=50, default="2")
    title = models.CharField("标题", max_length=50, default="测试标题")
    status = models.IntegerField("状态", choices=SQlSTATE_CHOICES, default=0)
    applysql=models.TextField()
    applysql2=models.TextField(default="")
    applydate=models.CharField("上线时间",max_length=50)
    applyuserId=models.IntegerField("关联user表")
    nowdate=models.CharField("时间",max_length=50,default="2018-07-22")
    version=models.CharField("版本号",max_length=50,default="未发布")
    type=models.IntegerField("发布状态标识",default=0)


class projectToMachine(models.Model):

    project=models.CharField("项目名称",max_length=50)
    machine=models.CharField("服务器IP",max_length=60)
    mastatus=models.CharField("服务器发布状态",max_length=30)
    start_release_time=models.CharField("服务发布时间",max_length=50)
    succ_release_time=models.CharField("发布完成时间",max_length=50)
    port=models.CharField("端口号",max_length=30,default="8080")
    applyEnv = models.CharField("环境",max_length=40,default="0")

class User_Grpup(models.Model):
   username=models.CharField("用户",max_length=50)
   name=models.CharField("中文名字",max_length=50,default="0")
   role = models.CharField("角色",max_length=50)
   group = models.CharField("组", max_length=50)
   level = models.CharField("leader",max_length=20,default="0")
   mail = models.EmailField("邮箱")

class Grpup_update_project(models.Model):
   role=models.CharField("组",max_length=50)
   update_project = models.CharField("项目",max_length=50)

class project_gitaddress(models.Model):
    project=models.CharField("projectname",max_length=50)
    name = models.CharField("name", max_length=50,default="None")
    gitaddress = models.CharField("gitaddress",max_length=100)


class Head(models.Model):
    username=models.CharField("projectname",max_length=50)
    role = models.CharField("name", max_length=50,default="None")


#consul配置文件
class consul_project(models.Model):
    project = models.CharField("项目", max_length=50)
    consul_url = models.CharField("consul路径", max_length=100)
    consul_env = models.CharField("环境", max_length=30)


class consul_version(models.Model):
    project = models.CharField("项目", max_length=50)
    consul_version = models.CharField("版本", max_length=80)
    consul_key = models.TextField()
    consul_values = models.TextField()
    consul_env = models.CharField("环境", max_length=30,default='test')



