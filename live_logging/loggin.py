
def live_log_test(firstNumber: float=4, secondNumber: float=5, delay: int=100):
    for i in range(delay):
        sleep(1)
        print(i)

    # Compute the add
    result = firstNumber + secondNumber

    return result
