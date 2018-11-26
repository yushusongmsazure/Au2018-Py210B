#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
HTML Renderer assignment
"""

import os
import random
import re
import sys

from collections import defaultdict

# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **attributes):
        if content:
            self.contents = [content]
        else:
            self.contents = []

        self.attributes = attributes
    
    def _open_tag(self):
        return f"<{self.tag}{self._get_attributes()}>"

    def _close_tag(self):
        return f"</{self.tag}>"

    def _get_attributes(self):
        page_attributes = ""
        if self.attributes:
            for attribute in self.attributes:
                page_attributes = f"{page_attributes} {attribute}=\"{self.attributes[attribute]}\""
        return page_attributes

    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write("\n")

        for content in self.contents:
            if isinstance(content, Element):
                content.render(out_file)
            elif isinstance(content, str):
                out_file.write(f"{content}")
                out_file.write("\n")
            else:
                raise TypeError("Cannot render!!")

        out_file.write(self._close_tag())
        out_file.write("\n")

    def append(self, new_content):
        self.contents.append(new_content)

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def append(self, content):
        raise NotImplementedError

    def render(self, out_file):
        out_file.write(super()._open_tag())
        out_file.write(self.contents[0])
        out_file.write(super()._close_tag())
        out_file.write("\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **attributes):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **attributes)

    def render(self, outfile):
        tag = super()._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **attributes):
        attributes["href"] = link
        super().__init__(content, **attributes)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class Header(OneLineTag):
    def __init__(self, level, content=None, **attributes):
        self.tag = f"h{level}"
        super().__init__(content, **attributes)
