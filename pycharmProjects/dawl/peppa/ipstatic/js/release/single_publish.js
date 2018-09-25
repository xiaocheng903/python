;
var release_publish_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".upload").click( function(){
            that.ops( $(this).attr("data"),"确定上传？","upload" )
        });

        $(".gray").click( function(){
            that.ops( $(this).attr("data"),"确定发灰度？","gray" )
        });

        $(".production").click( function(){
            var msg = $.trim( $(this).text() );
            that.ops( $(this).attr("data"),"确定" + msg +"？","production" )
        });

        $(".switch_weight").click( function(){
            var msg = $.trim( $(this).text() );
            that.ops( $(this).attr("data"),"确定" + msg +"？<br/>目前只支持切换全部流量","switch_weight" )
        });

    },
    ops:function( id,msg ,act,version){
        if( version == undefined ){
            version = "";
        }
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/release/publish_ops"),
                    type:'POST',
                    data:{
                        act:act,
                        id:id,
                        version:version,
                        projectId:$(".hidden_wrap input[name=projectId]").val()
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