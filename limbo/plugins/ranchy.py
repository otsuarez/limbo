"""!ranchy <search term> return the rancher metadata value for <search term>"""

import re
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote

import requests

def ranchy(searchterm):
    url = "http://rancher-metadata/latest/{0}"
    url = url.format(quote(searchterm))

    r = requests.get(url)
    results = r.text

    if not results:
        return "sorry, no results found"

    return results

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!ranchy (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return ranchy(searchterm.encode("utf8"))
