import torch

def compute(firstNumber: float=4, secondNumber: float=5):
    x = torch.rand(int(firstNumber), int(secondNumber))
    print(x)

    return x
