;
var stat_index_ops = {
    init:function(){
        chart_ops.setOption();
        this.eventBind();
        this.datetimepickerComponent();

    },
    eventBind:function(){

        var that = this;

        $(".wrap_search .search").click( function(){
            $(".wrap_search").submit();
        });


        var data = $(".hide_wrap input[name=data]").val();
        var categories = $(".hide_wrap input[name=categories]").val();
        data = eval('('+ data +')');
        categories = eval('('+ categories +')');
        var performance = data.performance;
        var slowFun = data.slowFun;
        var slowSql = data.slowSql;
        var errorCnt = data.errorCnt;
        that.drawPerformance( categories ,performance );
        that.dranSlowFun( categories ,slowFun );
        that.dranSlowSql( categories ,slowSql );
        that.dranErrorCnt( categories ,errorCnt );

    },
    drawPerformance:function( categories ,data){

        var series = [];

        for( idx in data ){
            var tmp_item = data[ idx ];
            var tmp_data = {
                "name":tmp_item['name'],
                "data":[]
            };

            for( tmp_idx in  tmp_item['data'] ){
                tmp_data['data'].push( parseInt( tmp_item['data'][ tmp_idx ] ) )
            }

            series.push( tmp_data );
        }

        format_data = {
            'title':'性能95',
            'target':'performance_wrap',
            'categories':categories,
            'series':series,
            'unit':'ms'
        };

        chart_ops.drawLine( format_data );
    },
    dranSlowFun:function( categories ,data ){
        var series = [];

        for( idx in data ){
            var tmp_item = data[ idx ];
            var tmp_data = {
                "name":tmp_item['name'],
                "data":[]
            };

            for( tmp_idx in  tmp_item['data'] ){
                tmp_data['data'].push( parseInt( tmp_item['data'][ tmp_idx ] ) )
            }

            series.push( tmp_data );
        }

        format_data = {
            'title':'慢方法',
            'target':'slowfun_wrap',
            'categories':categories,
            'series':series,
            'unit':'个'
        };

        chart_ops.drawLine( format_data );
    },
    dranSlowSql:function( categories ,data ){
        var series = [];

        for( idx in data ){
            var tmp_item = data[ idx ];
            var tmp_data = {
                "name":tmp_item['name'],
                "data":[]
            };

            for( tmp_idx in  tmp_item['data'] ){
                tmp_data['data'].push( parseInt( tmp_item['data'][ tmp_idx ] ) )
            }

            series.push( tmp_data );
        }

        format_data = {
            'title':'慢查询',
            'target':'slowurl_wrap',
            'categories':categories,
            'series':series,
            'unit':'个'
        };

        chart_ops.drawLine( format_data );
    },
    dranErrorCnt:function( categories ,data ){
        var series = [];

        for( idx in data ){
            var tmp_item = data[ idx ];
            var tmp_data = {
                "name":tmp_item['name'],
                "data":[]
            };

            for( tmp_idx in  tmp_item['data'] ){
                tmp_data['data'].push( parseInt( tmp_item['data'][ tmp_idx ] ) )
            }

            series.push( tmp_data );
        }

        format_data = {
            'title':'错误数量',
            'target':'errorcnt_wrap',
            'categories':categories,
            'series':series,
            'unit':'个'
        };

        chart_ops.drawLine( format_data );
    },
    datetimepickerComponent:function() {
        var that = this;
        //date range picker
        $(".wrap_search input[name=date_range_picker]").val( $(".wrap_search input[name=dateFrom]").val() + " 至 " + $(".wrap_search input[name=dateTo]").val() );
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
                $(".wrap_search input[name=dateFrom]").val( start );
                $(".wrap_search input[name=dateTo]").val( end );
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
    stat_index_ops.init();
} );