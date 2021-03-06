function Set() {
	this.values = {};
	this.n = 0;
	this.add.apply(this, arguments);
}

Set.prototype.add = function() {
	for (var i = 0; i < arguments.length; i++) {
		var val = arguments[i];
		var str = Set._v2s(val);
		if (! this.values.hasOwnProperty(str)) {
			this.values[str] = val;
			this.n++;
		}
	}

	return this;
}


Set.prototype.remove = function() {
	for (var i = 0; i < arguments.length; i++) {
		var val = arguments[i];
		var str = Set._v2s(val);
		if (this.values.hasOwnProperty(str)) {
			delete this.values[str];
			this.n--;
		}
	}

	return this;
}

Set.prototype.contains = function(value) {
	return this.values.hasOwnProperty(Set._v2s(value));
}

Set.prototype.size = function() {
	return this.n;
}

Set.prototype.foreach = function(f, context) {
	for (var s in this.values) {
		if (this.values.hasOwnProperty(s)) {
			f.call(context, this.values[s]);
		}
	}
}

Set._v2s = function(val) {
	switch (val) {
		case undefined: return 'u';
		case null: return 'n';
		case true: return 't';
		case false: return 'f';
		default: switch(typeof val) {
			case 'number': return '#' + val;
			case 'string': return '"' + val;
			default: return '@' + objectId(val);
		}

		function objectId(o) {
			var prop = "|**objectId**|";
			if (!o.hasOwnProperty(prop)) 
				o[prop] = Set._v2s.next++;
			return o[prop];
		}
	}
}

Set._v2s.next = 100;

-------------------------------------------
function NonNullSet() {
	Set.apply(this, arguments);
}

NonNullSet.prototype = inherit(Set.prototype);
NonNullSet.prototype.constructor = NonNullSet;

NonNullSet.prototype.add = function() {
	for (var i = 0; i < arguments.length; i++) {
		if (arguments[i] == null) {
			throw new Error("Can't add null or undefined to a NonNullSet.");
		}
	}

	return Set.prototype.add.apply(this, arguments);
}


// 子类工厂
function filteredSetSubClass(superclass, filter) {
	var constructor = function() {
		superclass.apply(this, arguments);
	}

	var proto = constructor.prototype = inherit(superclass.prototype);
	proto.constructor = constructor;
	proto.add = function() {
		for (var i = 0; i < arguments.length; i++) {
			var v = arguments[i];
			if (!filter(v)) 
				throw ("value " + v + " rejected by filter.");
		};

		superclass.prototype.add.apply(this, arguments);
	}

	return constructor;
}