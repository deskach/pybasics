import socket

class Resolver(object):

    def __init__(self):
        self._cache = {}


    def __call__(self, host):
        """ __call__ allows to create 'callable' classes. 
            These serves like functions which maintains state 
            between calls 
        """
        
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)

        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, name):
        return name in self._cache

def sequence_class(immutable):
    return tuple if immutable else list

def hypervolume(length, *lengths):
    v = length
    for l in lengths:
        v *= l
    
    return v

def tag(name, **attributes):
    result = '<' + name;
    for key, value in attributes.items():
        result += ' %s="%s"' % (key, value)
    result += '>'

    return result