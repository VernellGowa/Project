import numpy as np
import torch as T

actual = np.array([0, 1, 0, 0]) 
N = len(actual)
logits = [3.2, 1.3, 0.2, 0.8]
logits = T.tensor(logits)

softmax = T.nn.Softmax(dim=0)
predicted = softmax(logits)
entropy = 0

for i in range(N):
    entropy += actual[i] * np.log(predicted[i])

entropy = -entropy
print(entropy)