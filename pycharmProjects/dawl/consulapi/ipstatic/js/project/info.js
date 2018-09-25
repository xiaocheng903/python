 ;
var project_info_ops = {
    init:function(){
        this.eventBind();
        $( $("#myTabs li a").get(2) ).click();
    },
    mergeRelease: function (data) {
        if (!data) {
            data = {};
        }
        data["id"] = $(".hidden_wrap input[name=id]").val();
        $.ajax({
            url:common_ops.buildUrl( "/project/merge_release" ),
            type:"POST",
            data:data,
            dataType:'json',
            success:function( res ){
                if( res.code != 200 ){
                    if (res.code == 100001) {
                        common_ops.confirm(res.msg + ", 强制合并?", {"ok":function () {
                                project_info_ops.mergeRelease({"force": true});
                            }})
                    } else {
                        common_ops.alert(res.msg);
                    }
                    return;
                }

                laytpl($("#merge_release_template").html()).render(res.data, function(result){
                    $("#model_merge_release .modal-body").html( result );
                    $("#model_merge_release").modal();
                });
            }
        });
    },
    eventBind:function(){
        var that = this;
        $(".del").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"del"
            };
            that.ops( "确定删除，删除之后不可恢复？",data )
        });

        $(".test_ok").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"test_ok"
            };
            that.ops( "确定测试通过？",data )
        });

        $(".test_fail").click( function(){
            $("#test_fail_model").modal();
        });

        $(".reback").click( function(){
            var data = {
                status:$(this).attr("data"),
                act:"reback"
            };
            that.ops( "确定回退到开发阶段？",data )
        });

        $(".merge_branch").click( function(){
            $("#model_merge_branch input[name=branchName]").val( "master" );
            $("#model_merge_branch").modal();
        });

        $("#model_merge_branch .merge_branch_ok").click( function(){
            var branchName = $.trim( $("#model_merge_branch input[name=branchName]").val() );

            if( branchName == undefined || branchName.length < 1 ){
                common_ops.alert("请输入要合并的分支名称~~,分支名称，只能是master或者其他dev分支" );
                return;
            }

            // if( branchName != "master"  && branchName.indexOf( "dev_" ) < 0 ){
            //     common_ops.alert("请输入要合并的分支名称~~,分支名称，只能是master或者其他dev分支");
            //     return;
            // }

            var data = {
                act:"merge",
                branch:branchName,
                releaseId:0
            };
            that.ops( "确定与"+branchName+"进行合并？",data )
        });

        $(".model_merge_release").click( function(){
            project_info_ops.mergeRelease();
        });

        $("#model_merge_release .merge_release_ok").click( function(){


            if( $("#model_merge_release input[name=releaseId]:checked").length < 1 ){
                common_ops.alert( "请选择要合并的版本的~~" );
                return;
            }

            var releaseId = $("#model_merge_release input[name=releaseId]:checked").val();
            var branchName = $("#model_merge_release input[name=releaseId]:checked").attr("data-name");
            var data = {
                "act":"merge",
                "status":$(this).attr("data"),
                "releaseId":releaseId,
                "branch":branchName
            };
            that.ops( "确定合入，合并之后不可撤回？",data )

        });

        $(".develop_ok_model").click( function(){

            var status = parseInt( $(this).attr("project_status") );

            if ( status == 4 ){
                $("#develop_ok_model").modal();
                return;
            }


            $.ajax({
                url:common_ops.buildUrl("/project/check_need_review"),
                type:'POST',
                data:{
                    id:$(".hidden_wrap input[name=id]").val()
                },
                dataType:'json',
                success:function( res ){
                    var callback = null;
                    if( res.code == 200 ){

                        if( parseInt( res.data.need_review ) == 1 ){
                            callback = function(){
                                $("#model_design").modal();
                            }
                            common_ops.alert( res.msg,callback );
                        }else{
                            $("#develop_ok_model").modal();
                        }

                    }else{
                        common_ops.alert( res.msg );
                    }
                }
            });

        });

        $(".develop_ok").click( function(){

            var packageIds = [];
            var note = $("#develop_ok_model textarea[name=note]").val();
            $("#develop_ok_model input[name='packeage[]']:checked").each( function(){
                packageIds.push( $(this).val() );
            });

            if( packageIds.length < 1 ){
                common_ops.alert( "请选择此次项目涉及的包~~" );
                return;
            }

            if( note.length < 10 ){
                common_ops.alert( "请输入提测描述内容~~" );
                return;
            }

            var data = {
                "act":"develop_ok",
                "status":$(this).attr("data"),
                "packageIds":packageIds,
                "description":note
            };
            that.ops( "确定提测？<br/>提测前请务必记住填写上线资料（如果有）",data )
        });

        $("#test_fail_model .test_fail").click( function(){
            var note = $("#test_fail_model textarea[name=note]").val();

            if( note.length < 10 ){
                common_ops.alert( "请输入提测详细的驳回原因~~" );
                return;
            }

            var data = {
                status:$(this).attr("data"),
                act:"test_fail",
                rejectNote:note
            };
            that.ops( "确定测试不通过？",data )
        });

        $('#myTabs a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        })



        $(".design_ok").click(function(){

            var design_url = $("#model_design input[name='design_url']").val();

            if( design_url.length < 1
                || design_url.indexOf( "git.mogo.com/tech/doc" ) < 0 ){
                common_ops.alert( "请输入设计文档地址，并且设计文档必须放在 <a target='_blank' href='http://git.mogo.com/tech/doc'>http://git.mogo.com/tech/doc</a> " );
                return;
            }

            var data = {
                "act":"design_ok",
                "status":$(this).attr("data"),
                "designUrl":design_url
            }

            that.ops( "确定提交设计方案？",data )
        });

        $(".design_review_ok").click(function () {
            var data = {
                "act" : "design_review_ok",
                "status":4
            }

            that.ops("确定设计评审通过？", data)
        });

        $(".design_review_fail").click(function () {
            $("#design_review_fail_model").modal();
        });


        $("#design_review_fail_model .design_review_fail").click(function () {
            var data = {
                "act" : "design_review_fail",
                "status" : 2,
                "rejectNote" :  $("#design_review_fail_model textarea[name=note]").val()
            }
            that.ops("确定设计评审驳回？", data);
        })

        //自测环境加入申请测试机器的过程
        $(".my_test").click(function () {
            $("#my_test_modal").modal();
        });

        $("#my_test_modal .save").click( function(){
            var test_server_id = $("#my_test_modal select[name=test_server]").val();
            if( test_server_id == undefined || parseInt( test_server_id ) < 1 ){
                common_ops.alert( "请选择测试服务器用于自测~~" );
                return;
            }

            var test_server_ip = $("#my_test_modal select[name=test_server]").find("option:selected").text();
            var data = {
                "act" : "my_test",
                "status" : 2,
                "test_server_id" :  test_server_id,
                "test_server_ip" : test_server_ip
            }
            that.ops("确定要进入自测阶段？", data);
        } );

        $("#runUtBtn").click(function() {
            var data = {
                "act" : "run_ut",
                "status" : -1
            };
            that.ops("确定要进行ut覆盖率测试？", data);
        });
    },
    ops:function( msg ,data){
        data['id'] = $(".hidden_wrap input[name=id]").val();
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/project/ops"),
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
    project_info_ops.init();
});