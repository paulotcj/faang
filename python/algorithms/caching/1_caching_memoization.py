import time

#-------------------------------------------------------------------------
def closure_test_1():
    cache = {}

    def inner_func(param):
        if param in cache:
            return cache[param]
        else:
            print(f"value: {param} is not cached. Processing now... time for completion 4 sec")
            cache[param] = param * param
            time.sleep(4)
            return cache[param]
    
    return inner_func
#-------------------------------------------------------------------------

memoized1 = closure_test_1()
value = 2
print(f"Checking caching for: {value}: {memoized1(value)}")
print(f"Checking caching for: {value}: {memoized1(value)}")
print(f"Checking caching for: {value}: {memoized1(value)}")
value = 3
print(f"Checking caching for: {value}: {memoized1(value)}")
print(f"Checking caching for: {value}: {memoized1(value)}")
