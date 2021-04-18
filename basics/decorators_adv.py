# iters sets run <main> func quantity
def benchmark(iters):
    def actual_decorator(func):
        import time
    
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value
        return wrapper
    return actual_decorator


@benchmark(2)
def test_requests(text_print, fname):
    print(f"{text_print} from decorated function -> [{fname}]")
    import requests
    webpage = requests.get('https://google.com')
    return webpage.text

if __name__ == '__main__':
    test_requests("hello", fname= "test_requests")