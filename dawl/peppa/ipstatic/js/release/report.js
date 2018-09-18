;
var release_report_ops = {
    init:function(){
        var E = window.wangEditor
        var editor = new E('#test-report')
        editor.customConfig.zIndex = 100
        editor.create()
        $("#test-report .w-e-text-container").css({'height':'600px','margin-bottom':'20px'})

        this._editor = editor;

        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".btn_save").click(function () {
            var html = that._editor.txt.html()
            // console.log(html)
            var releaseId = $(this).attr("data");
            var data = {
                "id":releaseId,
                "report":html,
                "send":$(this).attr("is_send")
            }
            $.ajax({
                url:common_ops.buildUrl("/release/do-set-report"),
                type:'POST',
                data:data,
                dataType:'json',
                success:function( res ){
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/release/info",{id:releaseId});
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });

        });

    }
};

$(document).ready( function(){
    release_report_ops.init();
});