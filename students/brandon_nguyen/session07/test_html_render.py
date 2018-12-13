# Week7 Excercise html render - test file.
# Student: Brandon Nguyen - Au2018
"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier
# to test everything in a module.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

########
# Step 1
########


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()
    # print(file_contents)
    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

    # making sure we have the right count on root tag "html"
    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1
    # un-comment to see print
    # assert False  # to see the print statement in line 74 - only failed HERE.


# # Uncomment this one after you get the one above to pass
# # Does it pass right away?
def test_render_element2():
    """
     Tests whether the Element can render two pieces of text
     So it is also testing that the append method works correctly.

     It is not testing whether indentation or line feeds are correct.
     """
    e = Element()
    e.append("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

    # assert False


# # ########
# # # Step 2
# # ########

# # tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)

    #  assert file_contents.startswith("<html>")  #failed later with doctype
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


# Testing sub element with correct body
def test_sub_element2():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    body = Body()
    str = "Another small paragraph.\nThis one with multiple lines."
    body.append(P("A 1st small perargraph."))
    body.append(P(str))
    page.append(body)

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "A 1st small perargraph." in file_contents
    assert str in file_contents

    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    assert file_contents.count("<p>") == 2
    assert file_contents.count("</p>") == 2

    #assert False


#######################################
# Step 3
# Test Head(Element), Title(OneLineTag)
#######################################

# Add your tests here!
def test_head():
    page = Html()
    body = Body()
    page.append(Head("This is some text in HEADER!"))
    body.append(P("A simple paragraph."))
    page.append(body)

    file_contents = render_result(page).strip()
    print(file_contents)

    assert("This is some text in HEADER!") in file_contents
    assert("A simple paragraph.") in file_contents

    # assert file_contents.startswith("<html>")  #will failed with Doctype
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "<body>" in file_contents
    assert "</body>" in file_contents
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    assert file_contents.endswith("</html>")

    assert file_contents.count("<head>") == 1
    assert file_contents.count("</head>") == 1

    # assert False


# to Test new subclass of OneLineTag class - Tittle
def test_title():
    e = Title("This is a Title")
    with pytest.raises(NotImplementedError):  # test_one_line_tag_append
        e.append("to see the test failed here")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("This is a Title") in file_contents
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")

    assert "\n" not in file_contents


############################################
# Step 4
# Testing and coding for elements attributes.
# **kwargs adding in.
############################################
def test_attributes():
    # attrs = {'class': 'intro'}
    # e = P('some content', **attrs)
    e = P("A short test paragraph.", style="text-align: center", id="intro")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("A short test paragraph.") in file_contents
    assert file_contents.startswith("<p ")
    assert file_contents.endswith("</p>")
    assert ('style="text-align: center"') in file_contents
    assert ('id="intro"') in file_contents

    assert ('<p style="text-align: center" id="intro">\n') in file_contents

    # test closing bracket to the opening tag
    assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
    assert file_contents[:file_contents.index(">")].count(" ") == 3

    #assert False


############################################
# Step 5
# Testing and coding for elements attributes.
# Hr(SelfClosingTag), Br(SelfClosingTag)
############################################

def test_hr():
    """a simple horizontal rule with no attributes"""
    hr = Hr()
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr />\n'


def test_hr_attr():
    """a simple horizontal rule with attributes"""
    hr = Hr(width=400)
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'

    #assert False


def test_br():
    br = Br()
    file_contents = render_result(br)
    print(file_contents)
    assert file_contents == "<br />\n"


def test_content_in_br():
    with pytest.raises(TypeError):
        br = Br("some content")


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = Br()
        br.append("some content")


############################################
# Step 6
# Testing anchor.
############################################
def test_anchor():
    a = A("http://google.com", "link to google")
    file_contents = render_result(a)
    print(file_contents)
    assert ('<a href="http://google.com">link to google</a>') in file_contents


############################################
# Step 7
# Testing H(OneLineTage), Ul(Element), Li(Element).
############################################
def test_h_header():
    h_name = "This is a Header."
    h2 = H(2, h_name)
    file_contents = render_result(h2)
    print(file_contents)

    assert file_contents.startswith("<h2>")
    assert file_contents.endswith("</h2>\n")
    assert h_name in file_contents

    # assert False


def test_li_attr():
    """ Test list tag """
    li_txt = "This is second item"
    li = Li(li_txt, style="color: red")
    file_contents = render_result(li)
    print(file_contents)
    assert ('<li style="color: red">\n') in file_contents


def test_ul_attr():
    """ Test unordered list tag  with attributes"""
    ul = Ul(id="TheList", style="line-height:200%")
    file_contents = render_result(ul)
    print(file_contents)
    assert ('<ul id="TheList" style="line-height:200%">\n') in file_contents


############################################
# Step 8
# Testing:
#   doctype Html(Element) overridding render.
#   Meta(SelfClosingTag)
############################################
def test_html_doctype():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    assert("<!DOCTYPE html>") in file_contents
    print(file_contents)

    assert file_contents.endswith("</html>")
    # assert False


def test_meta_attrs():
    pass


# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * Element.indent + "<")

    assert lines[4].startswith(3 * Element.indent + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\html>

    More complex indentation should be tested later.
    """
    e = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")
