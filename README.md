# urllib.parse.ParseResult
Overload `urllib.parse.ParseResult` to be able to use operators like / and &amp; on it.

# Usage
```
from urllib_ext.parse import urlparse

urlparse("http://domain.tld/foo") / "bar" == urlparse("http://domain.tld/foo/bar")
```
