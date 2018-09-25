;
var dba_history_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".wrap_search select[name=status]").change( function(){
            $(".wrap_search").submit();
        });
    }
};

$(document).ready( function(){
    dba_history_ops.init();
});