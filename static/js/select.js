function existItem(obj, value) {
	var isExist = false;
	for (var i = 0; i < obj.options.length; i=i+1) {
		if (obj.options[i].value == value) {
			isExist = true;
			break;
		}
	}
	return isExist;
}

$(document).ready(function() {
var from = document.getElementById("obj1");
var to = document.getElementById("obj2");
	 $("#obj1").bind("dblclick", function(){
	 	moveTo(from,to);
	 }
	 );
 $("#obj2").bind("dblclick", function(){
	 	moveTo(to,from);
	 }
	 );
});

function addItem(obj, value, text){
	if(!existItem(obj,value)){
		var option = new Option(text,value);
		obj.options.add(option);
	}
}


function removeItem(obj, value){
	for(var i=0; i < obj.options.length; i=i+1) {
		if(obj.options[i].value == value){
			try{
				obj.options.remove(i);
			}catch(e){
				obj.remove(i);
			}
		}
	}
}


function clear(obj){
	obj.options.length = 0;
}


function moveTo(from, to){
	for(var i=0;i<from.options.length;i=i+1){
		if(from.options[i].selected){
			addItem(to, from.options[i].value, from.options[i].text);
		}
	}
	for(var j=from.options.length-1;j>=0;j=j-1){
		if(from.options[j].selected){
			try{
			from.options.remove(j);
			}catch(e){
			from.remove(j);
			}
		}
	}
}


function moveAll(from, to){
	for(var i=from.options.length-1;i>=0;i=i-1){
		addItem(to, from.options[i].value, from.options[i].text);
		try{
			from.options.remove(i);
			}catch(e){
			from.remove(i);
			}
	}
}

function addAll(obj, array){
	clear(obj);
	for(var i=0;i<array.length;i=i+1){
		addItem(obj, array[i].value, array[i].name);
	}
}

function getSelectArray(obj){
	var array = new Array();
	for(var i=0;i<obj.options.length;i=i+1){
		array.push(new User(obj.options[i].value,obj.options[i].text));
	}
	return array;
}

function User(value,name){
	this.value = value;
	this.name = name;
	this.toString = function(){
	  return "{\"value\":\"" + value + "\",\"name\":\"" + name + "\"}";
	}
}


function func1(){
	var from = document.getElementById("obj1");
	var to = document.getElementById("obj2");
	moveTo(from,to);
	}
	function func2(){
	var from = document.getElementById("obj2");
	var to = document.getElementById("obj1");
	moveTo(from,to);
	}
	function func3(){
	var from = document.getElementById("obj1");
	var to = document.getElementById("obj2");
	moveAll(from,to);
	}
	function func4(){
	var from = document.getElementById("obj2");
	var to = document.getElementById("obj1");
	moveAll(from,to);
	}
	
	
function checkAll(){
	var all=$("#all");
	var checks=$("input[name='ids']");
	if(all.attr("checked")){
		checks.attr("checked","checked");
	}else{
		checks.attr("checked","");
	}
}
