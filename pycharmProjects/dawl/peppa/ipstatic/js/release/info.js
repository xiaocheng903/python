;
var release_info_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".del").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"del"
            };
            that.ops( "确定废弃，废弃之后不可恢复？",data )
        });

        $(".reback").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"reback"
            };
            that.ops( "确定回退到待集测？",data )
        });

        $(".test_ok").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"test_ok"
            };
            that.ops( "确定集测测试通过？",data )
        });

        $(".test_fail").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"test_fail"
            };
            that.ops( "确定集测测试不通过？",data )
        });

        $(".dba_ok").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"dba_ok"
            };
            that.ops( "确定所有SQL已完成？",data )
        });

        $(".gray_publish").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"gray_publish"
            };
            that.ops( "确定灰度已发布完成？",data )
        });


        $(".gray_ok").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"gray_ok"
            };
            that.ops( "确定灰度验证通过？",data )
        });

        $(".gray_fail").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"gray_fail"
            };
            that.ops( "确定灰度验证不通过？",data )
        });

        $(".ga_publish").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"ga_publish"
            };
            that.ops( "确定生产GA已发布完成？",data )
        });


        $(".ga_ok").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"ga_ok"
            };
            that.ops( "确定生产GA验证通过？",data )
        });


        $(".merge_master").click( function(){
            var data = {
                act:"merge",
                branch:"master",
                actType:"merge_master"
            };
            that.ops( "确定要合入Master？",data )
        });

        $(".master_merge").click( function(){
            var data = {
                act:"merge",
                branch:"master",
                actType:"master_merge"
            };
            that.ops( "确定要合并Master？",data )
        });

        $(".publish_fail").click( function(){
            var data = {
                act:"publish_fail",
                id: $(this).attr("data") ,
                projectId:$(".hidden_wrap input[name=id]").val()
            };
            that.publishOps( "确定要标记此包上线失败？<br/>此功能一般用于发布之后发现有问题需回滚之后<br/>标记这个包上线失败了",data )
        });

        $(".check_network").click( function(){
            $.ajax({
                url:common_ops.buildUrl("/release/check-network"),
                success:function( res ){
                    var data = res.data;
                    if( data && data.length > 0 ){
                        laytpl( $("#check_network_template").html()  ).render(res.data, function(result){
                            $("#check_network_modal .modal-body").html( result );
                            $("#check_network_modal").modal();
                        });
                    }else{
                        common_ops.alert( res.msg );
                    }
                }
            });
        } );

        $(".auto_test").click( function(){
            $("#modal_auto_test").modal();
        });

        $("#modal_auto_test .ok").click( function(){
            var server_ip = $("#modal_auto_test select[name=auto_server]").val();
            if( server_ip == "0" ){
                common_ops.alert( "请选择要进行自动化测试的服务器~~" );
                return;
            }

            var data = {
                "id":$(".hidden_wrap input[name=id]").val(),
                "serverIp":server_ip
            };


            var callback = {
                'ok':function(){
                    $.ajax({
                        url:common_ops.buildUrl("/release/autotest"),
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
            common_ops.confirm( "确定要进行自动化测试?" ,callback );
        } );

        $('#myTabs a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        });

        //自测环境加入申请测试机器的过程
        $(".my_test").click(function () {
            $("#my_test_modal").modal();
        });

        $("#my_test_modal .save").click( function(){
            var test_server_id = $("#my_test_modal select[name=test_server]").val();
            if( test_server_id == undefined || parseInt( test_server_id ) < 1 ){
                common_ops.alert( "请选择测试服务器用于集测~~" );
                return;
            }

            var test_server_ip = $("#my_test_modal select[name=test_server]").find("option:selected").text();
            var data = {
                "act" : "my_test",
                "status":1,
                "test_server_id" :  test_server_id,
                "test_server_ip" : test_server_ip
            }
            that.ops("确定要申请服务器进行集测？", data);
        } );


    },
    ops:function( msg ,data){
        data['id'] = $(".hidden_wrap input[name=id]").val();
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/release/ops"),
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
    publishOps:function( msg ,data ){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/release/publish_ops"),
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
    }
};

$(document).ready( function(){
    release_info_ops.init();
});