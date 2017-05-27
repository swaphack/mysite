DOM
文档对象模型(Document Object Model)

DOM是描述HTML元素树形结构，类似XML

1.根据id(属性名称 id)
document.getElementById()
2.根据name(属性名称 name)
document.getElementsByName()
3.根据tag(元素名称)
document.getElementsByTagName()
4.css
document.getElementsByClassName()

document.querySelectorAll()
document.querySelector()

5.document.all[]

----------------------------------------------
元素

var node = document.getElementById();
node.parentNode;
node.childNodes;
node.firstChild, node.lastChild;
node.nextSibling, node.previousSibling;

node.nodeType;
1	Element	代表元素	Element, Text, Comment, ProcessingInstruction, CDATASection, EntityReference
2	Attr	代表属性	Text, EntityReference
3	Text	代表元素或属性中的文本内容。	None
4	CDATASection	代表文档中的 CDATA 部分（不会由解析器解析的文本）。	None
5	EntityReference	代表实体引用。	Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference
6	Entity	代表实体。	Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference
7	ProcessingInstruction	代表处理指令。	None
8	Comment	代表注释。	None
9	Document	代表整个文档（DOM 树的根节点）。	Element, ProcessingInstruction, Comment, DocumentType
10	DocumentType	向为文档定义的实体提供接口	None
11	DocumentFragment	代表轻量级的 Document 对象，能够容纳文档的某个部分	Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference
12	Notation	代表 DTD 中声明的符号。	None

node.nodeValue; // Text 或Comment文本内容
node.nodeName;

----------------------------------------------
属性

变化
"for" -> "htmlFor"
"class" -> "className"

1.获取和设置非标准HTML属性
getAttibute(name)
setAttribute(name, value)
hasAttribute(name)
removeAttribute(name)

var image = document.images[0];
var width = image.getAttribute("WIDTH");
image.setAttribute("class", "thumbnail");

2.数据属性集
HTML，任意一"data-"为前缀的小写的属性都是合法的。
Element.dataset;
data-jquery-test =>dataset.jqueryTest;

node.attributes[0]			// 第一个属性
node.attributes.bgcolor  	// 属性名称为bgcolor
node.attributes.["onload"]  // 属性名称为onload

3.innerHTML, outerHTML

<div>adfakdjflasdjf</div>

innerHTML adfakdjflasdjf
outerHTML <div>adfakdjflasdjf</div>

----------------------------------------------
创建，插入和删除节点

document.createTextNode()
document.createComment()
document.createDocumentFragment()


var node;
node.appendChild();
node.insertBefore();