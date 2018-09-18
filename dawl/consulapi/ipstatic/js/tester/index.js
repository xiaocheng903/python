;
var tester_index_ops = {
    init:function(){
        this.eventBind();
        this.datetimepickerComponent();
    },
    eventBind:function(){
        var that = this;
        $(".reback").click( function(){
            var data = {
                id:$(this).attr("data"),
                act:"reback"
            };
            that.ops( "确定释放服务器嘛？",data );
        });

        $(".apply").click( function(){

            $("#model_apply input[name=id]").val( $(this).attr("data") );
            $("#model_apply").modal();

        });

        $(".publish").click( function(){
            $("#model_publish_env input[name=id]").val( $(this).attr("data") );
            $("#model_publish_env .hostIp").html( $(this).attr("dataIp") );
            $("#model_publish_env input[name=branchName]").val( $(this).attr("dataBranchName") );
            $("#model_publish_env").modal();
        });

        $(".restartEnv").click( function(){
            $("#model_restart_env input[name=id]").val( $(this).attr("data") );
            $("#model_restart_env .hostIp").html( $(this).attr("dataIp") );
            $("#model_restart_env input[name=branchName]").val( $(this).attr("dataBranchName") );
            $("#model_restart_env").modal();
        });

        $("#model_publish_env input[name=packageUrl]").bind("input",function(){
            var url = $(this).val();
            if( url == undefined || url.length < 1 ){
                return;
            }

            var url_arr = url.split("/");
            var branch_name = "";
            if( url_arr.length == 8 ){
                branch_name = url_arr[5];
            }
            if( branch_name.length > 1  ){
                $('#model_publish_env input[name=branchName]').val( branch_name );
            }
        });

        $("#model_publish_env .save").click( function(){

            var packageUrl = $('#model_publish_env input[name=packageUrl]').val();
            var branchName = $('#model_publish_env input[name=branchName]').val();

            if( packageUrl == undefined || packageUrl.length < 1 ){
                common_ops.alert( "请输入Jenkins包地址Url~~" );
                return;
            }

            if( branchName == undefined || branchName.length < 1 ){
                common_ops.alert( "请输入配置分支名称~~" );
                return;
            }

            if( branchName == "test_config"){
                common_ops.alert( "禁止使用test_config分支进行测试~~" );
                return;
            }

            var data = {
                packageUrl:packageUrl,
                branchName:branchName,
                id: $("#model_publish_env input[name=id]").val(),
                act:"publish"
            };
            that.ops( "确定发布到组内测试环境嘛？",data );

        });

        $("#model_restart_env .save").click( function(){

            var projectName = $('#model_restart_env select[name=projectName]').val();
            var refreshConfigFlag = $('#model_restart_env input[name=refreshConfigFlag]:checked').val();
            var branchName = $('#model_restart_env input[name=branchName]').val();

            if( projectName == "0" ){
                common_ops.alert( "请选择操作项目名称~~" );
                return;
            }

            if( refreshConfigFlag == "1" ){
                if( branchName == undefined || branchName.length < 1 ){
                    common_ops.alert( "请输入配置分支名称~~" );
                    return;
                }
            }else{
                refreshConfigFlag = 0;
            }

            var data = {
                projectName:projectName,
                refreshConfigFlag:refreshConfigFlag,
                branchName:branchName,
                id: $("#model_restart_env input[name=id]").val(),
                act:"restart_env"
            };
            that.ops( "确定重启组内测试环境嘛？",data );

        });

        $("#model_apply .save").click( function(){

            var validTo = $('#model_apply input[name=validTo]').val();
            var validFrom = (new Date()).Format("yyyy-MM-dd");
            var diff = common_ops.datedifference( validFrom,validTo );
            if( diff > 100 ){
                common_ops.alert( "最长申请使用天数不能超过100天~~" );
                return;
            }
            var data = {
                validTo:validTo,
                id: $("#model_apply input[name=id]").val(),
                act:"apply"
            };
            that.ops( "确定申请嘛？",data );
        });

    },
    ops:function( msg ,data){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/test/env/ops"),
                    type:'POST',
                    data:data,
                    dataType:'json',
                    success:function( res ){
                        var callback = null;
                        if( res.code == 200 ){
                            callback = function(){
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert( res.msg,callback );
                    }
                });
            },
            'cancel':null
        };
        common_ops.confirm( msg ,callback );
    },
    datetimepickerComponent:function() {
        $.datetimepicker.setLocale('zh');
        params = {
            scrollInput: false,
            scrollMonth: false,
            scrollTime: false,
            dayOfWeekStart: 1,
            lang: 'zh',
            todayButton: true,//回到今天
            defaultSelect: true,
            defaultDate: new Date().Format('yyyy-MM-dd'),
            format: 'Y-m-d',//格式化显示
            timepicker: false
        };
        $('#model_apply input[name=validTo]').datetimepicker( params );
    }
};

$(document).ready( function(){
    tester_index_ops.init();
});