lxml.html.formfill
------------------


.. autoclass:: lxml.html.formfill.DefaultErrorCreator
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.formfill.FormNotFound
    :members:
    :undoc-members:
    :private-members:

.. autofunction:: lxml.html.formfill._add_class(el, class_name)

.. autofunction:: lxml.html.formfill._check(el, check)

.. autofunction:: lxml.html.formfill._fill_form(el, values)

.. autofunction:: lxml.html.formfill._fill_multiple(input, value)

.. autofunction:: lxml.html.formfill._fill_single(input, value)

.. autofunction:: lxml.html.formfill._find_elements_for_name(form, name, error)

.. autofunction:: lxml.html.formfill._find_form(el, form_id=None, form_index=None)

.. autofunction:: lxml.html.formfill._find_form_ids(el)

.. autofunction:: lxml.html.formfill._insert_error(el, error, error_class, error_creator)

.. autofunction:: lxml.html.formfill._nons(tag)

.. autofunction:: lxml.html.formfill._select(el, select)

.. autofunction:: lxml.html.formfill._takes_multiple(input)

.. autofunction:: lxml.html.formfill._transform_result(typ, result)

.. autofunction:: lxml.html.formfill.fill_form( el, values, form_id=None, form_index=None, )

.. autofunction:: lxml.html.formfill.fill_form_html(html, values, form_id=None, form_index=None)

.. autofunction:: lxml.html.formfill.fromstring(html, base_url=None, parser=None, **kw)

.. autofunction:: lxml.html.formfill.insert_errors( el, errors, form_id=None, form_index=None, error_class="error", error_creator=default_error_creator, )

.. autofunction:: lxml.html.formfill.insert_errors_html(html, values, **kw)

.. autofunction:: lxml.html.formfill.tostring(doc, pretty_print=False, include_meta_content_type=False, encoding=None, method="html", with_tail=True, doctype=None)

.. autodata:: lxml.html.formfill.XHTML_NAMESPACE

.. autodata:: lxml.html.formfill._form_name_xpath

.. autodata:: lxml.html.formfill._forms_xpath

.. autodata:: lxml.html.formfill._input_xpath

.. autodata:: lxml.html.formfill._label_for_xpath

.. autodata:: lxml.html.formfill._name_xpath

.. autodata:: lxml.html.formfill._options_xpath

.. autodata:: lxml.html.formfill.default_error_creator



