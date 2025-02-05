import torch
import numpy as np
import pandas as pd

print("check versions")
print("torch==" + torch.__version__)
print("numpy==" + np.__version__)
print("pandas==" + pd.__version__)
print("check cuda")
print("cuda is available:", torch.cuda.is_available())