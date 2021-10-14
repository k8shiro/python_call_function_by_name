from os import system

def function_x(a, b):
    print('----function_x', a, b, '----')


if __name__ == '__main__':
    # globalsから関数を引っ張ってくる方法 
    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = globals()[function_name]
    f(a, b)

    # globalsの代わりにlocalsでもよい
    print('--globals--', globals())
    print('--locals--', locals())


    # importしている関数も呼び出せてしまうのでちょっと危険
    function_name = 'system'
    f = globals()[function_name]
    f('ls -la')
    

