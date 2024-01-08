from memory_profiler import profile, memory_usage


@profile
def myFunction(listSize):
    list1 = ['word1'] * listSize
    list2 = ['word2'] * listSize
    del list2
    return list1

myFunction(1000000)

