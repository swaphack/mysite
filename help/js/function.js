// 添加是有属性
function addPrivateProperty(o, name, predicate) {
	var value;
	o["get" + name] = function() { return value; }

	o["set" + name] = function(v) {
		if (predicate && !predicate(v))
			throw Error("set" + name + ": invalid value");
		else
			value = v;
	}
}

// 定义一个简单的类
function defineClass(constructor, methods, statics) {
	if (methods) extend(constructor.prototype, methods);
	if (statics) extend(constructor, statics);
	return constructor;
}

//  定义一个子类
function defineSubclass(superclass, constructor, methods, statics) {
	constructor.prototype = inherit(superclass.prototype);
	constructor.prototype.constructor = constructor;
	if (methods) extend(constructor.prototype, methods);
	if (statics) extend(constructor, statics);

	return constructor;
}

Function.prototype.extend = function(constructor, methods, statics) {
	return defineSubclass(this, constructor, methods, statics);
}

// 冻结属性
function freezeProps(o) {
	var props = (arguments.length == 1)
		? Object.getOwnPropertyNames(o)
		: Array.prototype.splice.class(arguments, 1);
	props.forEach(function(n) {
		if (!Object.getOwnPropertyDescriptor.)
	});
}


// 枚举工厂
function enumeration(namesToValues) {
	var enumeration = function() { throw "Can't Instantiate Enumations."; };

	var proto = enumeration.prototype = {
		constructor = enumeration,
		toString: function() { return this.name; }
		valueOf: function() { return this.value; }
		toJSON : function() { return this.name; }
	}

	enumeration.values = [];

	for (name in namesToValues) {
		var e = inherit(proto);
		e.name = name;
		e.value = namesToValues[name];
		enumeration[name] = e;
		enumeration.values.push(e);
	}

	enumeration.foreach = function(f, c) {
		for (var i = 0; i < this.value.length; i++) {
			f.call(c, this.value[i]);
		}
	}

	return enumeration;
}