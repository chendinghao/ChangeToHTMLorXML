# ChangeToHTMLorXML
《pyhon基础教程》中的第一个项目
　主要是边抄边学习啦，之后会把注释一步一步写上去
 　把文档转换成html或者xml
 
1、一开始的　simple_makeup.py 和　util.py 只是简单地把文本分解成单独处理的块，并且每一个块用一个过滤器（re.sub)
     ------------------------------------------------------------------------------------------------
     python simple_makeup.py <test.input.txt> test_output.html
     ------------------------------------------------------------------------------------------------
     
２、接下来在尝试着拓展其功能
   有四个文件
   分割文件块：util.py
   处理程序: handler.py
   规则：rules.py
   主程序: makeup.py
