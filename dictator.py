class dictator(dict):
    """provides nice lua-like syntactic sugar for python dictionaries"""
    def __init__(self, arg=[], **kwargs):
        # jumping through a couple of hoops to allow fancy initialization in
        # classical dictionary style
        d = {}
        if isinstance(arg, dict):
            for k in arg:
                d[k] = arg[k]
        elif isinstance(arg, list):
            print arg
            for k,v in arg:
                d[k] = v
        dict.__init__(self, d, **kwargs)

    def __getattribute__(self, name):
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):
        return dict.__setitem__(self, name, value)
