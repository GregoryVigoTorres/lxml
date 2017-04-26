lxml.html.diff
--------------


.. autoclass:: lxml.html.diff.DEL_END
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.DEL_START
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.InsensitiveSequenceMatcher
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.NoDeletes
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.href_token
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.tag_token
    :members:
    :undoc-members:
    :private-members:


.. autoclass:: lxml.html.diff.token
    :members:
    :undoc-members:
    :private-members:

.. autofunction:: lxml.html.diff._contains_block_level_tag(el)

.. autofunction:: lxml.html.diff._fixup_ins_del_tags(doc)

.. autofunction:: lxml.html.diff._merge_element_contents(el)

.. autofunction:: lxml.html.diff._move_el_inside_block(el, tag)

.. autofunction:: lxml.html.diff.cleanup_delete(chunks)

.. autofunction:: lxml.html.diff.cleanup_html(html)

.. autofunction:: lxml.html.diff.compress_merge_back(tokens, tok)

.. autofunction:: lxml.html.diff.compress_tokens(tokens)

.. autofunction:: lxml.html.diff.copy_annotations(src, dest)

.. autofunction:: lxml.html.diff.default_markup(text, version)

.. autofunction:: lxml.html.diff.end_tag(el)

.. autofunction:: lxml.html.diff.expand_tokens(tokens, equal=False)

.. autofunction:: lxml.html.diff.fixup_chunks(chunks)

.. autofunction:: lxml.html.diff.fixup_ins_del_tags(html)

.. autofunction:: lxml.html.diff.flatten_el(el, include_hrefs, skip_tag=False)

.. autofunction:: lxml.html.diff.fragment_fromstring(html, create_parent=False, base_url=None, parser=None, **kw)

.. autofunction:: lxml.html.diff.html_annotate(doclist, markup=default_markup)

.. autofunction:: lxml.html.diff.html_annotate_merge_annotations(tokens_old, tokens_new)

.. autofunction:: lxml.html.diff.htmldiff(old_html, new_html)

.. autofunction:: lxml.html.diff.htmldiff_tokens(html1_tokens, html2_tokens)

.. autofunction:: lxml.html.diff.is_end_tag(tok)

.. autofunction:: lxml.html.diff.is_start_tag(tok)

.. autofunction:: lxml.html.diff.is_word(tok)

.. autofunction:: lxml.html.diff.locate_unbalanced_end(unbalanced_end, pre_delete, post_delete)

.. autofunction:: lxml.html.diff.locate_unbalanced_start(unbalanced_start, pre_delete, post_delete)

.. autofunction:: lxml.html.diff.markup_serialize_tokens(tokens, markup_func)

.. autofunction:: lxml.html.diff.merge_delete(del_chunks, doc)

.. autofunction:: lxml.html.diff.merge_insert(ins_chunks, doc)

.. autofunction:: lxml.html.diff.parse_html(html, cleanup=True)

.. autofunction:: lxml.html.diff.serialize_html_fragment(el, skip_outer=False)

.. autofunction:: lxml.html.diff.split_delete(chunks)

.. autofunction:: lxml.html.diff.split_trailing_whitespace(word)

.. autofunction:: lxml.html.diff.split_unbalanced(chunks)

.. autofunction:: lxml.html.diff.split_words(text)

.. autofunction:: lxml.html.diff.start_tag(el)

.. autofunction:: lxml.html.diff.tokenize(html, include_hrefs=True)

.. autofunction:: lxml.html.diff.tokenize_annotated(doc, annotation)

.. autodata:: lxml.html.diff._body_re

.. autodata:: lxml.html.diff._end_body_re

.. autodata:: lxml.html.diff._ins_del_re

.. autodata:: lxml.html.diff.block_level_container_tags

.. autodata:: lxml.html.diff.block_level_tags

.. autodata:: lxml.html.diff.empty_tags

.. autodata:: lxml.html.diff.end_whitespace_re

.. autodata:: lxml.html.diff.split_words_re

.. autodata:: lxml.html.diff.start_whitespace_re



