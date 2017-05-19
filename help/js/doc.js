-------------------------------------------------------------
void 忽略返回结果，返回undefined

void window.open()

-------------------------------------------------------------
with 创建一个新的作用域，在离开时恢复

a.b = 1
a.c = 2

with (a) {
	b = 1
	c = 2
}

-------------------------------------------------------------
label 类似c语言goto

a: function func() {
	var b = 1; 
}

function test() {
	for (var i = 0; i < 5; i++) {
		if (i == 1) {
			break a
		}
	}
}

-------------------------------------------------------------
debugger 临时断点

-------------------------------------------------------------
严格模式

"use strict"

1.禁止使用with
2.变量要实现声明
3.函数中的this是undefined
4.调用call()或apply()中的this值时第一个传入参数
5.只读属性不可复制，不可扩展对象不能创建新成员
6.不允许八进制

-------------------------------------------------------------
原型

Object.prototype 获取原型对象的引用,Object类本生

Object.create()


-------------------------------------------------------------
属性 getter setter

getter setter
1		1		可读可写
1		0		可读不可写
0		1		可写不可读

var o = {
	data_prop : value,

	get accessor_prop() {}
	set accessor_prop(value) {}
}

-------------------------------------------------------------
属性特性

value
writable
enumerable
configurable

存取器属性特性
get
set
enumerable
configurable

-------------------------------------------------------------
var o = {};
// 创建属性
Object.defineProperty(o, "x", {
	value : 1,
	writable:true,
	enumerable:false,
	configurable:true
})

// 属性描述
Object.getOwnPropertyDescriptor(o, "toString");
// 可配置 configurable:true
Object.defineProperty(o,"x", {value : 2});
// 存取器属性
Object.defineProperty(o,"x", { get : function() { return 0;}});

-------------------------------------------------------------
对象的三个属性
prototype 原型
class 类
extensible 可扩展性

isPrototypeOf 是否继承于
instanceof

// 是否可扩展
Object.isExtensible()

// 设置为不可扩展
Object.preventExtensions()

// 是否可扩展，可配置
Object.isSealed();
// 不可扩展，不可配置
Object.seal()

// 是否冻结
Object.isFrozen()
// 冻结 不可扩展 不可配置 只读
Object.frozen()

-------------------------------------------------------------
序列化
var o = {x : 1, y : { z:[false, null, ""]}};
var s = JSON.stringify(o);
var p = JSON.parse(s);

-------------------------------------------------------------
方法
hasOwnProperty()
propertyIsEnumerable()
isPrototypeOf()
toString()
toLocaleString()
stringify() => toJSON()
valueOf()

-------------------------------------------------------------
数组
1.join(str) 数组转字符串,str是数组元素建插入的字符串
2.reverse() 反转
3.sort() 排序
4.concat(ary)拼接
5.slice(begin,end)切出
6.splice(param) 查找到值为param的位置，切出位置为[0,indexOf(param)-1]的数据
7.push(param) 尾部插入
8.pop() 尾部移除
9.unshift(param)头部插入
10.shift() 头部移除

ECMAScript5
1.forEach(func(value, idx, self) {}) 遍历
2.map(func(value) { return ;} ) 有返回值遍历
3.filter(func(value, idx) { return;}) 过滤
4.every(func(value) { return bool;}) 所有都满足条件
5.some(func(value) { return bool;}) 只要有一个满足条件
6.reduce() reduceRight()
7.indexOf() lastIndexOf()


