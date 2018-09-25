;
var release_set_ops = {
    init:function(){
        this.eventBind();
        this.datetimepickerComponent();
    },
    eventBind:function(){
        var that = this;
        $("#repo").SumoSelect({
            csvDispCount: 10,
            selectAll: true,
            placeholder: '请选择仓库',
            floatWidth: 400
        });


        $("#release_set_wrap .save").click( function(){
            var btn_target = $(this);

            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }


            var repo = [];

            var branchType_target = $("#release_set_wrap #branchType");
            var branchType = branchType_target.val();

            var gaDate_target = $("#release_set_wrap #gaDate");
            var gaDate = gaDate_target.val();

            var testDate_target = $("#release_set_wrap #testDate");
            var testDate = testDate_target.val();

            var lockDate_target = $("#release_set_wrap #lockDate");
            var lockDate = lockDate_target.val();

            var note_target = $("#release_set_wrap #note");
            var note = note_target.val();


            if( $("#repo option:selected").length < 1 ){
                common_ops.alert( "请选择仓库~~" );
                return;
            }

            $("#repo option:selected").each( function() {
                repo.push( $(this).val() );
            });

            if( branchType < 1 ){
                common_ops.tip( "请选择分支类型~~",branchType_target );
                return;
            }


            if( !/^\d{4}-\d{2}-\d{2}$/.test( gaDate ) ){
                common_ops.tip( "请选择上线日期~~",gaDate_target );
                return;
            }

            if( !/^\d{4}-\d{2}-\d{2}$/.test( testDate ) ){
                common_ops.tip( "请选择集测日期~~",testDate_target );
                return;
            }

            if( !/^\d{4}-\d{2}-\d{2}$/.test( lockDate ) ){
                common_ops.tip( "请选择锁版日期~~",lockDate_target );
                return;
            }

            if( gaDate < lockDate  ){
                common_ops.alert( "上线日期不能小于锁版日期~~" );
                return;
            }

            if( testDate > lockDate ){
                common_ops.alert( "集测日期不能大于锁版日期~~" );
                return;
            }

            var id = $("#release_set_wrap input[name=id]").val();

            var data = {
                "id": id?id:0 ,
                "repoIds":repo,
                "branchType":branchType,
                "gaDate":gaDate,
                "testDate":testDate,
                "lockDate":lockDate,
                "note":note
            };



            btn_target.addClass("disabled");

            $.ajax({
                url:common_ops.buildUrl("/release/doSet") ,
                type:'POST',
                data:JSON.stringify(data),
                dataType:'json',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json;charset=utf-8'
                },
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/release/info",{ "id":res.data.id });
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        });
    },
    datetimepickerComponent:function() {
        $.datetimepicker.setLocale('zh');
        params = {
            scrollInput: false,
            scrollMonth: false,
            scrollTime: false,
            dayOfWeekStart: 1,
            lang: 'zh',
            todayButton: true,//回到今天
            defaultSelect: true,
            defaultDate: new Date().Format('yyyy-MM-dd'),
            format: 'Y-m-d',//格式化显示
            timepicker: false
        };
        $('#release_set_wrap input[name=gaDate]').datetimepicker( params );
        $('#release_set_wrap input[name=testDate]').datetimepicker( params );
        $('#release_set_wrap input[name=lockDate]').datetimepicker( params );

    }
};

$(document).ready( function(){
    release_set_ops.init();
});