import torch
import torch.nn as nn
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the model
class DualInputModel(nn.Module):
    def __init__(self, input_dim1, input_dim2, hidden_dim):
        super(DualInputModel, self).__init__()
        self.linear1 = nn.Linear(input_dim1, hidden_dim)
        self.linear2 = nn.Linear(input_dim2, hidden_dim)
    
    def forward(self, x1, x2):
        out1 = self.linear1(x1)
        out2 = self.linear2(x2)
        similarity = F.cosine_similarity(out1.to(device), out2.to(device))
        return similarity