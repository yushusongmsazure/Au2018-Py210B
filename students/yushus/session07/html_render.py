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

    def get_attributes(self, attributes):
        page_attributes = ""
        if self.attributes:
            for attribute in self.attributes:
                page_attributes = f"{page_attributes} {attribute}=\"{self.attributes[attribute]}\""
        return page_attributes

    def render(self, out_file):
        page_attributes = self.get_attributes(self.attributes)

        for content in self.contents:
            out_file.write(f"<{self.tag}")
            out_file.write(f"{page_attributes}>\n")

            if isinstance(content, Element):
                content.render(out_file)
            elif isinstance(content, str):
                out_file.write(f"{content}")
            else:
                raise TypeError("Cannot render!!")
            out_file.write("\n")
            out_file.write(f"</{self.tag}>\n")

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
        out_file.write(f"<{self.tag}>")
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    pass

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"



