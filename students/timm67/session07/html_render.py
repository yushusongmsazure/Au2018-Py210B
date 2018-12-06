#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    _tag = str('html')
    indent = str('    ')

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self._content = [content]
        else:
            self._content = []

    def append(self, new_content):
        if new_content is not None:
            self._content.append(new_content)

    def render(self, out_fd, indent_in=''):

        try:
            out_fd.write('{0}<{1}>\n'.format(indent_in, self._tag))
            # loop through the list of contents:
            for content in self._content:
                try:
                    content.render(out_fd, (indent_in + self.indent))
                except AttributeError:
                    out_fd.write('{0}{1}\n'.format(indent_in + self.indent, content))
            out_fd.write('{0}</{1}>\n'.format(indent_in, self._tag))
        except IOError:
            print("Element: I/O Error on render")
            return

class OneLineTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_fd, indent_in=''):
        try:
            out_fd.write('{0}<{1}> '.format(indent_in, self._tag))
            try:
                self._content[0].render(out_fd, indent_in + self.indent)
            except AttributeError:
                out_fd.write('{0}{1}'.format(indent_in, self._content[0]))
            out_fd.write('{0}</{1}>\n'.format(indent_in, self._tag))
        except IOError:
            print("OneLineTag: I/O Error on render")
            return

class SelfClosingTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_fd, indent_in=''):
        if not indent_in:
            if self._indent_count > 0:
                self._indent = ' ' * self._indent_count
        else:
            self._indent = indent_in

        try:
            out_fd.write('{0}<{1}> '.format(self._indent, self._tag))

            #TODO: add attributes here

            out_fd.write(' />\n')
        except IOError:
            print("SelfClosingTag: I/O Error on render")
            return

class Html(Element):
    _tag = str('html')
    _indent_count = 0 * 5

class Head(Element):
    _tag = str('head')
    _indent_count = 0 * 5

class Body(Element):
    _tag = str('body')
    _indent_count = 1 * 5

class P(Element):
    _tag = str('p')
    _indent_count = 2 * 5

class Title(OneLineTag):
    _tag = str('title')
    _indent_count = 0
