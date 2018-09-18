;
var project_task_set_ops = {
    init:function(){
        this.eventBind();
        this.init_apollo();
    },
    eventBind:function(){

        var that = this;

        $("#project_task_sql_wrap .save").click( function(){

            var title_target = $("#project_task_sql_wrap input[name=title]");
            var title = title_target.val();

            var sqlType_target = $("#project_task_sql_wrap select[name=sqlType]");
            var sqlType = sqlType_target.val();

            var content_target = $("#project_task_sql_wrap textarea[name=content]");
            var content = content_target.val();

            if( title.length < 1  ){
                common_ops.tip( "请输入SQL脚本标题~~",title_target );
                return;
            }

            if( sqlType < 1 ){
                common_ops.tip( "请选择类型~~",sqlType_target );
                return;
            }

            if( content.length < 10  ){
                common_ops.tip( "请输入SQL脚本具体描述~~",content_target );
                return;
            }

            var data = {
                "itemId":$("#project_task_sql_wrap input[name=itemId]").val(),
                "title":title,
                "sqlType":sqlType,
                "detail":content,
                "type":1
            };

            that.submit( $(this),data );

        });

        $("#project_task_job_wrap .save").click( function(){

            var jobTitle_target = $("#project_task_job_wrap input[name=jobTitle]");
            var jobTitle = jobTitle_target.val();

            var jobClassName_target = $("#project_task_job_wrap input[name=jobClassName]");
            var jobClassName = jobClassName_target.val();


            var jobParam_target = $("#project_task_job_wrap input[name=jobParam]");
            var jobParam = jobParam_target.val();

            var jobBiz_target = $("#project_task_job_wrap select[name=jobBiz]");
            var jobBiz = jobBiz_target.val();


            var jobType_target = $("#project_task_job_wrap select[name=jobType]");
            var jobType = jobType_target.val();

            var jobRuntime_target = $("#project_task_job_wrap input[name=jobRuntime]");
            var jobRuntime = jobRuntime_target.val();

            var description_target = $("#project_task_job_wrap textarea[name=description]");
            var description = description_target.val();

            if( jobTitle.length < 1  ){
                common_ops.tip( "请输入定时器的名称~~",jobTitle_target );
                return;
            }

            if( jobClassName.length < 2 ){
                common_ops.tip( "请输入定时器的类名称,切记为完整包名~~",jobClassName_target );
                return;
            }

            if( jobParam.length < 1  ){
                common_ops.tip( "请输入定时器的参数~~",jobParam_target );
                return;
            }

            if( jobBiz < 1  ){
                common_ops.tip( "请选择任务所属类型~~",jobBiz_target );
                return;
            }



            if( jobType < 1  ){
                common_ops.tip( "请选择任务类型~~",jobType_target );
                return;
            }

            if( jobType > 1 && jobRuntime.length < 2 ){
                common_ops.tip( "请输入定时器的运行时间~~",jobRuntime_target );
                return;
            }


            if( description.length < 10  ){
                common_ops.tip( "亲，多写点描述哇，为业务做备注啦，至少10个字符~~",description_target );
                return;
            }

            var data = {
                "itemId":$("#project_task_job_wrap input[name=itemId]").val(),
                "jobTitle":jobTitle,
                "jobClassName":jobClassName,
                "jobParam":jobParam,
                "jobBiz":jobBiz,
                "jobType":jobType,
                "jobRuntime":jobRuntime,
                "description":description,
                "type":2
            };

            that.submit( $(this),data );

        });

        $("#project_task_config_wrap .save").click( function(){

            var bizId_target = $("#project_task_config_wrap select[name=bizId]");
            var bizId = bizId_target.val();

            var act_target = $("#project_task_config_wrap select[name=act]");
            var act = act_target.val();

            var env_target = $("#project_task_config_wrap select[name=env]");
            var env = env_target.val();

            var fileName_target = $("#project_task_config_wrap input[name=fileName]");
            var fileName = fileName_target.val();

            var detail_target = $("#project_task_config_wrap textarea[name=detail]");
            var detail = detail_target.val();

            var description_target = $("#project_task_config_wrap input[name=description]");
            var description = description_target.val();

            if( bizId < 1  ){
                common_ops.tip( "请选择所属业务~~",bizId_target );
                return;
            }

            if( act < 1 ){
                common_ops.tip( "请选择操作类型~~",act_target );
                return;
            }

            if( env < 1  ){
                common_ops.tip( "请选择操作环境~~",env_target );
                return;
            }

            if( fileName.length < 2 ){
                common_ops.tip( "请输入配置文件名~~",fileName_target );
                return;
            }

            if( detail.length < 1  ){
                common_ops.tip( "请输入配置内容~~",detail_target );
                return;
            }

            if( description.length < 5  ){
                common_ops.tip( "亲，多写点描述哇，为业务做备注啦，至少5个字符~~",description_target );
                return;
            }

            var data = {
                "itemId":$("#project_task_config_wrap input[name=itemId]").val(),
                "bizId":bizId,
                "act":act,
                "env":env,
                "fileName":fileName,
                "detail":detail,
                "description":description,
                "type":3
            };

            that.submit( $(this),data );

        });

        $("#project_task_apollo_wrap select[name=env]").SumoSelect({
            csvDispCount: 10,
            selectAll: true,
            placeholder: '请选择操作环境',
            floatWidth: 400
        });

        $("#project_task_apollo_wrap select[name=appid]").change( function(){
            that.getApollo( $(this).val(), "" );
        } );
        
        $("#project_task_apollo_wrap .save").click( function () {

            var appid_target = $("#project_task_apollo_wrap select[name=appid]");
            var appid = appid_target.val();

            var namespace_target = $("#project_task_apollo_wrap select[name=namespace]");
            var namespace = namespace_target.val();

            var act_target = $("#project_task_apollo_wrap select[name=act]");
            var act = act_target.val();

            var apollo_key_target = $("#project_task_apollo_wrap input[name=apollo_key]");
            var apollo_key = apollo_key_target.val();

            var apollo_value_target = $("#project_task_apollo_wrap input[name=apollo_value]");
            var apollo_value = apollo_value_target.val();

            var description_target = $("#project_task_apollo_wrap input[name=description]");
            var description = description_target.val();


            var env = [];

            if( appid.length < 1  ){
                common_ops.tip( "请选择配置标示~~",appid_target );
                return;
            }

            if( $("#project_task_apollo_wrap select[name=env] option:selected").length < 1 ){
                common_ops.alert( "请选择操作环境~~" );
                return;
            }

            $("#project_task_apollo_wrap select[name=env] option:selected").each( function() {
                env.push( $(this).val() );
            });

            if( namespace.length < 1 ){
                common_ops.tip( "请选择命令空间~~",namespace_target );
                return;
            }

            if( act < 1 ){
                common_ops.tip( "请选择操作类型~~",act_target );
                return;
            }

            if( apollo_key.length < 1  ){
                common_ops.tip( "请输入配置Key名称~~",apollo_key_target );
                return;
            }

            if( apollo_value.length < 1  ){
                common_ops.tip( "请输入配置值~~",apollo_value_target );
                return;
            }


            if( description.length < 1  ){
                common_ops.tip( "请输入配置描述~~",description_target );
                return;
            }


            if( description.length < 5  ){
                common_ops.tip( "亲，多写点描述哇，为业务做备注啦，至少5个字符~~",description_target );
                return;
            }

            var data = {
                "itemId":$("#project_task_apollo_wrap input[name=itemId]").val(),
                "appid":appid,
                "envIds":env,
                "namespace":namespace,
                "act":act,
                "apollo_key":apollo_key,
                "apollo_value":apollo_value,
                "description":description,
                "type":4
            };
            that.submit( $(this),data );
        } );
        
    },
    submit:function( btn_target,data ){

        if( btn_target.hasClass("disabled") ){
            common_ops.alert("正在处理!!请不要重复提交~~");
            return;
        }

        btn_target.addClass("disabled");

        var project_id = $(".hidden_wrap input[name=projectId]").val();
        data['projectId'] = project_id;

        $.ajax({
            url:common_ops.buildUrl("/project/task_doset") ,
            type:'POST',
            data: data,
            dataType:'json',
            success:function(res){
                btn_target.removeClass("disabled");
                var callback = null;
                if( res.code == 200 ){
                    callback = function(){
                        window.location.href = common_ops.buildUrl("/project/task",{ "id":project_id });
                    }
                }
                common_ops.alert( res.msg,callback );
            }
        });
    },
    init_apollo:function(){
       var appid =  $("#project_task_apollo_wrap select[name=appid]").val();
       if( appid.length > 0 ){
           this.getApollo( appid,$("#project_task_apollo_wrap select[name=namespace]").attr("data_select") )
       }
    },
    getApollo:function( appid,default_namespace ){
        if( appid.length < 1 ){
            return;
        }
        $.ajax({
            url:common_ops.buildUrl("/apollo/namespace") ,
            type:'POST',
            data: {
                "appid":appid
            },
            dataType:'json',
            success:function(res){
                if( res.code != 200 ){
                    common_ops.alert( res.msg );
                }

                var data = res.data;
                var items = data['items'];
                if(  items.length < 1  ){
                    common_ops.alert( "该Appid下面下没有namespace" );
                }

                tmp_str = "<option value=''>请选择命名空间</option>";
                for(  item_n in items ){
                    tmp_str += "<option value='" + items[ item_n ] + "'>" + items[ item_n ] + "</option>";
                }
                $("#project_task_apollo_wrap select[name=namespace]").html( tmp_str );

                if( default_namespace.length > 0 ){
                    $("#project_task_apollo_wrap select[name=namespace]").val( default_namespace );
                }

            }
        });
    }
};

$( document ).ready( function(){
    project_task_set_ops.init();
} );