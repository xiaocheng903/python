from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from peppa.models import *
from peppa import peppaapi,release,tests,release_port
import time
import os,json
# 登陆权限
from django.contrib.auth.decorators import login_required

# 登陆访问权限
from django.contrib.auth.decorators import permission_required
import datetime
tags = []
branch = []
projectnames= []
# Create your views here.


class applysql(TemplateView):
    template_name = "applysql.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(applysql, self).get_context_data(**kwargs)
        nowdate=datetime.datetime.now().strftime("%Y-%m-%d")

        context['nowdate']=nowdate
        return context




#首页
class home(TemplateView):

    template_name="index.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        context['page_title'] = u'项目上线'
        context['page_tail'] = u'明日上线'
        context['page_sql'] = u'SQL上线'
        #获取session
        global_env = peppaapi.get_session_env(self.request)
        context['global_env'] = global_env


        x1 = Apply.objects.all().order_by('-id')
        s = sqlapply.objects.all().order_by('-id')
        x = Apply.objects.filter(applyEnv=global_env).order_by('-id')

        nowdate = datetime.datetime.now().strftime("%Y-%m-%d")
        username = self.request.user.username
        result = []
        resultsql = []
        for i in s:
            if nowdate == i.applydate:
                resultsql.append({
                    'id': i.id,
                    'title': i.title,
                    'beizhu': i.beizhu,
                    'dbname': i.dbname,
                    'applyuser': peppaapi.get_applyuser(i.applyuserId),
                    'applysql': i.applysql,
                    'applydate': i.applydate,
                    'nowdate': i.nowdate,
                    'status': i.get_status_display(),
                    'type': i.type
                })
            context['sqlinfo'] = resultsql
        for item in x:
            if nowdate == item.applydate:
                result.append({
                    'id': item.id,
                    'project': item.project,
                    'appdate': item.applydate,
                    'nowdate': item.nowdate,
                    'applyuser': peppaapi.get_applyuser(item.applyuserId),
                    'status': item.get_status_display(),
                    'type': item.type,
                    'applyEnv': item.applyEnv
                })
            context['appinfo'] = result
        context['username'] = username
        return context



#项目申请
class apply(TemplateView):
    template_name="apply.html"

    def get_context_data(self, **kwargs):

        context = super(apply, self).get_context_data(**kwargs)
        nowdate=datetime.datetime.now().strftime("%Y-%m-%d")

        global_env = self.request.session.get('env')

        context['glo_env'] = global_env
        context['nowdate'] = nowdate
        context['technology'] = Head.objects.filter(role='technology')
        context['test'] = Head.objects.filter(role='test')
        context['product'] = Head.objects.filter(role='product')
        return context

#sql申请存储
class applysqlsave(TemplateView):
    template_name = "applysql.html"

    def post(self, request, *args, **kwargs):
        dbname = request.POST.get("dbname")
        dbname1 = request.POST.get("dbname1")
        applysql = request.POST.get("applysql")
        applysql2 = request.POST.get("applysql2")
        beizhu = request.POST.get("beizhu")
        title = request.POST.get("title")
        username = self.request.user.username
        applyuserId = User_Grpup.objects.filter(username=username)[0].id
        nowdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sqldate = request.POST.get("slqdate")
        sqlapp = sqlapply.objects.create(
                beizhu=beizhu,
                dbname=dbname,
                applyuserId=applyuserId,
                nowdate=nowdate,
                applysql=applysql,
                applydate=sqldate,
                title=title,
                applysql2=applysql2,
                dbname1=dbname1,
    )
        sqlapp.save()
        return redirect("/peppa")


#项目状态更新
class status(TemplateView):
    template_name="index.html"

    def get(self, request, *args, **kwargs):
        id=request.GET.get('id')
        status=request.GET.get('type')
        row = Apply.objects.get(id=id)
        project1 = row.project
        userid = row.applyuserId
        project = project_gitaddress.objects.get(project=project1).name
        #测试人
        testname = row.csleader

        #申请人名字
       # appname = User_Grpup.objects.filter(id=userid)[0].username
        #邮箱
        #mail_csname = User_Grpup.objects.get(username=testname).mail
       # mail_appname = User_Grpup.objects.get(username=appname).mail
       #  mail_yaocj = User_Grpup.objects.get(username='yaocj').mail
       #  mail_zhangsz = User_Grpup.objects.get(username='zhangsz').mail
        # 判断状态值发送邮件
        if status == "0":
            peppaapi.send_mail('您有新的审批', '%s发布需要dba审核' %(project), ['wangl@diandainfo.com'])
        if status == "1":
            peppaapi.send_mail('您有新的审批', '%s发布需要审核'   %(project), ['wangl@diandainfo.com'])
        if status == "2":
            peppaapi.send_mail('你有新的发布提醒', '%s可以发布了' %(project), ['wangl@diandainfo.com'])
        if status == "4":
            peppaapi.send_mail('你有新的测试任务', '%s可以测试了' %(project), ['wangl@diandainfo.com'])

        peppaapi.get_applystatus(id,status)
        return redirect('/peppa')


