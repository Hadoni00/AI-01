import torch
import torch.nn as nn

model = nn.Linear(3, 1)

# 1. input đúng (3 feature)
x = torch.tensor([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

print(model(x))


# 2. input sai (chỉ có 2 feature)
x_wrong = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0]
])

print("linear(A,B) thi luon can A feature")