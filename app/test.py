import time

def my_timer(f):
    def time_wrapper(*args,**kwargs):
        strt = time.time()
        result = f(*args,**kwargs)
        dt = time.time()-strt
        print("Время выполнения: %f" %dt)
        return result
    return time_wrapper

@my_timer
def test_f(x,y):
    time.sleep(1)
    return(x+y)

print(test_f(10,10))



