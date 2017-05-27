
window.location = "localhost:80/shop/";

setTimeout(function() {
	alert("121");
}, 2000);


var timestamp = document.getElementById('timestamp');
if (timestamp.firstChild == null) {
	timestamp.appendChild(document.createTextNode(new Date().toString()));
}

/* css 样式*/
timestamp.style.background = "red";

timestamp.className = "hightlight";

timestamp.onclick = function() {
	this.innerHTML = new Date().toString();
}

--------------------------------------------------------
客户端JavaScript

内嵌方式
1.
<script type="text/javascript" src="url"></script>
2.
<script type="text/javascript">	javaScript code </script>

3.
<button onclick="javaScript event"></button>

4.
<a href="javascript:void alert('Hello')"></a>

--------------------------------------------------------
html按顺序执行，如果html中包含javascript 可执行代码，
在碰到JavaScript代码时，会执行代码，后继续渲染html页面

--------------------------------------------------------
事件驱动
click、change、load、mouseover、keypress、readystatechange。

window.addEventListener("load", function() {}, false);
request.addEventListener("readystatechange", function {}, false);

--------------------------------------------------------
html 阶段

1. 创建document对象，解析html页面 | readystate="loading"
2. 执行内置可执行脚本
3. 遇到 async,下载脚本
4. 解析完成 | readystate="interactive"
5. 顺序执行 defer 脚本
6. 触发DOMContentLoaded事件,从同步脚本执行阶段转到异步事件驱动阶段。
7. 文档解析完成，等待资源载入 | readystate="complete", 触发window load 事件驱动
8. 调用异步事件，异步响应输入，网络，计时器过期等。

--------------------------------------------------------
IE

<!-- [if IE 6]>
只在ie6显示
<![endif]-->

<!-- [if lte IE 7]>
只在早于（或等于）ie7版本上显示
<![endif]-->

<!-- [if !IE]<-->
非ie版本上显示
<!--> <![endif]-->

--------------------------------------------------------
javascript 限制

一、
1.没有权限写入和删除客户计算机上的任意文件或列出任意目录
2.没有任何通用的网络能力。当是有Http协议编程，html5 WebSockets

二、
1.可以打开一个新的浏览器窗口，但是一些浏览器会限制
2.可以关闭自己打开的浏览器窗口，必须经过用户确认才能关闭其他窗口
3.HTML FileUpload元素的value属性是只读。
4.不能读取不同服务器载入的文档内容，只能包含该脚本的文档。


--------------------------------------------------------

同源策略

不严格的同源策略
Document.domain = "baidu.com"
可以访问 xx.baidu.com类似的网站

跨域资源共享
Origin:请求头和新的Access-Control-Allow-Origin响应来扩展HTTP

跨文档消息
来自同一个文档的脚本可以传递文本消息到另一个文档的脚本
Window.postMessage();

--------------------------------------------------------
跨站脚本

name = name.replace(/</g, "&lt;").replace(/>/g, "&gt;");

拒绝服务攻击