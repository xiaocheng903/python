;
var project_task_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){

        prettyPrint();


        $('#myTabs a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        });

        $(".del_item").click( function(){
            var data = {
                "projectId":$(this).attr("data-projectId"),
                "itemId": $(this).attr("data-id")
            };
            var callback = {
                'ok':function(){
                    $.ajax({
                        url:common_ops.buildUrl("/project/task_ops"),
                        type:'POST',
                        data:data,
                        dataType:'json',
                        success:function( res ){
                            var tmp_callback = null;
                            if( res.code == 200 ){
                                tmp_callback = function(){
                                    window.location.href = window.location.href;
                                }
                            }
                            common_ops.alert( res.msg,tmp_callback );
                        }
                    });
                },
                'cancel':null
            };
            common_ops.confirm( "确定删除？删除之后不可恢复" ,callback );
        });


    }
};

$(document).ready( function(){
    project_task_ops.init();
});