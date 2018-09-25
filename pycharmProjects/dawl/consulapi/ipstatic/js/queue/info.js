;
var queue_info_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){

        $(".retry").click( function(){
            data = {
                id: $(this).attr("data")
            }
            var callback = {
                'ok':function(){
                    $.ajax({
                        url:common_ops.buildUrl("/queue/retry"),
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
            common_ops.confirm( "确定重新运行？" ,callback );
        } );
    }
};

$(document).ready( function(){
    queue_info_ops.init();
} );