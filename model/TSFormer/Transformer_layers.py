import math
import torch.nn as nn
from torch.nn import TransformerEncoder, TransformerEncoderLayer
import math

class TransformerLayers(nn.Module):
    def __init__(self, hidden_dim, nlayers, num_heads=4, dropout=0.1):
        super().__init__()
        self.d_model = hidden_dim
        encoder_layers = TransformerEncoderLayer(hidden_dim, num_heads, hidden_dim*4, dropout)
        self.transformer_encoder = TransformerEncoder(encoder_layers, nlayers)

    def forward(self, src):
        B, N, L, D = src.shape
        src = src * math.sqrt(self.d_model)
        src = src.view(B*N, L, D)
        src = src.transpose(0, 1)
        output = self.transformer_encoder(src, mask=None)
        output = output.transpose(0, 1).view(B, N, L, D)
        
        # return [B, N, L, D]
        
        return output
