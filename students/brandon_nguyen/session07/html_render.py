#!/usr/bin/env python3
# Week7 Excercise html render -
# Student: Brandon Nguyen - Au2018
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    # abstract_tag = "html"  # to be pure!

    def __init__(self, content=None, **kwargs):
        # self.contents = [content]
        self.contents = [content] if content else []
        self.element_attrs = kwargs if kwargs else {}
        # print("***DEBUG*** contents is:", self.contents)  # to debug test_render2

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents + recursive render(...)
        # TODO how to be pure if ELEMENT has abstract_tag instead.
        # NEXT LINE replacing with _open_tag()
        #out_file.write("<{}>\n".format(self.tag))  # use in part 3

        out_file.write(self._open_tag())
        #out_file.write("\n")
        #
        # out_file.write("<{}".format(self.tag))
        # for k, v in self.element_attrs.items():
        #     out_file.write(" {}=\"{}\"".format(k, v))
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except:
                out_file.write(content)
                out_file.write("\n")
        # out_file.write("</{}>\n".format(self.tag))
        out_file.write(self._close_tag())
        #out_file.write("\n")

    # python private conv opening tags with items in element_attrs
    def _open_tag(self):
        # TODO
        open_tag = ["<{}".format(self.tag)]
        for k, v in self.element_attrs.items():
            open_tag.append(" {}=\"{}\"".format(k, v))
        open_tag.append(">")
        return "".join(open_tag)

    # python pivate conv closing tag
    def _close_tag(self):
        return "</{}>\n".format(self.tag)


# Create sub-classes of Element
class Body(Element):
    tag = "body"


class Html(Element):
    tag = "html"


class P(Element):
    tag = "p"


# in STEP 3
class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        # ONE line no need to loop!
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    # blocking other append
    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


# in STEP 5
class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)

    def append(self, *args):
        raise TypeError("You cannot add content to SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"