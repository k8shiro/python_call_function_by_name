class Functions:
    def get_functions(self):
        return {
            'function_x': self.function_x,
            'function_y': self.function_y
        }

    @staticmethod
    def function_x(a, b):
        print('----function_x', a, b, '----')
    @staticmethod
    def function_y(a, b):
         print('====function_y', a, b, '====')

if __name__ == '__main__':
    # class内に関数一覧を返す関数(get_functions)を定義する方法
    function_name = 'function_x'
    a = 'A'
    b = 'B'
    f = Functions().get_functions()[function_name]
    f(a, b)

    # 定義するものが増えるが構造としてはきれい
    # 予期せぬ関数が実行されることがないので安全


# 複数のclassに分割もできる

class FunctionsA:
    def get_functions(self):
        return {
            'FunctionsA.function_x': self.function_x,
            'FunctionsA.function_y': self.function_y
        }

    @staticmethod
    def function_x(a, b):
        print('----function_x', a, b, '----')
    @staticmethod
    def function_y(a, b):
         print('====function_y', a, b, '====')

class FunctionsB:
    def get_functions(self):
        return {
            'FunctionsB.function_x': self.function_x,
            'FunctionsB.function_y': self.function_y
        }

    @staticmethod
    def function_x(a, b):
        print('++++function_x', a, b, '++++')
    @staticmethod
    def function_y(a, b):
         print('<<<<function_y', a, b, '<<<<')

if __name__ == '__main__':
    function_name = 'FunctionsA.function_x'
    a = 'A'
    b = 'B'
    functions = dict()
    functions.update(FunctionsA().get_functions()) # dictの連結では本当は重複時にエラーになる方がよい
    functions.update(FunctionsB().get_functions())
    functions[function_name](a, b)




