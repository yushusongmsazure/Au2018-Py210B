#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element(object):
    """ Default Element class for rendering html """
    tag_name = "html"
    indent = 3
    cur_ind = 0

    def __init__(self, content=None, **kwargs):
        self.html_content = ([content] if content else [])
        self.header_arg = (kwargs if kwargs else {})

    def append(self, new_content):
        self.html_content.append(new_content)

    def render(self, out_file, cur_ind=0):
        if self.header_arg:
            self.writetag(out_file, (" " * cur_ind) + "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">\n")
        else:
            self.writetag(out_file, (" " * cur_ind) + "<{}>\n")

        for htmlitem in self.html_content:
            if type(htmlitem) == str:
                out_file.write((" " * (cur_ind + self.indent)) + "{}\n".format(htmlitem))
            else:
                htmlitem.render(out_file, (cur_ind + self.indent))

        self.writetag(out_file, (" " * cur_ind) + "</{}>\n")

    def writetag(self, out_file, outstring):
        out_file.write(outstring.format(self.tag_name))


class OneLineTag(Element):
    """ subclass of Element for rendering single line html tags """
    tag_name = ""

    def render(self, out_file, cur_ind=0):
        if self.header_arg:
            self.writetag(out_file, (" " * cur_ind) + "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">")
        else:
            self.writetag(out_file, (" " * cur_ind) + "<{}>")

        for htmlitem in self.html_content:
            out_file.write("{}".format(htmlitem))

        self.writetag(out_file, "</{}>\n")


class SelfClosingTag(Element):
    """ subclass of Element for rendering tags with no content """
    tag_name = ""

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Error: Content not allowed for tag.')
        else:
            self.html_content = []

        self.header_arg = (kwargs if kwargs else {})

    def append(self, new_content):
        raise TypeError('Error: Content not allowed for tag. Discarding content.')

    def render(self, out_file, cur_ind=0):
        if self.header_arg:
            self.writetag(out_file, (" " * cur_ind) + "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(" />\n")
        else:
            self.writetag(out_file, (" " * cur_ind) + "<{} />\n")


class A(Element):
    """ subclass of Element for rendering a tags """
    tag_name = "a"

    def __init__(self, link=None, content=None):
        if not link or not content:
            raise TypeError('Error: Value cannot be null.')
        else:
            self.href_link = link
            self.html_content = content

    def render(self, out_file, cur_ind=0):
        out_file.write((" " * cur_ind) + "<a href=\"{}\">{}</a>\n".format(self.href_link, self.html_content))


class H(OneLineTag):
    """ subclass of OneLineTag for rendering h tags """
    def __init__(self, level, content):
        self.tag_name = "h{}".format(level)
        Element.__init__(self, content)


class Html(Element):
    """ subclass of Element for rendering html tags """
    tag_name = "html"

    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)


class Body(Element):
    """ subclass of Element for rendering body tags """
    tag_name = "body"


class P(Element):
    """ subclass of Element for rendering p tags """
    tag_name = "p"


class Head(Element):
    """ subclass of Element for rendering head tags """
    tag_name = "head"


class Title(OneLineTag):
    """ subclass of OneLineTag for rendering title tags """
    tag_name = "title"


class Hr(SelfClosingTag):
    """ subclass of SelfClosingTag for rendering hr tags """
    tag_name = "hr"


class Br(SelfClosingTag):
    """ subclass of SelfClosingTag for rendering br tags """
    tag_name = "br"


class Ul(Element):
    """ subclass of Element for rendering ul tags """
    tag_name = "ul"


class Li(Element):
    """ subclass of Element for rendering li tags """
    tag_name = "li"


class Meta(SelfClosingTag):
    """ subclass of SelfClosingTag for rendering meta tags """
    tag_name = "meta"
