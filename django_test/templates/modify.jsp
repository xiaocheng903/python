<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="application/json; charset=UTF-8"/>
<title>竞拍</title>
<script src="../js/jquery.js"></script>
<script src="../js/jquery-ui.js"></script>  
</head>
<body>
手机号码:<input id="phone" type="text" value="" style="width:200px"/>&nbsp;
验证码:<input id="verifycode" type="text" value="" style="width:200px"/>&nbsp;
<button id="getCodeBtn" type="button">获取验证码</button>&nbsp;&nbsp;&nbsp;
<button id="loginBtn" type="button">登录</button>&nbsp;&nbsp;&nbsp;<br/><br/>
登录成功列表:&nbsp;<br><textarea rows="5" cols="30" id="logins"></textarea>&nbsp;&nbsp;
<button id="loginsBtn" type="button">登录列表</button>&nbsp;&nbsp;&nbsp;
<button id="primaryBtn" type="button">删除拍车数据</button>&nbsp;&nbsp;&nbsp;<br/><br/>
竞拍手机号:<input id="phoneId" type="text" value="" style="width:200px"/>&nbsp;
拍车价:<input id="price" type="text" value="" style="width:50px"/>&nbsp;<br><br>
时间:&nbsp;<br><textarea rows="1" cols="20" id="times"></textarea>&nbsp;&nbsp;
<button id="submitBtn" type="button">手动拍车</button>&nbsp;&nbsp;&nbsp;
<button id="modifyBtn" type="button">获取列表</button>&nbsp;&nbsp;&nbsp;
<button id="queryBtn" type="button">查询竞拍列表</button>&nbsp;&nbsp;&nbsp;
<button id="tryBtn" type="button">时间差</button>&nbsp;&nbsp;&nbsp;<br/>
<table id="myTable" cellpadding="3" cellspacing="0" border="1">
<caption align="top">车源信息</caption>
<thead>
<tr>
<th>操作</th>
<th>车名</th>
<th>底价</th>
<th>车辆id</th>
</tr>
</thead>
<tbody id ="car"></tbody>
</table>

<table id="myTable2" cellpadding="1" cellspacing="0" border="1">
<caption align="top">待拍车信息</caption>
<thead>
<tr>
<th>删除</th>
<th>车辆id</th>
<th>手机号</th>
<th>低价</th>
<th>拍车价</th>
</tr>

