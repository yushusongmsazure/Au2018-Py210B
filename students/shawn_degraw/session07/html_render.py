#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = "html"

    def __init__(self, content=None):
        if content:
            self.html_content = [content]
        else:
            self.html_content = []

    def append(self, new_content):
        self.html_content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag_name))
        for htmlitem in self.html_content:
            if type(htmlitem) == str:
                out_file.write("{}\n".format(htmlitem))
            else:
                htmlitem.render(out_file)
        out_file.write("</{}>\n".format(self.tag_name))


class Html(Element):
    tag_name = "html"


class Body(Element):
    tag_name = "body"


class P(Element):
    tag_name = "p"


class Head(Element):
    tag_name = "head"


class OneLineTag(Element):
    tag_name = "title"

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag_name))
        for htmlitem in self.html_content:
            out_file.write("{}".format(htmlitem))
        out_file.write("</{}>\n".format(self.tag_name))


class Title(OneLineTag):
    tag_name = "title"