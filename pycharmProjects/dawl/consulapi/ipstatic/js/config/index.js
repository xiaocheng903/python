;
var dba_index_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){

        var width = $("table").width();
        $(".prettyprint").css( "width",parseInt( width * 0.7 ) );

        prettyPrint();

        $("#uid_target").select2();

        var  that  = this;

        $(".wrap_search .search").click( function(){
            $(".wrap_search").submit();
        });


        $(".pass").click( function(){
            var data = {
                "projectId":$(this).attr("data-projectId"),
                "itemId":$(this).attr("data-id"),
                "act":"pass"
            };
            that.ops( $(this),"确定通过？", data );
        });

        $(".reject").click( function(){
            $('#modal_reject input[name=id]').val( $(this).attr("data-id") );
            $('#modal_reject input[name=projectId]').val( $(this).attr("data-projectId") );
            $('#modal_reject').modal();
        });

        $("#modal_reject .save").click( function(){

            var rejectNote_target = $('#modal_reject textarea[name=rejectNote]');
            var rejectNote = rejectNote_target.val();
            if( rejectNote.length < 3 ){
                common_ops.tip( "请输入驳回原因~~",rejectNote_target );
                return;
            }

            var data = {
                "projectId":$('#modal_reject input[name=projectId]').val(),
                "itemId":$('#modal_reject input[name=id]').val(),
                "act":"reject",
                "rejectNote":$('#modal_reject textarea[name=rejectNote]').val()
            };
            that.ops( $(this),"确定驳回？", data );
        });

        $(".betaStatus").click( function(){
            var data = {
                "projectId":$(this).attr("data-projectId"),
                "itemId":$(this).attr("data-id"),
                "act":"betaStatus"
            };

            that.ops( $(this),"确定同步公测？", data );
        });

    },
    ops:function( btn_target,msg,data ){
        if( btn_target.hasClass("disabled") ){
            common_ops.alert("正在处理!!请不要重复提交~~");
            return;
        }

        btn_target.addClass("disabled");

        var confirm_callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/config/ops"),
                    type:'POST',
                    data:data,
                    dataType:'json',
                    success:function( res ){
                        btn_target.removeClass("disabled");
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
            'cancel':function(){
                btn_target.removeClass("disabled");
            }
        };

        common_ops.confirm( msg ,confirm_callback );
    }
};

$( document ).ready( function(){
    dba_index_ops.init();
});