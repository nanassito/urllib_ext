# urllib.parse.ParseResult
Overload `urllib.parse.ParseResult` to be able to use operators like / and &amp; on it.

# Usage
```
import urllib_parse_ParseResult_overloaded
from urllib.parse import urlparse

urlparse("http://domain.tld/foo") / "bar" == urlparse("http://domain.tld/foo/bar")
```