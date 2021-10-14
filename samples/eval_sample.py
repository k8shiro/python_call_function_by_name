def function_x(a, b):
    print('----function_x', a, b, '----')


if __name__ == '__main__':
    # evalに関数名を渡して実行する例
    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = eval(function_name)
    f(a, b)


    # 組み込み関数等をすべて使えてしまうのでセキュリティ的に微妙
    import os
    function_name = 'os.system'
    f = eval(function_name)
    f('ls -la')
