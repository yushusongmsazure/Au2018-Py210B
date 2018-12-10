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

    def __init__(self, content=None):
        # self.contents = [content]
        self.contents = ([content] if content else [])
        # print("***DEBUG*** contents is:", self.contents)  # to debug test_render2

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents + recursive render(...)
        # TODO how to be pure if ELEMENT has abstract_tag instead.
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except:
                out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


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
        # loop through the list of contents
        out_file.write("<{}>".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except:
                out_file.write(content)
                # out_file.write("\n")  # OneLineTage does not need \n
        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "title"
