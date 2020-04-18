from urllib_ext.parse import urlparse

import pytest


@pytest.mark.parametrize(
    ("left", "right", "result"),
    [
        ("http://domain.tld/foo", "bar", "http://domain.tld/foo/bar"),
        ("http://domain.tld", "bar", "http://domain.tld/bar"),
        ("http://domain.tld/", "/foo/bar", "http://domain.tld/foo/bar"),
        ("http://domain.tld/foo?q=1", "bar", "http://domain.tld/foo/bar?q=1"),
    ],
)
def test_truediv(left, right, result):
    assert urlparse(left) / right == urlparse(result)