#sql状态更新
class sqlstatus(TemplateView):
    template_name="index.html"

    def get(self,request,*args,**kwargs):
        id=request.GET.get('id')
        status=request.GET.get('type')
        #如果type值为2（dba执行完成时），设置执行时间为version值
        peppaapi.get_sqlstatus(id,status)
        row = sqlapply.objects.get(id=id)
        title = row.title
        #mail_yaocj = User_Grpup.objects.get(username='yaocj').mail
        #mail_zhangsz = User_Grpup.objects.get(username='zhangsz').mail

        # 判断状态值发送邮件
        if status == "0":
            peppaapi.send_mail('您有新的sql审批', '%s申请sql上线需要dba审核' %(title), ['wangl@diandainfo.com'])
        if status == "1":
            peppaapi.send_mail('您有新的sql审批', '%s申请sql上线需要架构师审核' %(title), ['wangl@diandainfo.com'])
        return redirect('/peppa')


#项目详情展示
class projectDetail(TemplateView):

    template_name = "projectDetail.html"

    def get_context_data(self, **kwargs):
        context = super(projectDetail, self).get_context_data(**kwargs)
        tid = self.request.GET.get('id')
        env = Apply.objects.get(id=tid).applyEnv
     #   glo_env = self.request.session.get('env')

        res = peppaapi.get_applyproject(tid)

        if res[0]['dbname1']:
            context['flag'] = 1

        context['proinfo'] = res
        context['env'] = env
        return context

#sql详情展示
class sqlDetail(TemplateView):

    template_name="sqlproject.html"

    def get_context_data(self, **kwargs):
        tid = self.request.GET.get('id')
        context = super(sqlDetail, self).get_context_data(**kwargs)
        res=peppaapi.get_sqlproject(tid)
        if res[0]['sql2']:
            context['flag'] = 1
        else:
            context['flag'] = 0

        context['sqlinfo']=res
        return context

#项目存储
class applysave(TemplateView):

    template_name = "apply.html"

    def post(self, request, *args, **kwargs):
        project = request.POST.get('projectName')
        nowdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        repo = project_gitaddress.objects.filter(project=project)[0].gitaddress  ##git地址
        tags = request.POST.get('tagName')
        branchname = request.POST.get('branchname')
        projectname = project_gitaddress.objects.get(project=project).name
        print(projectname)
        print(branchname)
        #如果是生产环境的话，赋予branch一个默认值，使其不为空
        if  branchname:
            os.system('cd /tmp/peppa/%s/ && git checkout %s'%(projectname,branchname))
        else:
            branchname = "0"
        if tags:
            os.system('cd /tmp/peppa/%s/ && git checkout %s' % (projectname, tags))
        else:
            tags = "0"

        applyEnv = request.session.get('env')
        jsleader = request.POST.get('techOwner')
        csleader = request.POST.get('testOwner')
        cpleader = request.POST.get('projectOwner')
        appdate = request.POST.get('gaDate')
        applyconf = request.POST.get('applyconf')
        applysql = request.POST.get('applysql')
        note = request.POST.get('note')
        dbname = request.POST.get('dbname')
        dbname1 = request.POST.get('dbname1')
        applysql1 = request.POST.get('applysql1')
        username = self.request.user.username
        applyuserId = User_Grpup.objects.filter(username=username)[0].id

        if not dbname and not dbname1 and applyEnv == "pro":
            type = 1
        elif applyEnv == "pro":
            type = 0
        else:
            type = 2

        app_obj = Apply.objects.create(project=project,
                                       nowdate=nowdate,
                                       tags=tags,
                                       repertory=repo,
                                       jsleader=jsleader,
                                       csleader=csleader,
                                       cpleader=cpleader,
                                       applydate=appdate,
                                       applyconfig=applyconf,
                                       applysql=applysql,
                                       beizhu=note,
                                       applyuserId=applyuserId,
                                       dbname=dbname,
                                       dbname1=dbname1,
                                       applysql1=applysql1,
                                       type=type,
                                       branchname=branchname,
                                       applyEnv=applyEnv,
                                       )
        app_obj.save()
        return redirect("/peppa")


    def get_context_data(self, **kwargs):
        context = super(applysave, self).get_context_data(**kwargs)
        context['page_title'] = u'上线申请'
        return context

