#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = "html"

    def __init__(self, content=None, **kwargs):
        self.html_content = ([content] if content else [])
        self.header_arg = (kwargs if kwargs else {})

    def append(self, new_content):
        self.html_content.append(new_content)

    def render(self, out_file):
        if self.header_arg:
            self.writetag(out_file, "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">\n")
        else:
            self.writetag(out_file, "<{}>\n")

        for htmlitem in self.html_content:
            if type(htmlitem) == str:
                out_file.write("{}\n".format(htmlitem))
            else:
                htmlitem.render(out_file)

        self.writetag(out_file, "</{}>\n")
    
    def writetag(self, out_file, outstring):
        out_file.write(outstring.format(self.tag_name))


class OneLineTag(Element):
    tag_name = ""

    def render(self, out_file):
        if self.header_arg:
            self.writetag(out_file, "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">")
        else:
            self.writetag(out_file, "<{}>")

        for htmlitem in self.html_content:
            out_file.write("{}".format(htmlitem))

        self.writetag(out_file, "</{}>\n")


class SelfClosingTag(Element):
    tag_name = ""

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Error: Content not allowed for tag.')
        else:
            self.html_content = []

        self.header_arg = (kwargs if kwargs else {})

    def append(self, new_content):
        raise TypeError('Error: Content not allowed for tag. Discarding content.')

    def render(self, out_file):
        if self.header_arg:
            self.writetag(out_file, "<{}")
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(" />\n")
        else:
            self.writetag(out_file, "<{} />\n")


class A(Element):
    tag_name = "a"

    def __init__(self, link=None, content=None):
        if not link or not content:
            raise TypeError('Error: Value cannot be null.')
        else:
            self.href_link = link
            self.html_content = content

    def render(self, out_file):
        out_file.write("<a href=\"{}\">{}</a>\n".format(self.href_link, self.html_content))


class Html(Element):
    tag_name = "html"


class Body(Element):
    tag_name = "body"


class P(Element):
    tag_name = "p"


class Head(Element):
    tag_name = "head"


class Title(OneLineTag):
    tag_name = "title"


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"
