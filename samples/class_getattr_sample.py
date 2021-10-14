class Functions:
    @staticmethod
    def function_x(a, b):
        print('----function_x', a, b, '----')

    @staticmethod
    def function_y(a, b):
         print('====function_y', a, b, '====')

if __name__ == '__main__':
    # class内に定義して__dict__経由で呼び出す方法
    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = getattr(Functions, function_name)
    f(a, b)

    # __dict__とのちがいはpython3.10未満でも@staticmethodにしても動く
