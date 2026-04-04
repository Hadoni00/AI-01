import torch
import torch.nn as nn
# Model A
moda = nn.Sequential(
    nn.Linear(2, 3),
    nn.Linear(3, 1)
)
# Model B
modb = nn.Sequential(
    nn.Linear(2, 3),
    nn.ReLU(),
    nn.Linear(3, 1)
)
inp = torch.rand(5,2)
outa = moda(inp)
outb = modb(inp)
print(f"output cua model A\n: {outa}")
print('\n')
print(f":output cua model B\n:{outb}")
#linear + linear = linear, nen can layer activate de model hoc duoc 
#quan he phi tuyen (relu: f(x) = max(x,0))

