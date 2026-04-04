import torch
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(2, 3),
    nn.ReLU(),
    nn.Linear(3, 1),
)
a=torch.rand(1,2)
y = model(a)
print(y)
#2 feature di vao layer linear1, output ra 3 feature -> dc activate bang ham relu, f(x) = max(x,0)
#sau do 3 feature vao layer linear2 va output ra 1 feature cuoi cung.

