# dictator & anarchist #

Small, almost useless Python module, offering Lua-style syntactic table access sugar to dictionaries. 

In case of using the dictator class you, in return, won't be able to use any traditional dictionaryobject methods. 

In case of using the anarchist class you, on the other hand, will easily shoot yourself in the foot if you try to put strings into the dictionary which are already existing as an object attribute name.

## Features ##

Syntactic sugar for (string) keys. Does away with the tedious "bracket-quote-string-quote-bracket" subscripting notation. Instead, simply access the dictionary with the key string as  _attribute_ like so:

>>> from dictator import dictator
>>> d = dictator()
>>> d.some_string_key = 42
>>> print d
{'some_string_key': 42}

Of course, the following still works:

>>> d["some fancy longer string"] = 23
>>> print d
{'some fancy longer string': 23, 'some_string_key': 42}

Trying to access an attribute of the object that simply does not exist as a key in the dictionary will _always_ result in a KeyError.

Also, all the obscure ways to instantiate a "normal" dictionary are still supported:

>>> d = dictator({"a":23}, fettemama=42)
>>> print d
{'a': 23, 'fettemama': 42}

Instantiation with a list of tuples also works:

>>> d = dictator([("fettemama",42)])
>>> print d
{'fettemama': 42}

The anarchist class can do anything of the above, just import it like so:
>>> from dictator import anarchist

(The dictator idea came first, that's why the module is named after him (or her))

## Limitations & Differences ##

As mentioned, any code relying on direct access to object methods, such as ".keys()" or
".pop()" will not work in case of the dictator class, because trying to call these will be interpreted as attempted dictionary element access. 

Thus, the way you use dictionaries is pretty much _dictated_. 

Of course, the anarchist doesn't need such stupid limitations, but that's also why (s)he "can't have nice things". (Such as the "security" of being able to use the syntactic sugar for every string that can legally be used as object attribute. Some strings just remain reserved.) 

