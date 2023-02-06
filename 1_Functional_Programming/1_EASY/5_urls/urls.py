from urllib.parse import urlparse
from tldextract import tldextract


def shrunk_url(url_string: str):
    """Return URL address without https:// or http://, depending on which
    protocol is in the address.

    Parameters
    ----------
    url_string : str
        An URL to be shrunked

    Returns
    -------
    str
        An URL string without HTTP/HTTPS protocol.
    """
    return url_string.split("//")[1]


def domain_of_url(url_string: str):
    """Return a main domain from given URL.

    Parameters
    ----------
    url_string : str
        An URL from which main domain will be extracted.

    Returns
    -------
    str
        Concatenated strings of URL domain and suffix.
    """
    return (
        tldextract.extract(url_string).domain
        + "."
        + tldextract.extract(url_string).suffix
    )


def url_list(url_string: str):
    """Return a list of elements of URL.

    Parameters
    ----------
    url_string : str
        An URL string to be splitted into a list of elements.

    Returns
    -------
    list
        List of elements of an URL parameter.
    """
    result = (
        [urlparse(url_string).scheme + "://"]
        + urlparse(url_string).netloc.split(".")
        + [component for component in urlparse(url_string).path.split("/") if component]
        + [urlparse(url_string).query]
        + [urlparse(url_string).fragment]
    )
    return [component for component in result if component]
