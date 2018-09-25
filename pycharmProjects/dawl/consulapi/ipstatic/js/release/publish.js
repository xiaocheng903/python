;
var release_publish_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".upload").click( function(){
            that.ops( $(this).attr("data-projectId"),$(this).attr("data"),"确定上传？","upload" )
        });

        $(".gray").click( function(){
            that.ops( $(this).attr("data-projectId"),$(this).attr("data"),"确定发灰度？","gray" )
        });

        $(".production").click( function(){
            var msg = $.trim( $(this).text() );
            that.ops( $(this).attr("data-projectId"),$(this).attr("data"),"确定" + msg +"？","production" )
        });

        $(".switch_weight").click( function(){
            var msg = $.trim( $(this).text() );
            that.ops( $(this).attr("data-projectId"),$(this).attr("data"),"确定" + msg +"？<br/>目前只支持切换全部流量","switch_weight" )
        });


        $(".rollback_production").click( function(){
            var that = this;
            $.ajax({
                url:common_ops.buildUrl("/release/get_last_version"),
                type:'POST',
                data:{
                    packageId:$(that).attr("data-packageId")
                },
                dataType:'json',
                success:function( res ){

                    if( res.code != 200 ){
                        common_ops.alert( res.msg );
                        return;
                    }

                    var res_data = res.data;

                    $("#modal_rollback select[name=rollback_version]").empty();
                    $("#modal_rollback select[name=rollback_version]").append("<option value='0'>请选择回滚版本</option>");
                    for( var idx in res_data ){
                        tmp_option = "<option value='" + res_data[idx]['ver'] + "'>" + res_data[idx]['branchName'] + "【版本号" + res_data[idx]['ver']  +"】</option>";
                        $("#modal_rollback select[name=rollback_version]").append( tmp_option );
                    }

                    $("#modal_rollback input[name=act]").val( "rollback_production" );
                    $("#modal_rollback input[name=itemId]").val( $(that).attr("data") );
                    $("#modal_rollback input[name=projectId]").val( $(that).attr("data-projectId") );
                    $("#modal_rollback").modal();
                }
            });

        } );

        $("#modal_rollback .save").click( function(){
            var version =  $("#modal_rollback select[name=rollback_version]").val();
            var act = $("#modal_rollback input[name=act]").val();
            var id = $("#modal_rollback input[name=itemId]").val();
            var projectId = $("#modal_rollback input[name=projectId]").val();

            that.ops( projectId,id,"确定回滚？",act,version );
        } );
    },
    ops:function( projectId,id,msg ,act,version){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/release/publish_ops"),
                    type:'POST',
                    data:{
                        act:act,
                        id:id,
                        version:version,
                        projectId:projectId
                    },
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
    release_publish_ops.init();
});