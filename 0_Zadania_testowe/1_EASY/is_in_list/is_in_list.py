def is_in_list(list_: list, element_to_find: object) -> bool:
    """Return boolean value depending on whether element to find is in list.
    
    Parameters
    ----------
    list_ : list
        A list searched through to find and object
    element_to_find : object
        The object looked for in the list
    
    Returns
    -------
    bool
        boolean value (True if element is found, else False)
    """
    
    for i in list_:
        if i is element_to_find:
            return True
    return False