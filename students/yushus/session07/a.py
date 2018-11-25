def f(txt, **kwargs):
     attributes = kwargs
     for attribute in kwargs:
          page_attributes = f" {attribute}={attributes[attribute]}"
          print(page_attributes)

f("",style="abc")