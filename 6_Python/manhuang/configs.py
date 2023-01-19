# -*- conding:utf-8 -*-

class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def to_dict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = to_dict(v) if isinstance(v, dict) else v
    return D

default_configs = {
    'login':{
        'user_name':'fhl1993',
        'pwd':'fhl19930321'
    },
    'check_term':'#serverCon>img:nth-child(7)',
    'start_button':'#serverCon>img:nth-child(3)'
}

configs = to_dict(default_configs)
