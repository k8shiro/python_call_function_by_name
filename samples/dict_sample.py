def function_x(a, b):
    print('----function_x', a, b, '----')


if __name__ == '__main__':
    # dictで定義してしまう方法 
    functions = {'function_x': function_x}


    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = functions[function_name]
    f(a, b)

    # だいぶまともだが関数が増えるたびにdictを更新し続ける必要がある
