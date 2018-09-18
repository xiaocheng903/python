;
var project_set_ops = {
    init:function(){
        this.eventBind();
        this.datetimepickerComponent();
        this.eventRemove();
    },
    eventBind:function(){
        var that = this;
        $("#repo").SumoSelect({
            csvDispCount: 10,
            selectAll: true,
            placeholder: '请选择仓库',
            floatWidth: 400,
            //search: true,
            //searchText: '请输入仓库名称搜索...'
        });

        $( "#jira" ).autocomplete({
            source: function( request, response ) {
                $.ajax( {
                    url: common_ops.buildUrl( "/jira/search/issues" ),
                    dataType: "json",
                    data: {
                        query: request.term
                    },
                    success: function( res ) {
                        response( $.map( res.data, function( item ) {
                            return {
                                "issueKey":item.issueKey,
                                "assignee":item.assignee,
                                "description":item.description,
                                "id":item.issueKey,
                                "label":item.issueKey + " " + item.description
                            }
                        }));
                    }
                } );
            },
            minLength: 2,
            select: function( event, ui ) {
                if( $("#jiraWrap table tbody tr[data=" + ui.item.issueKey + "]").length > 0 ){
                    return;
                }

                var tmpIssue = "<a target='_blank' href='" + common_ops.buildJiraUrl( ui.item.issueKey ) + "'>" + ui.item.issueKey  + "</a>";
                var tr_html = "<tr data='" + ui.item.issueKey + "'>" +
                    "<td>" + tmpIssue + "</td>" +
                    "<td>" + ui.item.assignee + "</td>" +
                    "<td>" + ui.item.description + "</td>" +
                    "<td><button type='button' class='btn btn-link'><i class='fa fa-remove'>移除</i></button></td>" +
                    "</tr>";

                $("#jiraWrap tbody").append( tr_html );
                that.eventRemove();
            }
        });

        $("#relateOwner").select2({
            language: "zh-CN",
            width:'100%'
        });

        $("#techOwner").select2();
        $("#testOwner").select2();
        $("#projectOwner").select2();
        $("#relateOwner").on('select2:select', function () {
            var tmp_target = $("#relateOwner option:selected");
            if( tmp_target.val() < 1  ){
                return;
            }

            if( $("#relateOwnerWrap table tbody tr[data=" + tmp_target.val() + "]").length > 0 ){
                return;
            }

            var tmp_data = tmp_target.data();
            var tmp_tr = "<tr data='" + tmp_target.val() + "'><td>" + tmp_data['name'] + "</td>" +
                "<td>" + tmp_data['email'] + "</td>" +
                "<td>" + tmp_data['roletypedesc'] + "</td>" +
                "<td><button type='button' class='btn btn-link'><i class='fa fa-remove'>移除</i></button></td></tr>";
            $("#relateOwnerWrap table tbody").append( tmp_tr );
            that.eventRemove();
        });


        $("#project_set_wrap .save").click( function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var name_target = $("#project_set_wrap #name");
            var name = name_target.val();

            var repo = [];

            var techOwner_target = $("#project_set_wrap #techOwner");
            var techOwner = techOwner_target.val();

            var testOwner_target = $("#project_set_wrap #testOwner");
            var testOwner = testOwner_target.val();

            var projectOwner_target = $("#project_set_wrap #projectOwner");
            var projectOwner = projectOwner_target.val();

            var startDate_target = $("#project_set_wrap #startDate");
            var startDate = startDate_target.val();

            var endDate_target = $("#project_set_wrap #endDate");
            var endDate = endDate_target.val();

            var gaDate_target = $("#project_set_wrap #gaDate");
            var gaDate = gaDate_target.val();

            var note_target = $("#project_set_wrap #note");
            var note = note_target.val();
            
            var projectType_target = $("#project_set_wrap #projectType")
            var projectType = projectType_target.val();

            var relateOwnerIds = [];
            $("#relateOwnerWrap table tbody tr").each( function(){
                relateOwnerIds.push( $(this).attr( "data" ) );
            });

            var jira = [];

            $("#jiraWrap table tbody tr").each( function(){
                var tmpIssueKey = $(this).attr( "data" );
                var tmpAssignee = $( $(this).find("td").get(1) ).html();
                var tmpDescription = $( $(this).find("td").get(2) ).html();
                jira.push( tmpIssueKey + "#" + tmpAssignee + "#" + tmpDescription );
            } );

            if( name.length < 1 ){
                common_ops.tip( "请输入合法的项目名称~~",name_target );
                return;
            }

            if( $("#repo option:selected").length < 1 ){
                common_ops.alert( "请选择仓库~~" );
                return;
            }

            $("#repo option:selected").each( function() {
                repo.push( $(this).val() );
            });

            if( techOwner < 1 ){
                common_ops.tip( "请选择技术负责人~~",techOwner_target );
                return;
            }


            if( testOwner < 1 ){
                common_ops.tip( "请选择测试负责人~~",testOwner_target );
                return;
            }

            if( projectOwner < 1 ){
                common_ops.tip( "请选择测试负责人~~",projectOwner_target );
                return;
            }


            if( !/^\d{4}-\d{2}-\d{2}$/.test( startDate ) ){
                common_ops.tip( "请选择项目开始时间~~",startDate_target );
                return;
            }

            if( !/^\d{4}-\d{2}-\d{2}$/.test( endDate ) ){
                common_ops.tip( "请选择项目结束时间~~",endDate_target );
                return;
            }

            if( !/^\d{4}-\d{2}-\d{2}$/.test( gaDate ) ){
                common_ops.tip( "请选择项目上线时间~~",gaDate_target );
                return;
            }

            if (parseInt(projectType) == 0) {
                if( jira.length < 1 ){
                    common_ops.tip( "请输入JIRA项目编号~~", $("#project_set_wrap #jira"))
                    return;
                }
            }


            var id = $("#project_set_wrap input[name=id]").val();

            var data = {
                "id": id?id:0 ,
                "name":name,
                "repoIds":repo,
                "techOwner":techOwner,
                "testOwner":testOwner,
                "projectOwner":projectOwner,
                "startDate":startDate,
                "endDate":endDate,
                "gaDate":gaDate,
                "note":note,
                "relateOwnerIds":relateOwnerIds,
                "jira":jira,
                "projectType":projectType
            };



            btn_target.addClass("disabled");

            $.ajax({
                url:common_ops.buildUrl("/project/doSet") ,
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
                            window.location.href = common_ops.buildUrl("/project/info",{ "id":res.data.id });
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
        $('#project_set_wrap input[name=startDate]').datetimepicker( params );
        $('#project_set_wrap input[name=endDate]').datetimepicker( params );
        $('#project_set_wrap input[name=gaDate]').datetimepicker( params );
    },
    eventRemove:function(){
        $("table tr i.fa-remove").unbind().bind( "click",function(){
            $(this).parents( "tr" ).remove();
        } );
    }
};

$(document).ready( function(){
    project_set_ops.init();
});