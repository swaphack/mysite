// 单次调用
var id = setTimeout(func, delay);
clearTimeout(id);

// 间隔调用
var id = setInterval(func, delay);
clearInterval(id);

// 放到队列中，会等待前面处于等待状态的事件处理完后，再执行
setTimeout(func, 0);


function invoke(func, start, interval, end) {
	if (!start) start = 0;
	if (argments.length <=2 ) {
		setTimeout(func, start);
	} else {
		setTimeout(repeat, start);
		function repeat() {
			var h = setInterval(f, interval);
			if (end) setTimeout(function() {
				clearInterval(h);
			}, end);
		}
	}
}

--------------------------------------------------------
window.location = document.location;

var url = "https://baidu.com/?key=12&question=121";

location.href
protocol, host, name, port, pathname, search


function urlArgs() {
	var args = {};
	var query = location.search.toString(1);
	var pairs = query.split("&");
	for (var i = 0; i < pairs.length; i++) {
		var pos = pairs[i].indexOf('=');
		if (pos == -1) continue;
		var name = pairs[i].subString(0, pos);
		var value = pairs[i].subString(pos + 1);
		value = decodeURIComponent(value);
		args[name] = value;
	}

	return args;
}

1.定位
location.assign(url) 跳到一个新的页面，并把当前页面保留到历史记录中
location.replace(url) 跳到一个新的页面，但不把当前页面保留到历史记录中

location = url 直接跳转
location.search = "?page=" + (pagenum + 1);

2.历史
history.back();
history.forward();
history.go(-2);

3.navigator
浏览器嗅探

appName 		Web浏览器全称
appVersion 		Web浏览器版本
userAgent		USER_AGENT HTTP头部中发送的字符串。
platform 		浏览器所在得操作系统的字符串
onLine			是否联网
geolocation 	用户地理位置
javaEnabled		是否可以运行java小程序
cookieEnable 	是否永久保留cookie

var browser = (function() {
	var s = navigator.userAgent.toLowerCase();
	var match = /(webkit)[\/]([\w.]+)/.exec(s)
		|| /(opera)(?:.*version)?[\/]([\w.]+)/.exec(s)
		|| /(msie)[\/]([\w.]+)/.exec(s)
		|| |/compatible/.test(s) && /(mozilla)(?:.*? rv:([\w.]+))?/.exec(s)
		|| [];

	return {
		name:match[1] || "",
		version:match[2] || "0"
	};
}());

4.screen

screen.width
screen.height
screen.availWidth
screen.availHeight

5.对话框
alert	弹出包含文本的对话框
confirm	含有确定和取消按钮
prompt 	等待用户输入字符串
showModalDialog HTML格式的弹窗

6.错误处理
window.onerror = function(msg, url, line) {

};

7.打开和关闭窗口
window.open() => about:blank
window.open(url) => 打开一个新的界面
window.open(url, name) =>打开界面，如果name已有，跳转到该界面，否则，打开一个新的界面

<a target="" />
<form target="" />
target可以设置成_blank, _parent, _top

window.close()

var w = window.open();
w.alert("fadf");
w.location = "url";

w.close();

8.窗体之间
window = self
parent.history.back();

顶级窗口或标签
parent == self

parent.frames