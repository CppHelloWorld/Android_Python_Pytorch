import torch
import torch.nn as nn
from typing import OrderedDict
torch.set_default_tensor_type(torch.DoubleTensor)

#这个是模型文件。

class DNN(nn.Module):
    def __init__(self, input_channel = 2500, num_class = 5):
        super().__init__()
        self.input_channel = input_channel
        self.num_class = num_class
        self.layers = nn.Sequential(OrderedDict([('Linear1', nn.Linear(input_channel, 512)), ('Relu1', nn.ReLU(inplace=True)), ('Linear2', nn.Linear(512, 512)), ('Relu2', nn.ReLU(inplace=True)), ('Linear3', nn.Linear(512, 512)), ('Relu3', nn.ReLU(inplace=True)), ('Linear4', nn.Linear(512, self.num_class))]))


    def forward(self, x):
        x = x.to(torch.double)
        return self.layers(x)

