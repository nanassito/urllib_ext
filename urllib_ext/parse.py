from urllib.parse import ParseResult
from urllib.parse import urlparse as std_urlparse


class Url(ParseResult):
    def __truediv__(self: "Url", right: str) -> "Url":
        url_parts = list(self)
        url_parts[2] = self.path.rstrip("/") + "/" + right.lstrip("/")
        return Url(*url_parts)


def urlparse(text: str) -> Url:
    return Url(*std_urlparse(text))
