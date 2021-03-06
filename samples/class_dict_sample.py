class Functions:
    def function_x(a, b):
        print('----function_x', a, b, '----')

    def function_y(a, b):
         print('====function_y', a, b, '====')

if __name__ == '__main__':
    # class内に定義して__dict__経由で呼び出す方法
    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = Functions.__dict__[function_name]
    f(a, b)

    # 問題になりそうなものは出てこなさそうだが関数が増えるとclassの巨大化が問題 
    # インスタンスメソッドとして定義しているのは気持ち悪い
    # python 3.10からは@staticmethodにしても動く
    print(Functions.__dict__)