class project_release(TemplateView):
    template_name = 'releaseapp.html'

    def post(self, request, *args, **kwargs):
        machine = request.POST.getlist('check_box_list')
        project = request.POST.get('pro')


#发布状态存入到数据库
#发布
class release_status(TemplateView):
    template_name = 'index.html'


    def get(self,request,*args,**kwargs):
        id = request.GET.get('id')
        status = request.GET.get('type')
        peppaapi.get_applystatus(id, status)
        env = Apply.objects.get(id=id).applyEnv
        project1 = Apply.objects.get(id=id).project
        project = project_gitaddress.objects.get(project=project1).name
        # 生成版本号
        release_version = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        print('release_version = ',release_version)

        #从前端获取服务器列表
        machine = request.GET.getlist('check_box_list')
        #获取当前任务行，更改发布状态
        row = Apply.objects.get(id=id)
        print("准备开始发布")
        for i in machine:

            client2 = release.ParamikoClient()
            client2.connect('192.168.1.105')
            cmd = '/bin/bash /data/scripts/dianda_release/addhost.sh %s %s' %(project,i)
            client2.runcmd(cmd)
            client2.close_connect()
        # 获取操作标识，重启 发布 回滚
        print("host 已经配置好")
        operation = request.GET.get('operation')
        print("打印operation属性")
        print(operation)
        if operation == "release":
            # 把版本号存入数据库
            #peppaapi.save_version(id, release_version)
            row.version = release_version
            row.save()
            #推送git代码
            peppaapi.push_git(project, id)
            print(project,release_version,operation)
            #执行发布脚本
            try:
                cmd2 = '/bin/bash /data/scripts/dianda_release/diandarelease.sh %s %s %s' % (
                project, release_version, operation)
                client1 = release.ParamikoClient()
                client1.connect('192.168.1.105')
                client1.runcmd(cmd2)
                cmd3 = 'rm -f /root/Documents/Ddansible/release/prodution/hosts/%s.yml' % (project)
                client1.runcmd(cmd3)
                client1.close_connect()
                #执行成功后保存
                row.release_status = 3
                row.save()
                print("执行ansible一步")
            except Exception as e:
                row.release_status = 4
                row.save()
                print(e)
                print("执行ansible失败")

            #发布完成后延时2秒中，判断端口是否通
            time.sleep(15)
            print(machine)
            for i in machine:
                port = peppaapi.get_port(i,project)
                print(port)
                try:
                    sta = release_port.port_status(i,port)
                    print('发布状态码')
                    print(sta)
                    if sta == 0:
                        peppaapi.get_applystatus(id, 4)
                    else:
                        peppaapi.get_applystatus(id, 12)
                        print('发布失败1')
                except Exception as error:
                    peppaapi.get_applystatus(id, 12)
                    print('发布失败2')
            return redirect('/peppa/release_page?id=%s' %(id))

        if operation == "rollback":

            rollback_version=peppaapi.get_version(id)
            machine = peppaapi.get_machine(project, env)
            for i in machine:
                client2 = release.ParamikoClient()
                client2.connect('192.168.1.105')
                cmd = '/bin/bash /data/scripts/dianda_release/addhost.sh %s %s' % (project, i)
                client2.runcmd(cmd)
                client2.close_connect()

            #执行发布脚本
            cmd2 = '/bin/bash /data/scripts/dianda_release/diandarelease.sh %s %s %s' %(project,rollback_version,operation)
            cmd3 = 'rm -f /root/Documents/Ddansible/release/prodution/hosts/%s.yml' %(project)
            client1 = release.ParamikoClient()
            client1.connect('192.168.1.105')
            client1.runcmd(cmd2)
            client1.runcmd(cmd3)
            client1.close_connect()
            time.sleep(15)
            for i in machine:
                port = peppaapi.get_port(i, project)
                print(port)
                try:
                    sta = release_port.port_status(i,port)
                    print('回滚状态码')
                    print(sta)
                    if sta == 0:
                        peppaapi.get_applystatus(id, 11)
                    else:
                        peppaapi.get_applystatus(id, 13)
                except Exception as error:

                    peppaapi.get_applystatus(id, 13)
            return redirect('/peppa/version')

