/**
 * picChange lib
 * 自动生成图片切换导航，以及图片轮转特效
 * @name picChange-0.3.2.js
 * @author afc163 - http://www.ilovespringna.com/
 * @version 0.3
 * @date May 31st, 2010
 * @copyright (c) 2010 afc163 (http://www.ilovespringna.com/)
 * @example or demo Visit http://http://www.ilovespringna.com/test/picChange/
 */

var PC_lastImgOut = null;	//记录图片消失的延时事件
var PC_changingPic = null;	//增加一个对象用于保存消失过程中的图片对象
var PC_picHover = null;		//记录图片hover事件
var PC_changeInter = null;	//记录图片定时切换的延时器
var PC_currentIndex = 1;	//记录当前图片索引号

//图片消失的方法
/*
var picChangeHandle = {
	none:function(){},	//直接切换
	fade:function(){},	//淡出
	move:function(){},	//移出
	wheel:function(){},	//联动
	other:function(){}	//其他效果，供扩展
}
*/
var picChangeHandle = {
	//直接消失
	none: function(lastImg,currentImg){
		if(lastImg != null)
		{
			//上一张图片消失
			lastImg.style.display = "none";
		}
		currentImg.style.zIndex = "0";
		currentImg.style.display = "block";
		lastImg = currentImg;
	},

	//淡出消失
	fade: function(lastImg,currentImg,time){
		if(lastImg != null)
		{
			time = time || 500;
			var opacity = 100;

			//消除快速连续点击标签造成的bug
			clearInterval(PC_lastImgOut);
			setAlpha(currentImg,100);

			PC_lastImgOut = setInterval(function(){
				opacity -= 5;
				setAlpha(lastImg,opacity);
				if(opacity <= 5)
				{
					lastImg.style.display = "none";
					setAlpha(lastImg,100);
					clearInterval(PC_lastImgOut);
					return;
				}
			},time/19);
			lastImg.style.zIndex = "10";
		}
		currentImg.style.zIndex = "0";
		currentImg.style.display = "block";
	},
	
	//移出消失
	move: function(lastImg,currentImg,time,direction){
		direction = direction || "up";

		if(lastImg != null)
		{
			time = time||500;
			var outLength = 0; //指定方向上移出的距离
			var imgLength = 0; //图片的在指定方向上的长度

			//消除快速连续点击标签造成的bug
			clearInterval(PC_lastImgOut);
			switch(direction)
			{
				case "up":
				case "down":
					currentImg.style.top = "";
					imgLength = lastImg.offsetHeight;
					break;
				case "left":
				case "right":
					currentImg.style.left = "";
					imgLength = lastImg.offsetWidth;
					break;
			}
			var speed = 20*imgLength/time;

			PC_lastImgOut = setInterval(function(){
				//判断四个方向
				switch(direction)
				{
					case "up":
						outLength -= speed;
						lastImg.style.top = outLength + "px";
						break;
					case "left":
						outLength -= speed;
						lastImg.style.left = outLength + "px";
						break;
					case "down":
						outLength += speed;
						lastImg.style.top = outLength + "px";
						break;
					case "right":
						outLength += speed;
						lastImg.style.left = outLength + "px";
						break;
				}
				if(outLength <= (-imgLength) || outLength >= imgLength)
				{
					lastImg.style.display = "none";
					lastImg.style.outLength = 0 + "px";
					clearInterval(PC_lastImgOut);
					PC_changingPic = null;
					return;
				}
			},10);
			lastImg.style.zIndex = "10";
		}
		currentImg.style.zIndex = "0";
		currentImg.style.display = "block";
	},
	
	//联动效果
	wheel: function(lastImg,currentImg,time,direction){
		direction = direction || "up";
		//alert(currentImg.getAttribute("src"));
		if(lastImg != null)
		{
			time = time||500;
			var outLength = 0; //指定方向上移出的距离
			var imgLength = 0; //图片的在指定方向上的长度

			//消除快速连续点击标签造成的bug
			clearInterval(PC_lastImgOut);
			
			switch(direction)
			{
				case "up":
				case "down":
					currentImg.style.top = "";
					imgLength = lastImg.offsetHeight;
					break;
				case "left":
				case "right":
					currentImg.style.left = "";
					imgLength = lastImg.offsetWidth;
					break;
			}
			var speed = 20*imgLength/time;

			PC_lastImgOut = setInterval(function(){
				//判断四个方向
				switch(direction)
				{
					case "up":
						outLength -= speed;
						lastImg.style.top = outLength + "px";
						currentImg.style.top = (outLength + imgLength) + "px";
						break;
					case "left":
						outLength -= speed;
						lastImg.style.left = outLength + "px";
						currentImg.style.left = outLength + imgLength + "px";
						break;
					case "down":
						outLength += speed;
						lastImg.style.top = outLength + "px";
						currentImg.style.top = outLength - imgLength + "px";
						break;
					case "right":
						outLength += speed;
						lastImg.style.left = outLength + "px";
						currentImg.style.left = outLength - imgLength + "px";
						break;
				}
				if(outLength <= (-imgLength) || outLength >= imgLength)
				{
					lastImg.style.display = "none";
					lastImg.style.outLength = 0 + "px";
					currentImg.style.top = "";
					currentImg.style.left = "";
					clearInterval(PC_lastImgOut);
					PC_changingPic = null;
					return;
				}
			},10);
			lastImg.style.zIndex = "10";
		}
		currentImg.style.zIndex = "0";
		currentImg.style.display = "block";
	},
	//其他效果
	other: function(){
		//可扩展
	}
};

