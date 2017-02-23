# coding=utf-8


def lines(file):
    for line in file: yield line
    yield '\n'


# blocks生成器实现了前面说明的方法。当生成一个块后，里面的行会被链接成一个字符串，并且将开始和结尾的中的多余的空格删除，得到一个代表块的字符串


def blocks(file):
    """
    读取文件，将文件分成块
    """
    block = []
    for line in lines(file):  # 读取文件的每一行
        if line.strip():      # 去掉string的前后端的空格，判断是否为真
            block.append(line) #　如果为真，将string添加到block中
        elif block:           # 如果line为假，判断block是否为空　
            # 如果不为空，将block中所有元素连接起来成为一个新的string, 元素之间的连接字符为空
            # 去掉新的string的前后端空格，将新string添加到生成器中
            yield ''.join(block).strip()
            block = []  # 重新将block赋值为空，一边读取后面的内容
