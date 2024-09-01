function openWindow(url, width, height) {
	if (!width) {
		width = 600;
	}
	if (!height) {
		height = 400;
	}

	var topPos = screen.height/2 - height/2;
	var leftPos = screen.width/2 - width/2;
	var win_cfg = "status=no,scrollbars=yes,location=no,resizable=yes,top="
			+ topPos + ",left=" + leftPos + ",width=" + width + ",height="
			+ height;
	var win = window.open(url, "_NEW_WIN_" + window.name, win_cfg);
	win.focus();
}

function openwindow( url, winName, width, height) 
{
xposition=0; yposition=0;
if ((parseInt(navigator.appVersion) >= 4 ))
{
xposition = (screen.width - width) / 2;
yposition = (screen.height - height) / 2;
}
theproperty= "width=" + width + "," 
+ "height=" + height + "," 
+ "location=0," 
+ "menubar=0,"
+ "resizable=0,"
+ "scrollbars=yes,"
+ "status=0," 
+ "titlebar=0,"
+ "toolbar=0,"
+ "hotkeys=0,"
+ "screenx=" + xposition + "," //仅适用于Netscape
+ "screeny=" + yposition + "," //仅适用于Netscape
+ "left=" + xposition + "," //IE
+ "top=" + yposition; //IE 
window.open( url,winName,theproperty );
}


function openRightWindow(url, width, height) {

	var topPos =200;
	var leftPos = screen.width-190;
	var win_cfg = "status=no,scrollbars=yes,location=no,resizable=yes,top="
			+ topPos + ",left=" + leftPos + ",width=" + width + ",height="
			+ height;
	var win = window.open(url, "_NEW_WIN_" + window.name, win_cfg);
	win.focus();
}


	
function textLength(which,ths){
    if (which.value.length > ths){
        which.value = which.value.substring(0,ths); 
        return false;
    }

}