// 处理 ie bug:
// 在多数ie 版本中，如果o的属性拥有一个不可枚举的同名属性，则for/in 循环不会枚举对象o的可枚举属性
// 也就是说，将不会正确地处理注入toString的属性
var extend = (function() {
    for (var p in { toString: null }) {
        return function extend(o) {
            for (var i = 1; i < arguments.length; i++) {
                var source = arguments[i];
                for (var prop in source)
                    o[prop] = source[prop];
            }

            return o;
        }
    }

    return function patched_extend(o) {
        for (var i = 1; i < arguments.length; i++) {
            var source = arguments[i];
            for (var prop in source)
                o[prop] = source[prop];
        }
        for (var i = 1; i < protoprops.length; i++) {
            prop = protoprops[i];
            if (source.hasOwnProperty(prop))
                o[prop] = source[prop];
        }
    }
}());
