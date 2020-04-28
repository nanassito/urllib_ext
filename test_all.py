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


def test_recurse_truediv():
    u = urlparse("http://domain.tld") / "foo"
    u /= "bar"
    assert u == urlparse("http://domain.tld/foo/bar")


def test_str():
    assert str(urlparse("http://domain.tld/foo")) == "http://domain.tld/foo"
