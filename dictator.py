class dictator(dict):
    """provides nice lua-like syntactic sugar for python dictionaries"""
    def __init__(self, *args, **kwargs):
        dict.__init__(self, kwargs)

    def __getattribute__(self, name):
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):
        return dict.__setitem__(self, name, value)
