;
var common_ops = {
    init:function(){
       this.eventBind();
       this.setMenuHighLight();
    },
    eventBind:function(){

    },
    setMenuHighLight:function(){
        if( $(".top_nav_wrap .menu_wrap li.menu").length < 1 ){
            return;
        }

        var pathname = window.location.pathname;

        var nav_name = null;

        if(  pathname.indexOf("/index") > -1 || pathname == "/ipublish/" ){
            nav_name = "default";
        }

        if(  pathname.indexOf("/project/") > -1  ){
            nav_name = "project";
        }

        if(  pathname.indexOf("/release/") > -1  ){
            nav_name = "release";
        }

        if(  pathname.indexOf("/stat/") > -1  ){
            nav_name = "stat";
        }

        if(  pathname.indexOf("/queue/") > -1  ){
            nav_name = "queue";
        }

        if(  pathname.indexOf("/config/") > -1   ){
            nav_name = "config";
        }


        if(  pathname.indexOf("/test/env") > -1 ){
            nav_name = "tester";
        }

        if(  pathname.indexOf("/log/") > -1   ){
            nav_name = "log";
        }

        if(  pathname.indexOf("/jenkins/") > -1   ){
            nav_name = "jenkins";
        }


        if( nav_name == null ){
            return;
        }

        $(".top_nav_wrap .menu_wrap li.menu_" + nav_name ).addClass("active");
    },
    buildUrl:function( path ,params ){
        var url = basePath + path;
        //?a=1&b=1,{ a:1,b:2 }
        var _paramUrl = "";
        if(  params ){
            _paramUrl = Object.keys( params ).map( function( k ){
                return [ encodeURIComponent( k ),encodeURIComponent( params[ k ] ) ].join("=");
            }).join("&");
            _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
    },
    buildJiraUrl:function( issueKey ){
        return "http://192.168.60.204/browse/" +  issueKey;
    },
    alert:function( msg ,cb ){
        layer.alert( msg,{
            yes:function( index ){
                if( typeof cb == "function" ){
                    cb();
                }
                layer.close( index );
            }
        });
    },
    confirm:function( msg,callback ){
        callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
        layer.confirm( msg , {
            btn: ['确定','取消'] //按钮
        }, function( index ){
            //确定事件
            if( typeof callback.ok == "function" ){
                callback.ok();
            }
            layer.close( index );
        }, function( index ){
            //取消事件
            if( typeof callback.cancel == "function" ){
                callback.cancel();
            }
            layer.close( index );
        });
    },
    tip:function( msg,target ){
        layer.tips( msg, target, {
            tips: [ 3, '#e5004f']
        });
        $('html, body').animate({
            scrollTop: target.offset().top - 10
        }, 100);
    },
    datedifference:function (sDate1, sDate2) {    //sDate1和sDate2是2006-12-18格式
        var dateSpan,
            tempDate,
            iDays;
        sDate1 = Date.parse(sDate1);
        sDate2 = Date.parse(sDate2);
        dateSpan = sDate2 - sDate1;
        dateSpan = Math.abs(dateSpan);
        iDays = Math.floor(dateSpan / (24 * 3600 * 1000));
        return iDays
    }
};

$(document).ready( function(){
    common_ops.init();
} );

// 对Date的扩展，将 Date 转化为指定格式的String
// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符，
// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
// 例子：
// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
// (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18
Date.prototype.Format = function(fmt)
{ //author: meizz
    var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt))
        fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp("("+ k +")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    return fmt;
};