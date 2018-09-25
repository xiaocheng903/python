;
$(document).ready( function(){

    $("table tbody tr").click( function(){
        var date = $(this).attr("data");
        if( date == undefined ){
            return;
        }
        window.location.href = common_ops.buildUrl("/delivery/list",{ startDeliveryDate:date,endDeliveryDate:date });
    });

} );