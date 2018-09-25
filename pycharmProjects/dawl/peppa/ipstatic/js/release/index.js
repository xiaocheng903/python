;
var release_index_ops = {
    init:function(){
        this.eventBind();
        this.datetimepickerComponent();
    },
    eventBind:function(){
        var that = this;
        $(".wrap_search .search").click( function(){
            $(".wrap_search").submit();
        });

        $(".betaStatus").click( function(){
            var data = {
                act:"betaStatus",
                id:$(this).attr("data")
            };
            that.ops( "确定标记已同步公测？",data )
        } );
    },
    ops:function( msg ,data){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl("/release/ops"),
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
        common_ops.confirm( msg ,callback );
    },
    datetimepickerComponent:function() {
        var that = this;
        //date range picker
        $(".wrap_search input[name=date_range_picker]").val( $(".wrap_search input[name=gaDate_from]").val() + " 至 " + $(".wrap_search input[name=gaDate_to]").val() );
        $(".wrap_search input[name=date_range_picker]").dateRangePicker({
            autoClose: false,
            format: 'YYYY-MM-DD',
            separator: ' 至 ',
            language: 'cn',
            startOfWeek: 'monday',// or monday
            getValue: function() {
                return $(this).val();
            },
            setValue: function(s,start,end) {
                if(!$(this).attr('readonly') && !$(this).is(':disabled') && s != $(this).val()) {
                    $(this).val(s);
                }
                $(".wrap_search input[name=gaDate_from]").val( start );
                $(".wrap_search input[name=gaDate_to]").val( end );
            },
            startDate: false,
            endDate: false,
            time: {
                enabled: false
            },
            minDays: 0,
            maxDays: 0,
            showShortcuts: false,
            shortcuts: {},
            customShortcuts : [],
            inline:false,
            container:'body',
            alwaysOpen:false,
            singleDate:false,
            lookBehind: false,
            batchMode: false,
            duration: 200,
            stickyMonths: false,
            dayDivAttrs: [],
            dayTdAttrs: [],
            applyBtnClass: '',//确定btn的class btn-tiny
            singleMonth: 'auto',
            hoveringTooltip: function(days, startTime, hoveringTime)
            {
                return false;
            },
            showTopbar: true,
            customTopBar: '请选择日期',
            swapTime: false,
            selectForward: false,
            selectBackward: false,
            showWeekNumbers: false,
            getWeekNumber: function(date) {//date will be the first day of a week
                return moment(date).format('w');
            }
        }).bind('datepicker-apply',function(event,obj) {
        });
    }
};

$(document).ready( function(){
    release_index_ops.init();
} );