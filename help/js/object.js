// 继承
function inherit(p) {
	if (p == null) throw TypeError();
	if (Object.create) {
		return Object.create(p);
	}

	var t = typeof p;
	if (t != "object" && t != "function")
		throw TypeError();

	function f() {};
	f.prototype = p;
	return new f();
}

// 扩展，相同属性，覆盖原有
function extend(o, p) {
	for (prop in p) {
		o[prop] = p[prop];
	}

	return o;
}

// 扩展，相同属性，保留原有
function merge(o, p) {
	for (prop in p) {
		if (o.hasOwnProperty(prop)) 
			continue;
		o[prop] = p[prop];
	}

	return o;
}

// 删除不同名属性
function restrict(o, p) {
	for (prop in o) {
		if (!(prop in p)) 
			delete o.prop;
	}

	return o;
}

// 删除同名属性
function substract(o, p) {
	for (prop in p) {
		delete o[prop];
	}

	return o;
}

// 并集
function union(o, p) {
	return extend(extend({}, o), p);
}

// 交集
function intersection(o, p) {
	return restrict(extend({}, o), p);
}

// 属性名称
function keys(o) {
	if (typeof o !== "object") throw TypeError();
	var result = [];
	for (var prop in o) {
		if (o.hasOwnProperty(prop)) {
			result.push(prop);
		}
	}

	return result;
}

// 获取类名称
function classof(o) {
	if (o == null) {
		return "Null";
	}

	if (o == undefined) {
		return "Undefined";
	}

	return Object.prototype.toString.call(o).slice(8,-1);
}