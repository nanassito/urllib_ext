from urllib.parse import ParseResult


def truediv(left: ParseResult, right: str) -> ParseResult:
    """urlparse("http://domain.tld/foo") / "bar" == urlparse("http://domain.tld/foo/bar")"""
    url_parts = list(left)
    url_parts[2] = left.path.rstrip("/") + "/" + right.lstrip("/")
    return ParseResult(*url_parts)


ParseResult.__truediv__ = truediv