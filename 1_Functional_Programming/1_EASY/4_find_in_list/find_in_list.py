from collections import namedtuple


def find_item(list_, key_):
    result_tuple = namedtuple(typename="Result", field_names=["value", "index"])
    for index, value_ in enumerate(list_):
        if key_ == value_:
            return result_tuple(value=value_, index=index)
    return tuple()
