def case_check(string_1, string_2):
    """Return boolean value depending on whether given strings are of the
    same case. Return -1 if one of given parameters is not a string.

    Parameters
    ----------
    string_1 : Unknown
        First given string
    string_2 : Unknown
        Second given string

    Returns
    -------
    bool
        boolean value (True if given strings are of the same case, else False)
    str
        -1 if one of given parameters is not a string
    """

    if (
        isinstance(string_1, str)
        and isinstance(string_2, str)
        and string_1.isalpha()
        and string_2.isalpha()
    ):
        if (
            string_1.islower() == string_2.islower()
            or string_1.isupper() == string_2.isupper()
        ):
            return True
        return False
    return "-1"