# #验证发布是否成功
# class confirm(TemplateView):
#
#     template_name = "releaseapp.html"
#
#     def get(self, request, *args, **kwargs):
#         tid = request.GET.get('id')
#         print(tid)
#         env = Apply.objects.get(id=tid).applyEnv
#         project1 = Apply.objects.get(id=tid).project
#         project = project_gitaddress.objects.get(project=project1).name
#         #从前端获取服务器列表
#         machine = peppaapi.get_machine(project, env)
#
#         #获取当前任务行，更改发布状态
#         print(machine)
#         try:
#             for i in machine:
#                 port = peppaapi.get_port(i, project)
#                 print(port)
#              #   status1 = tests.testconn(i, port)
#                 status = os.popen('curl -I -m 10 -o /dev/null -s -w %%{http_code} http://%s:%s' % (i, port)).read()
#                 status1 = int(status)
#                 print(status1)
#                 print(type(status1))
#                 if status1 < 400:
#                     peppaapi.get_applystatus(tid, 4)
#                 else:
#                     peppaapi.get_applystatus(tid, 12)
#
#         except Exception as error:
#                 peppaapi.get_applystatus(tid, 12)
#
#         return redirect('/peppa')
#历史版本
class version(TemplateView):
    template_name = 'version.html'

    def get_context_data(self, **kwargs):
        context = super(version, self).get_context_data(**kwargs)
        context['page_title'] = '版本列表'
        nowdate = datetime.datetime.now().strftime("%Y-%m-%d")
        context['nowdate'] = nowdate
        global_env = self.request.session.get('env')
        plantime = self.request.GET.get('release_plan')
        context['glo_env'] = global_env
        #筛选查询sql发布或者项目版本发布版本历史消息
        verpro=self.request.GET.get('project')
        if verpro == "proapply":
          #根据环境变量查结果
            verdetail = Apply.objects.filter(applyEnv=global_env).order_by('-id')

            verresult = []
            if plantime:
                verdetail1 = Apply.objects.filter(applyEnv=global_env)
                verdetail = verdetail1.filter(applydate=plantime).order_by('-id')
                for i in verdetail:

                    verresult.append({
                        'id': i.id,
                        'project': i.project,
                        'tags': i.tags,
                        'version': i.version,
                        'applyuser': peppaapi.get_applyuser(i.applyuserId),
                        'status': i.get_status_display,
                        'applydate': i.applydate,
                        'cjdate': i.nowdate,
                        'branchname': i.branchname
                    })
            else:
                verdetail = Apply.objects.all().order_by('-id')
                for i in verdetail:
                    verresult.append({
                        'id': i.id,
                        'project': i.project,
                        'version': i.version,
                        'tags': i.tags,
                        'applyuser': peppaapi.get_applyuser(i.applyuserId),
                        'status': i.get_status_display,
                        'applydate':i.applydate,
                        'cjdate':i.nowdate
                    })
            context['vertype'] = "project"
            context['verdetail'] = verresult

        if verpro == "appsql":
            versqldetail=sqlapply.objects.all().order_by('-id')
            verdetail=[]
            if plantime:
                versqldetail = sqlapply.objects.all().filter(applydate=plantime).order_by('-id')
                for i in versqldetail:
                    verdetail.append({
                        'id':i.id,
                        'project': i.title,
                        'version': i.version,
                        'applyuser': peppaapi.get_applyuser(i.applyuserId),
                        'status': i.get_status_display,
                        'applydate':i.applydate,
                        'cjdate':i.nowdate
                    })
            else:
                for i in versqldetail:
                    verdetail.append({
                        'id':i.id,
                        'project': i.title,
                        'version': i.version,
                        'applyuser': peppaapi.get_applyuser(i.applyuserId),
                        'status': i.get_status_display,
                        'applydate': i.applydate,
                        'cjdate': i.nowdate
                    })
            context['vertype'] = "sql"
            context['verdetail'] = verdetail
        return context

def query_verinfo(request):
    txt = os.popen('cat /tmp/sms_service')
    line = len(open('/tmp/sms_service', 'rU').readlines())
    wu = os.popen("sed -n '3,$p' /tmp/sms_service \n")
    return render(request,'releaseapp.html', {'log':wu.read()})

class release_page(TemplateView):
    template_name = 'releaseapp.html'

    def get_context_data(self, **kwargs):
        context = super(release_page, self).get_context_data(**kwargs)
        tid=self.request.GET.get('id')
        #根据id查询 Apply 表中project以及机器
        project = peppaapi.get_project(tid)
        #根据项目查询对应的机器
        project_name = peppaapi.get_project_name(project)
        #根据id获取环境变量
