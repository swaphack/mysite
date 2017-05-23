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

-------------------------------------------------------------
函数 闭包

var strict = (function() { return !this; } ());

等价于
function isStrict() { return !this; }

var strict = isStrict();

定义对象的函数
var calculator = {
	x : 1,
	y : 1,

	getRadius : function() {
		return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
	}
}

-------------------------------------------------------------
严格模式下，函数里的this是undefined
非严格模式下，函数里的this是全局对象

-------------------------------------------------------------
可选参数
function getPropertyName(o, /*optional*/ a) {
	a = a || [];
}

/*optional*/ 可选参数标识

-------------------------------------------------------------
可变长度的实参
function(x, y, z) {
	if (arguments.length != 3) {

	}
}


function varargs(/*...*/) {
	var len = arguments.length;
	for (var i = 0; i < len; i++) {
		var value = arguments[i];
	}

}

-------------------------------------------------------------
caller 非标准
callee 标准

严格模式下，读写会错

非严格模式下

var func = function(x) {
	if (x <= 1) return 1;
	return x * arguments.callee(x-1);
}

-------------------------------------------------------------
传入参数的检查

-------------------------------------------------------------
对象
var o = {square : function(x) { return x * x;} }
var y = o.square(2);
类数组：
var a = [function(x) { return x * x}, 20];
a[0](a[1]);

-------------------------------------------------------------
自定义函数属性

uniqueInterger.counter = 0;

function uniqueInterger() {
	return uniqueInterger.counter++;
}

uniqueInterger[1] = 1;

-------------------------------------------------------------
注意
function constfuncs() {
	var funcs = [];

	for (var i = 0; i < 10; i++) {
		funcs[i] = function() { return i; }
	}

	return funcs;
}

var funcs = constfuncs();
funcs[5]() => return 10;

-------------------------------------------------------------
function checkArgs(args) {
	var actual = args.length; // 实际传入参数个数
	var expected = args.callee.length; // 期望传入参数个数
	if (actual != expected) {

	}
}

-------------------------------------------------------------
call apply
第一个参数是函数母体对象,名称是函数名
传入参数不同，call 参数列表， aplly 数组
f.call(o, 1, 2);
f.aplly(o, [1,2]);

-------------------------------------------------------------
bind 把函数绑定到对象
function add(y) { return this.x + y; }
var o = {x : 1};
var g = f.bind(o);
g(2)

function bind(f, o) {
	if (f.bind) return f.bind(o);
	else return function() {
		return f.aplly(o, arguments);
	}
}


var sum	= function(x, y) { return x + y; }
var succ = sum.bind(null, 1);
succ(2) => 3, x绑定到1,传入实参2绑定到y

-------------------------------------------------------------
函数构造

var f = new Function("x", "y", "return x * y;");
var f = function(x,y) { return x * y; }

Function 构造函数
1.可在运行时动态创建编译
2.效率低，因为1
3.创建的函数不能使用次作用域


function isFunction(x) {
	return Object.prototype.toString.call(x) == "[object Function]";
}

-------------------------------------------------------------
函数式编程

不完全函数

记忆函数

-------------------------------------------------------------
类的创建

1.
function Range(from, to) { // 大写
	this.from = from;
	this.to = to;
}

Range.prototype = {
	includes = function(x) {
		return this.from <= x && x <= this.to;
	},

	foreach : function(f) {
		for (var x = Math.ceil(this.from); i <= this.to; x++) {
			f(x);
		}
	},

	toString : function() {
		return "(" + this.from + "..." + this.to + "}";
	}
}

var r = range(1, 4); // 小写

2.

function Range(from, to) { // 大写
	this.from = from;
	this.to = to;
}

Range.prototype = {
	constructor : Range, // 显示构造函数
}

Range.prototype.includes = function(x ) { ...}

var r = new Range(1, 4);

-------------------------------------------------------------
不定参数的类创建

function Set(/*array*/) {
	if (arguments.length !== 1 && isArrayLike(arguments[0]))
		this.add.apply(this, arguments[0]);
	else if (arguments.length > 0) 
		this.add.apply(this, arguments);
}


function SetFromArray(a) {
	Set.apply(this, a);
}

SetFromArray.prototype = Set.prototype;

var s = new SetFromArray[1,2,3];
s instanceof Set => true

-------------------------------------------------------------
子类

B.prototype = inherit(A.prototype);
B.prototype.constructor = B;

组合优于继承

-------------------------------------------------------------
// 定义不可枚举的属性
(function() {
	Object.defineProperty(Object.prototype, "objectId", {
		get : idGetter,
		enumerable : false,
		configurable : false
	});

	function idGetter() {
		if (!(idprop in this)) {
			if (!Object.isExtensible(this))
				throw Error("Can't define id for nonetensible objects.");
			Object.defineProperty(this, idprop, {
				value: nextid++;
				writable: false;
				enumerable: false;
				configurable: false;
			});

			return this[idprop];
		}

		var idprop = "|**objectId**|";
		var nextid = 1;
	}
} ());


-------------------------------------------------------------
命名空间

1.
var sets = {}
sets.SingletonSet = sets.AbstractEnumerableSet.extend(...);

var s = new sets.SingletonSet(1);

2.
var collections;
if (!collections) collections = {};
collections.sets = {}

3.
导出私有
var collections;
if (!collections) collections = {};
(1)
collections.sets = (function namespace() {
	return { 
		AbstractSet: AbstractSet,
		NotSet: NotSet,
	}
});

(2)
collections.sets = (new function namespace() {
	this.AbstractSet = AbstractSet;
	this.NotSet = NotSet;
});

(3)
collections.sets = {}


(new function namespace() {
	collections.sets.AbstractSet = AbstractSet;
	collections.sets.NotSet = NotSet;
}());

-------------------------------------------------------------
javaScript
<script type="application/javaScript;version=1.8" />

let 
1.可以作为变量生命，类似var，但是是局部内，超出作用域就无效
{
	let x = 1;
}

2.解构赋值
let [x,y] = [1,2]

3.迭代器
function counter(start) {
	let nextValue = Math.round(start);
	return {
		next : function() {
			return nextValue++;
		}
	}
}

__iterator__


4.生成器
function range(min, max) {
	for (let i = Math.ceil(min); i <= max; i++)
		yield i;
}

for (let n in range(1,10))
	console.log(n);

-----------------
function fibonacci() {
	let x = 0, y = 1;
	while (true) {
		yield y;
		[x,y] = [y, x + y];
	}
}

f = fibonacci();
for (let i = 0; i < 10; i++) {
	f.next();
}

f.close();

5.数组推导
let eventsquares = [x * x for (x in range(1,10)) if (x % 2 == 0)]

let eventsquares = []

for (x in range(1,10)) {
	if (x % 2 == 0) {
		eventsquares.push(x * x);
	}
}

6.生成器表达式
let h = (f(x) for (x in g))

7.函数简写
let succ = function(x)x+1, yes = function() true;

8.
try {

}catch(e if e instanceof Object) {

}finally {
	
}
