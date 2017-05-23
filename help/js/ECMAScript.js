// ECMAScript 3中实现的ECMAScript 5功能

// 绑定
if (!Function.prototype.bind) {
	Function.prototype.bind = function(o /*, args*/) {
		var self = this;
		var boundArgs = arguments;

		return function() {
			var args = [], i;
			for (i = 1; i < boundArgs.length; i++) {
				args.push(boundArgs[i]);
			}

			for (i = 1; i < arguments.length; i++) {
				args.push(arguments[i]);
			}

			return self.apply(o, args);
		}
	}
}