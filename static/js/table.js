
$(function () {
	$(".table_list #rows:even").addClass("table_list_rows_1"); //even odd 为jquery的方法，even为偶数，odd为奇数。特别注意：索引从0开始，所以第一行是偶数！
	$(".table_list #rows:odd").addClass("table_list_rows_2");
	var s = document.body.offsetWidth;  //(带浏览器边框的宽度)
if(isFirefox=navigator.userAgent.indexOf("Firefox")>0)
 s=window.innerWidth;
var a = 777;  //要变换的临界点
var w = "800px"; //DIV宽度（像素）
var w1 = "100%";  //DIV宽度（百分比）
if(s > a){
 $(".table_list").attr("style","width:100%;");
 $(".search").attr("style","width:98%;");
}else{
 $(".table_list").attr("style","width:800px;");
 $(".search").attr("style","width:786px");
}
});
function overStyle(ths) {
	ths.className = "table_list_rows_0";
}
function outStyle(ths) {
	ths.className = ths.className.replace("table_list_rows_0", "");
	$(".table_list #rows:odd").addClass("table_list_rows_2"); //even odd 为jquery的方法，even为偶数，odd为奇数。特别注意：索引从0开始，所以第一行是偶数！
	$(".table_list #rows:even").addClass("table_list_rows_1");
}
function checkAll() {
	var all = $("#all");
	var checks = $("input[name='ids']");
	if (all.attr("checked")) {
		checks.attr("checked", "checked");
	} else {
		checks.attr("checked", "");
	}
}

window.onresize=function(){
var s = document.body.offsetWidth;  //(带浏览器边框的宽度)
if(isFirefox=navigator.userAgent.indexOf("Firefox")>0)
 s=window.innerWidth;
var a = 777;  //要变换的临界点
var w = "800px"; //DIV宽度（像素）
var w1 = "100%";  //DIV宽度（百分比）
if(s > a){
 $(".table_list").attr("style","width:100%;");
 $(".search").attr("style","width:98%;");
}else{
 $(".table_list").attr("style","width:800px;");
 $(".search").attr("style","width:786px");
}
}

