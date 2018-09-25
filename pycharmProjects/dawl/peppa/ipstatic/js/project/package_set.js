;
var package_set_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $("#package_set_wrap .save").click( function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var items = [];
            var is_break = false;
            $("#package_set_wrap .item input[name=url]").each( function(){

                var tmp_url = $(this).val();
                if( tmp_url.length > 1 && !/^http/.test( tmp_url ) ){
                    is_break = true;
                    common_ops.alert( "包地址必须以http开头~~" );
                    return false;
                }

                items.push( $(this).attr("data") + "#" + tmp_url  );

            });

            if( is_break ){
                return;
            }

            btn_target.addClass("disabled");
            $.ajax({
                url:common_ops.buildUrl("/project/package_doset") ,
                type:'POST',
                data: {
                    "items":items,
                    "targetId":$("#package_set_wrap input[name=targetId]").val(),
                    "targetType": $("#package_set_wrap input[name=targetType]").val()
                },
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            if( $("#package_set_wrap input[name=targetType]").val() == 1 ){
                                window.location.href = common_ops.buildUrl( "/project/info",{ "id": $("#package_set_wrap input[name=targetId]").val() } );
                            }else{
                                window.location.href = common_ops.buildUrl( "/release/info",{ "id": $("#package_set_wrap input[name=targetId]").val() } );
                            }

                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        });
    }
};

$(document).ready( function(){
    package_set_ops.init();
});