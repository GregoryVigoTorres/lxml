lxml.html.clean
---------------


.. autoclass:: lxml.html.clean.Cleaner
    :members:
    :undoc-members:
    :private-members:

.. autofunction:: lxml.html.clean._break_text(text, max_width, break_character)

.. autofunction:: lxml.html.clean._insert_break(word, width, break_character)

.. autofunction:: lxml.html.clean._is_javascript_scheme(s)

.. autofunction:: lxml.html.clean._link_text(text, link_regexes, avoid_hosts, factory)

.. autofunction:: lxml.html.clean._transform_result(typ, result)

.. autofunction:: lxml.html.clean.autolink(el, link_regexes=_link_regexes, avoid_elements=_avoid_elements, avoid_hosts=_avoid_hosts, avoid_classes=_avoid_classes)

.. autofunction:: lxml.html.clean.autolink_html(html, *args, **kw)

.. autofunction:: lxml.html.clean.fromstring(html, base_url=None, parser=None, **kw)

.. autofunction:: lxml.html.clean.tostring(doc, pretty_print=False, include_meta_content_type=False, encoding=None, method="html", with_tail=True, doctype=None)

.. autofunction:: lxml.html.clean.word_break(el, max_width=40, avoid_elements=_avoid_word_break_elements, avoid_classes=_avoid_word_break_classes, break_character=unichr(0x200b))

.. autofunction:: lxml.html.clean.word_break_html(html, *args, **kw)

.. autofunction:: lxml.html.clean.xhtml_to_html(xhtml)

.. autodata:: lxml.html.clean.XHTML_NAMESPACE

.. autodata:: lxml.html.clean._avoid_classes

.. autodata:: lxml.html.clean._avoid_elements

.. autodata:: lxml.html.clean._avoid_hosts

.. autodata:: lxml.html.clean._avoid_word_break_classes

.. autodata:: lxml.html.clean._avoid_word_break_elements
    :noindex:

.. autodata:: lxml.html.clean._break_prefer_re

.. autodata:: lxml.html.clean._conditional_comment_re

.. autodata:: lxml.html.clean._css_import_re

.. autodata:: lxml.html.clean._css_javascript_re

.. autodata:: lxml.html.clean._find_external_links

.. autodata:: lxml.html.clean._find_styled_elements

.. autodata:: lxml.html.clean._link_regexes

.. autodata:: lxml.html.clean.clean

.. autodata:: lxml.html.clean.clean_html



