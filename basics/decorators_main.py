def hello_world():
    print('[1] Hello world!')

def higher_order(func):
    print('[2] Получена функция {} в качестве аргумента'.format(func))
    func()
    return func

def decorator_function(func):
    def wrapper():
        print('[3] Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world_wrapped():
    print('Hello world from decorated function!')

def main():
    rec_f = hello_world
    rec_f()

    print("\n")
    higher_order(hello_world)
    
    print("\n")
    hello_world_wrapped()

main()