class dictator(dict):
    """provides nice lua-like syntactic sugar for python dictionaries,
    sacrificing access to object methods for uncompromising key access via
    attributes"""
    def __getattribute__(self, name):
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):
        return dict.__setitem__(self, name, value)

class anarchist(dict):
    """provides nice lua-like syntactic sugar for python dictionaries, which
    only works for those keys which are not already object attributes. Easier to
    shoot yourself in the foot but more convenient"""
    def __getattr__(self, name):
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):
        return dict.__setitem__(self, name, value)

   
