;
var release_task_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        prettyPrint();

        $('#myTabs a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        });

        $(".wrap_search select[name=type]").change( function() {
            $(".wrap_search").submit();
        });
    }
};

$(document).ready( function(){
    release_task_ops.init();
});