//设置透明度
function setAlpha(img,opacity)
{
	if(!-[1,]) //if IE
	{
		img.style.filter = "alpha(opacity="+opacity+")";
		if(img.filters && img.filters.Alpha)
			img.filters.Alpha.opacity = opacity;
	}
	else
	{
		img.style.opacity = ((opacity >= 100)? 99:opacity) / 100;
	}
}

/***使用示例
 *	$pic("picChange").picChange();													//直接切换效果
 *	$pic("picChange").picChange({changeStyle:"fade", time:250,});					//0.25秒淡出效果
 *	$pic("picChange").picChange({changeStyle:"move", time:250, direction:"up"});	//0.25秒向上移出效果
 *	$pic("picChange").picChange({changeStyle:"wheel", time:250, direction:"up"});	//0.25秒向上联动效果
 *  $pic("picChange").picChange({
 *		changeStyle:"fade",		//图片切换效果
 *		time:250,				//图片切换速度（毫秒）
 *		direction:"up",			//图片切换方向，移出和联动时有效
 *      showDesc:true			//是否显示图片描述
 *      isClick:true			//是否为鼠标点击行为触发切换事件，默认为false，代表鼠标停留时触发
 *      interTime:2000			//定时切换图片的间隔，留空时不切换
 *  }};
 */
