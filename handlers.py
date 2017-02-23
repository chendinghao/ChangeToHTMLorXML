class Handler:
    """
    处理器，处理各种标签,如标题，列表，段落等，主要实现方法在其子类
    """
    # 定义回调函数，调用该类中的函数名为prefix + name　的方法，输入参数为*args
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
    # 定义substitution函数，该函数将作为re.sub函数的第二个参数
    # 该函数的作用是替换制定规则的字符串
        def substitution(match):
            # 只要进入这个函数，就表示有匹配的字符串
            # 若callback返回的字符串为空，则返回蚕蛹完整的匹配
            # 否则返回回调函数中的字符串
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)   #group(0)是完整匹配
            return  result
        return substitution

#　处理函数
class HTMLRenderer(Handler):
    """
    handler类的子类，html渲染类，用来实现添加具体的标签
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        # 匹配字符串转换为html强调字符
        return '<em>%s</em>' %match.group(1)
    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def feed(self,data):
        print(data)
