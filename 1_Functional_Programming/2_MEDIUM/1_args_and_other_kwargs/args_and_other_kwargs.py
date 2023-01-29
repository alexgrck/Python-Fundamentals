def list_parameters(*args, **kwargs):
    return {**{index: value for index, value in enumerate(args)}, **kwargs}
