from urllib.parse import urlparse
from tldextract import tldextract


def shrunk_url(url_string):
    return url_string.split("//")[1]


def domain_of_url(url_string):
    return (
        tldextract.extract(url_string).domain
        + "."
        + tldextract.extract(url_string).suffix
    )


def url_list(url_string):
    result = (
        [urlparse(url_string).scheme + "://"]
        + urlparse(url_string).netloc.split(".")
        + [component for component in urlparse(url_string).path.split("/") if component]
        + [urlparse(url_string).query]
        + [urlparse(url_string).fragment]
    )
    return [component for component in result if component]
