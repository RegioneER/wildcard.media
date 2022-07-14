# -*- coding: utf-8 -*-
from wildcard.media.interfaces import IMediaEnabled
from plone.indexer.decorator import indexer


def _unicode_safe_string_concat(*args):
    """
    concats args with spaces between and returns utf-8 string, it does not
    matter if input was unicode or str
    """
    result = ''
    for value in args:
        result = ' '.join((result, value))
    return result


def SearchableText(obj, text=False):
    return u" ".join((
        obj.id,
        obj.title or u"",
        obj.description or u"",
    ))


@indexer(IMediaEnabled)
def MediaSearchableText(obj):
    text = getattr(obj, 'transcript', None)
    if text is None or text.output is None:
        return SearchableText(obj)
    return _unicode_safe_string_concat(SearchableText(obj), text.output)
