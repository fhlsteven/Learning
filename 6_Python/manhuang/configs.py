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

#转生 [zhuǎn shēng]
#[reincarnation] 佛教指人或动物的转世轮回,灵魂在人死后投胎再生

default_configs = {
    'browser_type':'chrome',  # chrome, edge
    'login':{
        'url':'https://h5game.gowan8.com/?yisdk_param=mZpuX9Lm2M_S&ext_param=ZJ1raKOp',
        'user_name':'fhl1993',
        'pwd':'fhl19930321',
        'cur_index':'1'
    },
    'browser_pos':{
        'x':0,
        'y':0
    },
    'check_term':'#serverCon>img:nth-child(7)',
    'start_button':'#serverCon>img:nth-child(3)',
    'reincarnation': 4,
    'svip_level':0,
    'runtime':'debug',
    'wait_min_morning':5
}

configs = to_dict(default_configs)