#        release_env = Apply.objects.get(id=tid).applyEnv
        release_env = self.request.session.get('env')

        machine=peppaapi.get_machine(project_name, release_env)
        resultma=[]
        for i in machine:
            resultma.append({
                'machine': i
            }
            )
        row = Apply.objects.get(id=tid)

        test = row.release_status
        context['status'] = test
        context['machine'] = machine
        context['project'] = project
        context['tid'] = tid
        return context

def releStatu(request):

    tid = request.GET.get("id")
    row = Apply.objects.get(id=tid)
    resleaseSt = row.release_status
    resStatus = row.get_release_status_display()
    a={}
    a["result"] = resleaseSt
    a["resStatus"] = resStatus
    return HttpResponse(json.dumps(a), content_type='application/json')

class upload(TemplateView):

    template_name = 'releaseapp.html'

def test(request):
    if request.GET['name'] =='tagName':
        tagName = request.GET['value']
        gitadd = project_gitaddress.objects.filter(project=tagName)[0].gitaddress
        print('gitadd = '+gitadd)
        git_tag(tagName,gitadd)
        return HttpResponse(json.dumps(tags))
    if request.GET['name'] == 'projectName':
        username = request.user.username
        group=User_Grpup.objects.filter(username=username)[0].role
        ##获取项目对象
        project = []
        if group == 'yunwei':
            obj = Grpup_update_project.objects.all()
            print(obj)
        else:
            obj = Grpup_update_project.objects.filter(role=group)
        for i in range(len(obj)):
            project.append(obj[i].update_project)
        ##project是获取到的项目传到前端然后选tag

        print(project)

        return HttpResponse(json.dumps(project))
    if request.GET['name'] == 'branchname':
        tagName = request.GET['value']
        branchname = request.GET['value']
        gitadd = project_gitaddress.objects.filter(project=tagName)[0].gitaddress
        git_branch(branchname,gitadd)
        return HttpResponse(json.dumps(branch))



def git_tag(projectname,gitaddress):
    global tags
    filename = project_gitaddress.objects.filter(project=projectname)[0].name
    tags = []
    fabu_path = '/tmp/peppa/'
    if os.path.exists('/tmp/peppa/'):
        print('True')
    else:
        print('false')
        os.system('mkdir /tmp/peppa/')
    if os.path.exists(fabu_path+filename):
        print('项目[%s]本地缓存  存在'%filename)
        os.system('cd %s && git pull %s' % (fabu_path, gitaddress))
    else:
        print('项目[%s]本地缓存 不存在'%filename)
        os.system('cd %s && git clone %s' % (fabu_path, gitaddress))
    dizhi = 'cd %s && cd %s && git tag > 1.txt' % (fabu_path,filename)
    os.system(dizhi)
    f = open('%s%s/1.txt' % (fabu_path,filename), 'r')
    os.system('rm -fr %s%s/1.txt' % (fabu_path,filename))
    xx = f.read()
    x = len(str(xx).split('\n'))
    for i in range(x -1):
        tags.append(xx.split('\n')[i])
    tags.reverse()##倒序
    f.close()


def git_branch(projectname,gitaddress):
    global branch
    filename = project_gitaddress.objects.filter(project=projectname)[0].name
    branch = []
    fabu_path = '/tmp/peppa/'
    if os.path.exists('/tmp/peppa/'):
        print('True')
    else:
        print('false')
        os.system('mkdir /tmp/peppa/')
    if os.path.exists(fabu_path+filename):
        print('项目[%s]本地缓存  存在'%filename)
        os.system('cd %s && git pull %s' % (fabu_path, gitaddress))
    else:
        print('项目[%s]本地缓存 不存在'%filename)
        os.system('cd %s && git clone %s' % (fabu_path, gitaddress))
    dizhi = 'cd %s && cd %s && git branch -r > branch.txt' % (fabu_path,filename)
    os.system(dizhi)
    f = open('%s%s/branch.txt' % (fabu_path,filename), 'r')
    xx = f.read()
    os.system('rm -fr %s%s/branch.txt' % (fabu_path,filename))
    x = len(str(xx).split('\n'))
    for i in range(x -1):
        branch.append(xx.split('\n')[i].split('/')[1])
        branch.reverse()##倒序
    print(branch)
    f.close()


#动态加载环境变量
def select_env(request):
    #默认给测试环境
    env_global = request.GET.get('env')
    request.session['env'] = env_global
    env22 = request.session.get('env')
    a={}
    a['envselect'] = env22

    return HttpResponse(json.dumps(a), content_type='application/json')
