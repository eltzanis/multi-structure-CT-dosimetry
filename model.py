import torch.nn as nn

class RegressionModel(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size, num_layers, dropout):
        super(RegressionModel, self).__init__()

        layers = []
        layers.append(nn.Linear(input_size, hidden_sizes[0]))
        layers.append(nn.ReLU())

        for i in range(1, num_layers - 1):
            layers.append(nn.Linear(hidden_sizes[i - 1], hidden_sizes[i]))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout))
        
        layers.append(nn.Linear(hidden_sizes[num_layers - 2], output_size))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)