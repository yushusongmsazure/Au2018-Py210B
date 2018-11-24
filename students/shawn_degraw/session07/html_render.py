#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = "html"

    def __init__(self, content=None, **kwargs):
        if content:
            self.html_content = [content]
        else:
            self.html_content = []

        if kwargs:
            self.header_arg = kwargs
        else:
            self.header_arg = {}

    def append(self, new_content):
        self.html_content.append(new_content)

    def render(self, out_file):
        if self.header_arg:
            out_file.write("<{}".format(self.tag_name))
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">\n")
        else:
            out_file.write("<{}>\n".format(self.tag_name))
        for htmlitem in self.html_content:
            if type(htmlitem) == str:
                out_file.write("{}\n".format(htmlitem))
            else:
                htmlitem.render(out_file)
        out_file.write("</{}>\n".format(self.tag_name))


class OneLineTag(Element):
    tag_name = ""

    def render(self, out_file):
        if self.header_arg:
            out_file.write("<{}".format(self.tag_name))
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(">")
        else:
            out_file.write("<{}>".format(self.tag_name))
        for htmlitem in self.html_content:
            out_file.write("{}".format(htmlitem))
        out_file.write("</{}>\n".format(self.tag_name))


class SelfClosingTag(Element):
    tag_name = ""

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Error: Content not allowed for tag.')
        else:
            self.html_content = []

        if kwargs:
            self.header_arg = kwargs
        else:
            self.header_arg = {}

    def append(self, new_content):
        raise TypeError('Error: Content not allowed for tag. Discarding content.')

    def render(self, out_file):
        if self.header_arg:
            out_file.write("<{}".format(self.tag_name))
            for k, v in self.header_arg.items():
                out_file.write(" {}=\"{}\"".format(k, v))
            out_file.write(" />\n")
        else:
            out_file.write("<{} />\n".format(self.tag_name))


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