</thead>
<tbody id = submits></tbody>
</table>
</body>
<script>
	function changeState(){ 
		$.ajax(
			{
				type:"post",
				url:"../cust/getWebsiteDatetime",
				data:"",
				dataType:"text",
				success:function(result){
					$("#times").text(result);
			    }
			});
	}
	//登录数据
	function logins(){ 
		$.ajax(
		{
			type:"post",
			url:"../cust/findPhones",
			data:"",
			dataType:"json",
			success:function(result){
				var p = JSON.stringify(result);
				$("#logins").val(p);
		    }
		});
	}
	function pais()
	{
		//刷新表
		var tbody=$("#submits"); 
	    tbody.html("");                                                                                                                     
	    $.ajax(
	    {
             type: "POST",//传输方式
             url: "../cust/query",//action路径
             data:"",//传递参数，可有可无
             dataType:"json",
			 success:function (result)
			 {
				  var p = JSON.stringify(result)
				  var obj= eval(p);
				  var tbody=$("#submits"); 
				  $(obj).each(function (index){
					  var val=obj[index];
					  var tr=$('<tr></tr>');
					  var col = $('<td></td>');
					  var button2 = $('<button>删除</button>');
					  col.append(button2);
					  tr.append(col);
					  tr.append('<td>'+ val.car_id + '</td>'+'<td>'+ val.phone + '</td>'+'<td>'+ val.car_price + '</td>' + '<td>'+ val.price + '</td>');
					  tbody.append(tr);
					   //删除按钮控件
					   button2.click(function()
					   {								
							$.ajax(
						    {
			                  type: "POST",//传输方式
			                  url: "../cust/delete",//action路径
			                  data: {car_id:val.car_id},//传递参数，可有可无
			                  dataType:"text",
							  success:function (result){
									alert("删除成功");
							  }
							});
						});
				  });
				  $('#myTable2 tbody').replaceWith(tbody);
			 }
		});
	}
	$(function()
	{
		setInterval("changeState()",1000);
		logins();
		pais();
		//登录数据
		$("#loginsBtn").click(function()
		{
			$.ajax(
			{
				type:"post",
				url:"../cust/findPhones",
				data:"",
				dataType:"json",
				success:function(result){
					var p = JSON.stringify(result);
					$("#logins").val(p);
			    }
			});
		});	
		//获取验证码
		$("#getCodeBtn").click(function()
		{
			var phone = $("#phone").val();
			if(phone!="")
			{
				$.ajax(
				{
					type:"post",
					url:"../cust/getcode",
					data:{phone:phone},
					dataType:"json",
					success:function (result){
						if(result.status == '0'){
							alert("获取验证码成功");
						}
						else if(result.code == '500'){
							alert("获取验证码失败喽");
						}
						else{
							alert("获取验证码失败");
						}
					},
					error: function (result) {
					   alert("后台请求失败");
	                  }
				  }
				);
			}else{
				alert("请输入手机号码地址");
			}
		});
		//登录
		$("#loginBtn").click(function()
		{
			var phone = $("#phone").val();
			var verifycode = $("#verifycode").val();
			if(phone!="" && verifycode!=""){
			    $.ajax(
			    {
	                  type: "POST",//传输方式
	                  url: "../cust/login",//action路径
	                  dataType:"json",
	                  data:{phone:phone,verifycode:verifycode},
					  success:function (result)
					  {
						if(result.status == '0'){
							alert("登录成功");
						}
						else if(result.code == '403'){
							alert("登录失败喽");
						}
						else{
							alert("登录失败");
						}
					  },
	                  error: function (result) {
						 alert("后台请求失败");
	                  }
				});
			}else{
				alert("请输入手机号码");
		}
		});
		//获取列表
		$("#modifyBtn").click(function()
		{
		    $.ajax(
		    {
                  type: "GET",//传输方式
                  url: "../cust/getValue",//action路径
                  data:"",//传递参数，可有可无
                  dataType:"json",
				  success:function (result)
				  {
					  var p = JSON.stringify(result);
					  var obj= eval(p);
					  var tbody=$("#car"); 
					  tbody.html("");
					  $(obj).each(function (index){
						  var val=obj[index];
						  var tr=$('<tr></tr>');
						  var col = $('<td></td>');
						  var button1 = $('<button>添加列表</button>');
						  col.append(button1);
						  tr.append(col);
						  tr.append('<td>'+ val.title + '</td>' + '<td>'+ val.car_price + '</td>' +'<td>'+ val.id + '</td>');						 
						  var input1 = $('<input id = phone2></input>');
						  tbody.append(tr);
						  //添加列表的控件
						  button1.click(function()
					      {
							var price = $("#price").val();
							var phone = $("#phoneId").val(); 
							if(price!="" && phone!=""){
								//拍车数据入库
								$.ajax(
							    {
				                  type: "POST",//传输方式
				                  url: "../cust/getsubmit",//action路径 竞拍数据入库
				                  data: {phone:phone,price:price,car_price:val.car_price,car_id:val.id},//传递参数，可有可无
				                  dataType:"text",
								  success:function (result){
										alert("添加成功");
								  }
								});
							}
							else{
								alert("请输入价格和手机号");
							}
						  });
					  });
					  $('#myTable tbody').replaceWith(tbody);
				  }
			});
		});
		//时间差按钮控件
		$("#tryBtn").click(function()
		{
			$.ajax(
			{
				type:"post",
				url:"../cust/Difftime",
				data:"",
				dataType:"text",
				success:function(result){
			    }
			});
		});
		//拍车按钮
		$("#submitBtn").click(function()
		{
			$.ajax(
		    {
                  type: "POST",//传输方式
                  url: "../cust/submits",//action路径
                  data: {},//传递参数，可有可无
                  dataType:"text",
				  success:function (result){
				  }
			});
		});		
		//查询竞拍的列表
		$("#queryBtn").click(function()	
		{
			//刷新表
			var tbody=$("#submits"); 
		    tbody.html("");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
		    $.ajax(
		    {
                 type: "POST",//传输方式
                 url: "../cust/query",//action路径
                 data:"",//传递参数，可有可无
                 dataType:"json",
				 success:function (result)
				 {
					  var p = JSON.stringify(result)
					  var obj= eval(p);
					  var tbody=$("#submits"); 
					  $(obj).each(function (index){
						  var val=obj[index];
						  var tr=$('<tr></tr>');
						  var col = $('<td></td>');
						  var button2 = $('<button>删除</button>');
						  col.append(button2);
						  tr.append(col);
						  tr.append('<td>'+ val.car_id + '</td>'+'<td>'+ val.phone + '</td>'+'<td>'+ val.car_price + '</td>' + '<td>'+ val.price + '</td>');
						  tbody.append(tr);
						   //删除按钮控件
						   button2.click(function()
						   {								
								$.ajax(
							    {
				                  type: "POST",//传输方式
				                  url: "../cust/delete",//action路径
				                  data: {car_id:val.car_id},//传递参数，可有可无
				                  dataType:"text",
								  success:function (result){
										alert("删除成功");
								  }
								});
							});
					  });
					  $('#myTable2 tbody').replaceWith(tbody);
				 }
			});
		});
		//删除拍车数据按钮
		$("#primaryBtn").click(function()
		{
			$.ajax(
		    {
                 type: "POST",//传输方式
                 url: "../cust/delete2",//action路径
                 data: {},//传递参数，可有可无
                 dataType:"text",
			     success:function (result){
					alert("删除成功");
			  }
			});
		});
	});	 	
</script>
</html>