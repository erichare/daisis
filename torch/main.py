import torch

def compute(firstNumber: float=4, secondNumber: float=5):
    x = torch.rand(firstNumber, secondNumber)
    print(x)

    return x
