#!/usr/bin/env python3
# Week7 Excercise html render -
# Student: Brandon Nguyen - Au2018
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None):
        # self.contents = [content]
        self.contents = ([content] if content else [])
        #print("***DEBUG*** contents is:", self.contents)  # to debug test_render2

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))
