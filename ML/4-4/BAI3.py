import torch
import torch.nn as nn
model = nn.Linear(2,1)
a = torch.tensor([
	[1.0,2.0],
	[3.0,4.0],
	[5.0,6.0],
])
print(f"weight cua model:  {model.weight}")
print(f"bias cua model : {model.bias}")
y = model(a)
print(y)
