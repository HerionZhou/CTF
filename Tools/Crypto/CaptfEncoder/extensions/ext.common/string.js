const _ = require('underscore');
const _s = require('underscore.string');

var TextEncoder = require("text-encoding").TextEncoder;
var TextDecoder = require("text-encoding").TextDecoder;


/**
   * 将字符串的第一个字母转换为大写。
   * @param str 
   */
function capitalize(str) {
    return _s.capitalize(str);
}

/**
 * 
 * @param str 
 */
function decapitalize(str) {
    return _s.decapitalize(str);
}

/**
 * 
 * @param str 
 */
function swapCase(str) {
    return _s.swapCase(str);
}

/**
 * 
 * @param str 
 */
function titleize(str) {
    return _s.titleize(str);
}

/**
 * 
 * @param str 
 */
function classifye(str) {
    return _s.classifye(str);
}

/**
 * 将下划线或者中划线字符转换成 camelized
 * @param str 
 */
function camelize(str) {
    return _s.camelize(str);
}

/**
 * 将camelized 或者中划线转化成下划线
 * @param str 
 */
function underscored(str) {
    return _s.underscored(str);
}


/**
 * 将camelized 或者下划线转化成中划线
 * @param str 
 */
function dasherize(str) {
    return _s.underscored(str);
}

/**
 * 返回颠倒的字符串
 * @param str 
 */
function reverseString(str) {
    return _s.reverse(str);
}

/**
 * 
 * @param str 
 * @returns 
 */
function xor(str) {
    let result = '';

    for (var i = 0; i < str.length; ++i) {
        result += String.fromCharCode(key ^ str.charCodeAt(i))
    }

    return result;
}
    


/**
 * Translates an ordinal into a character.
 *
 * @param {number} o
 * @returns {string}
 *
 * @example
 * // returns 'a'
 * chr(97);
 */
function chr(o) {
    // Detect astral symbols
    // Thanks to @mathiasbynens for this solution
    // https://mathiasbynens.be/notes/javascript-unicode
    if (o > 0xffff) {
        o -= 0x10000;
        const high = String.fromCharCode(((o >>> 10) & 0x3ff) | 0xd800);
        o = 0xdc00 | (o & 0x3ff);
        return high + String.fromCharCode(o);
    }

    return String.fromCharCode(o);
}

/**
 * Translates a character into an ordinal.
 *
 * @param {string} c
 * @returns {number}
 *
 * @example
 * // returns 97
 * ord('a');
 */
function ord(c) {
    // Detect astral symbols
    // Thanks to @mathiasbynens for this solution
    // https://mathiasbynens.be/notes/javascript-unicode
    if (c.length === 2) {
        const high = c.charCodeAt(0);
        const low = c.charCodeAt(1);
        if (high >= 0xd800 && high < 0xdc00 && low >= 0xdc00 && low < 0xe000) {
            return (high - 0xd800) * 0x400 + low - 0xdc00 + 0x10000;
        }
    }

    return c.charCodeAt(0);
}

/**
 * Converts a character or number to its hex representation.
 *
 * @param {string|number} c
 * @param {number} [length=2] - The width of the resulting hex number.
 * @returns {string}
 *
 * @example
 * // returns "6e"
 * Utils.hex("n");
 *
 * // returns "6e"
 * hex(110);
 */
function hex(c, length = 2) {
    var _c = typeof c == "string" ? ord(c) : c;

    return _c.toString(16).padStart(length, "0");
}

/**
 * Converts a character or number to its binary representation.
 *
 * @param {string|number} c
 * @param {number} [length=8] - The width of the resulting binary number.
 * @returns {string}
 *
 * @example
 * // returns "01101110"
 * bin("n");
 *
 * // returns "01101110"
 * bin(110);
 */
function bin(c, length = 8) {
    var _c = typeof c == "string" ? ord(c) : c;
    return _c.toString(2).padStart(length, "0");
}

/**
 * Converts a string to a unicode charcode array
 *
 * @param {string} str
 * @returns {number[]}
 *
 * @example
 * // returns [72,101,108,108,111]
 * Utils.strToCharcode("Hello");
 *
 * // returns [20320,22909]
 * Utils.strToCharcode("你好");
 */
function strToCharcode(input) {
    var charcode = [];

    for (let i = 0; i < input.length; i++) {
        let ord = input.charCodeAt(i);

        // Detect and merge astral symbols
        if (i < input.length - 1 && ord >= 0xd800 && ord < 0xdc00) {
            const low = input[i + 1].charCodeAt(0);
            if (low >= 0xdc00 && low < 0xe000) {
                ord = ord(input[i] + input[++i]);
            }
        }

        charcode.push(ord);
    }

    return charcode;
}

/**
 *
 * @param input
 * @param encoding
 */
function uint8ArrayToStr(input, encoding) {
    return new TextDecoder(encoding).decode(input);
}

/**
 *
 * @param input
 * @param encoding
 */
function strToUint8Array(input, encoding) {
    return new TextEncoder(encoding).encode(input);
}

/**
 * 
 * @param str 
 * @param search 
 * @param replacement 
 */
function replaceAll(str, search, replacement) {
    replacement = !replacement ? "" : replacement;
    return str.split(search).join(replacement);
}

/**
 * 
 * @param str 
 * @param strToRemove 
 */
function removeAll(str, strToRemove) {
    return replaceAll(str, strToRemove, "");
}





module.exports = {
    capitalize: capitalize,
    decapitalize: decapitalize,
    swapCase: swapCase,
    titleize: titleize,
    classifye: classifye,
    camelize: camelize,
    underscored: underscored,
    dasherize: dasherize,
    reverseString: reverseString,
    xor: xor,
    chr: chr,
    ord: ord,
    hex: hex,
    bin: bin,
    strToCharcode: strToCharcode,
    uint8ArrayToStr: uint8ArrayToStr,
    strToUint8Array: strToUint8Array,
    replaceAll: replaceAll,
    removeAll: removeAll
}