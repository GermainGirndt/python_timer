import time
import functools


def python_timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_python_timer(calc_range, repetitions, *functions):

        # defined variable for storing function's acumulated run time
        acumulated_time = {}
        for function in functions:
            acumulated_time[function.__name__] = 0

        for n in range(repetitions):
            for function in functions:
                start_time = time.perf_counter()    # 1
                function(calc_range)
                end_time = time.perf_counter()      # 2
                runtime = end_time - start_time
                acumulated_time[function.__name__] += runtime
                print(f"Executed function {function.__name__} in {runtime:.9f} secs")

        average_time = {}
        print(f"\n\n\nEach function was executed {repetitions} times within a range of {calc_range} numbers\n\n")
        for function in functions:
            average_time[function.__name__] = acumulated_time[function.__name__] / repetitions
            print(f"{function.__name__.capitalize()}'s average runtime was {average_time[function.__name__]:.8f} secs")
        print()

        return functions

    return wrapper_python_timer

# applies python_timer decorator to the function 'time_functions'


@python_timer
def time_functions(*args):
    return args


#                        #
##                      ##
###                    ###
#### Modify from here ####
###                    ###
##                      ##
#                        #


# without list comprehension
def function1(calc_range):
    l = []
    for x in range(calc_range):
        l.append(x ** x)
    print(l)
    return l


# with list comprehension
def function2(calc_range):
    l = [x ** x for x in range(calc_range)]
    print(l)
    return l


# adjust complexity
calc_range = 15
# adjust number of repetitions
repetitions = 10000


# add your functions here
time_functions(calc_range, repetitions, function1, function2)
