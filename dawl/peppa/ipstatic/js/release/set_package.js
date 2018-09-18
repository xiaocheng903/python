;
var release_set_package_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $("#set_package_wrap .save").click( function(){
            var packageIds = [];
            $("#set_package_wrap input[name='packeage[]']:checked").each( function(){
                packageIds.push( $(this).val() );
            });

            if( packageIds.length < 1 ){
                common_ops.alert( "请选择此次项目涉及的包~~" );
                return;
            }


            var data = {
                "packageIds":packageIds,
                "id":$("#set_package_wrap input[name=id]").val(),
                "type":$("#set_package_wrap input[name=type]").val()
            };

            var callback = {
                'ok':function(){
                    $.ajax({
                        url:common_ops.buildUrl("/release/do-set-package"),
                        type:'POST',
                        data:data,
                        dataType:'json',
                        success:function( res ){
                            var callback = null;
                            if( res.code == 200 ){
                                callback = function(){
                                    url =  common_ops.buildUrl("/release/info",{ "id":data['id'] });
                                    if( parseInt( data["type"] ) == 1 ){
                                        url = common_ops.buildUrl("/project/info",{ "id":data['id'] });
                                    }
                                    window.location.href = url;
                                }
                            }
                            common_ops.alert( res.msg,callback );
                        }
                    });
                },
                'cancel':null
            };
            common_ops.confirm( "确定提交？" ,callback );
        });

    }
};

$(document).ready( function(){
    release_set_package_ops.init();
});