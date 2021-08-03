# @Author ZhangGJ
# @Date 2021/08/03 10:03

class SingletonEnv(object):
    __isinstance = None
    profile = None

    def __init__(self, *args):
        if len(args) == 0:
            pass
        else:
            if self.profile is None:
                self.profile = args

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance


if __name__ == '__main__':
    s = SingletonEnv()
    p = s.profile
    ss = SingletonEnv('')
    pp = ss.profile
    s1 = SingletonEnv('dev')
    p1 = s1.profile
    s2 = SingletonEnv('bug')
    p2 = s2.profile
    p3 = s.profile
    print()