function $pic(id)
{
	if(typeof id != "string")
	{
		throw "参数必须为字符串类型";
		return id;
	}
	return {
		id:id,
		picChange:function(param){;
			clearInterval(PC_picHover);
			clearInterval(PC_lastImgOut);
			clearInterval(PC_changeInter);
			PC_lastImgOut = null;
			PC_changingPic = null;
			PC_currentIndex = 1

			param = param || {};
			var picId = this.id||"picChange";
			var changeStyle = param.changeStyle||"none";
			var changeStyleFunc = picChangeHandle[changeStyle];
			var time = param.time||250;
			var direction = param.direction || "up";
			var showDesc = param.showDesc || true;
			var isClick = param.isClick || false; //默认为鼠标停留行为触发
			var interTime = param.interTime;
			var picDesc = document.getElementById("picDesc");

			if(typeof param == "string")
				changeStyle = param;

			//添加右下角图片切换标签
			var pic = document.getElementById(picId);
			if(pic == null)
			{
				throw "不存在这个id";
				return;
			}
			var lastImg = null, nextImg = null;
			var index = 0;
			var lastIndex = null; //记录上一个标签

			var picList = pic.getElementsByTagName("li");
			picList[0].firstChild.style.display = "block";
			var picNum = picList.length;	//获得图片数量

			//切换函数封装
			var changePicFunc = function(currentImg){
				if(this.firstChild.className == "select")
					return;

				//切换图片描述
				if(showDesc == true)
					picDesc.innerHTML = currentImg.getAttribute("title") || currentImg.getAttribute("alt");

				//更改切换标签的样式
				if(lastIndex != null)
					lastIndex.className = "";
				this.firstChild.className = "select";
				lastIndex = this.firstChild;

				//切换图片

				if(PC_changingPic != null)
					PC_changingPic.style.display = "none";

				if(lastImg != null)
				{
					//保存正在消失中的图片对象，当用户在一个动作未完成时触发下一个动作时，用于恢复消失中的图片对象的状态
					PC_changingPic = lastImg;
					//上一张图片消失
					changeStyleFunc(lastImg,currentImg,time,direction); //time,direction可选
				}
				lastImg = currentImg;
			};

			if(document.getElementById("picChangeIndex") != null)
				document.getElementById("picChangeIndex").parentNode.removeChild(document.getElementById("picChangeIndex"));
			var indexMenu = document.createElement("ul");
			indexMenu.id = "picChangeIndex";
			for(var i=0;i<picNum;i++)
			{
				var indexList = document.createElement("li");
				if(i==0)
				{
					indexList.innerHTML = "<a href=\"#\" class=\"select\">"+(i+1)+"</a>";
					lastIndex = indexList.firstChild;
					lastImg = picList[i].firstChild;
				}
				else
					indexList.innerHTML = "<a href=\"#\">"+(i+1)+"</a>";

				//添加变换函数
				index = i;
				(function(i){
					if(isClick)
					{
						var hoverItem = indexList;
						indexList.onclick = function(){
							changePicFunc.call(hoverItem,picList[i].firstChild);
							PC_currentIndex = i;
						};
					}
					else
					{
						var hoverItem = indexList;
						indexList.onmouseover = function(){
							PC_picHover = setTimeout(function(){changePicFunc.call(hoverItem,picList[i].firstChild);},300);
							PC_currentIndex = i;
						};
						indexList.onmouseout = function(){clearTimeout(PC_picHover);};
					}
				})(index);
				indexMenu.appendChild(indexList);
			}
			pic.parentNode.appendChild(indexMenu);

			//添加照片描述
			if(showDesc == true && document.getElementById("picDesc") == null)
			{
				var picDescBg = document.createElement("div");
				picDescBg.id = "picDescBg";
				pic.parentNode.appendChild(picDescBg);
				setAlpha(picDescBg,10);

				var picDesc = document.createElement("div");
				picDesc.id = "picDesc";
				
				//从图片的title属性或alt属性中读取描述
				var firstPic = picList[0].firstChild;
				picDesc.innerHTML = firstPic.getAttribute("title") || firstPic.getAttribute("alt");
				//pic.parentNode.appendChild(picDesc);
				setAlpha(picDesc,75);
			}
			
			//每隔interTime的时间切换图片
			pic.parentNode.onmouseover = null;
			pic.parentNode.onmouseout = null;
			if(interTime != null)
			{
				var tempIndexMenu = document.getElementById("picChangeIndex").getElementsByTagName("li");
				PC_changeInter = setInterval(function(){
					currentImg = picList[PC_currentIndex].firstChild;
					changePicFunc.call(tempIndexMenu[PC_currentIndex],currentImg);
					PC_currentIndex = (PC_currentIndex+1<picNum)?PC_currentIndex+1:((PC_currentIndex+1)%picNum);
				},interTime);
			
				pic.parentNode.onmouseover = function(){
					clearInterval(PC_changeInter);
				};

				pic.parentNode.onmouseout = function(){
					PC_changeInter = setInterval(function(){
						currentImg = picList[PC_currentIndex].firstChild;
						changePicFunc.call(tempIndexMenu[PC_currentIndex],currentImg);
						PC_currentIndex = (PC_currentIndex+1<picNum)?PC_currentIndex+1:((PC_currentIndex+1)%picNum);
					},interTime);
				};
			}
		}
	};
}