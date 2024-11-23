import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sentence_transformers import SentenceTransformer
import torch.nn.functional as F

import json
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
from model import DualInputModel
model_save_path = 'model_linear/'
plt_save_path = 'plt_images/'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"使用的设备: {device}")

if os.path.exists(model_save_path):
    print("model_files exists")
else:
    os.makedirs(model_save_path)

if os.path.exists(plt_save_path):
    print("plt_images exists")
else:
    os.makedirs(plt_save_path)


model = SentenceTransformer("model_files")
with open('result.json', 'r') as f:
    data = json.load(f)

data = data
request1s = []
request2s = []
labels = []
for i in tqdm(range(len(data))):
    request1s.append(data[i]['request1'])
    request2s.append(data[i]['request2'])
    labels.append(data[i]['relevance']*2-1)


labels = torch.tensor(labels, dtype=torch.float32)
embedding1s = model.encode(request1s)
embedding2s = model.encode(request2s)
print(embedding1s.shape)
embedding1s = torch.tensor(embedding1s, dtype=torch.float32)
embedding2s = torch.tensor(embedding2s, dtype=torch.float32)
labels = labels.to(device)
embedding1s = embedding1s.to(device)
embedding2s = embedding2s.to(device)

# Create DataLoader
dataset = TensorDataset(embedding1s, embedding2s, labels)
loader = DataLoader(dataset, batch_size=512, shuffle=True)
testloader = DataLoader(dataset, batch_size=512, shuffle=True)
# Initialize model, loss, optimizer
model = DualInputModel(input_dim1=embedding1s.shape[1], input_dim2=embedding1s.shape[1], hidden_dim=800)
model.to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)


# Training loop
epochs = 50000
loss_history = []
for epoch in tqdm(range(epochs)):
    epoch_loss = 0.0
    for batch_x1, batch_x2, batch_y in loader:
        optimizer.zero_grad()
        outputs = model(batch_x1, batch_x2)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    avg_loss = epoch_loss / len(loader)
    loss_history.append(avg_loss)  # 记录平均损失

    tqdm.write(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}')
    # 每隔2000个epoch绘制一次损失图
    if (epoch + 1) % 100 == 0:
        plt.figure()
        plt.plot(range(1, epoch + 2), loss_history, label='Training Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title(f'Training Loss up to Epoch {epoch +1}')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{plt_save_path}loss_epoch_{epoch +1}.png')  # 保存图表
        plt.close()  # 关闭图表以节省内存
        
        print(f'已保存损失图表: {plt_save_path}loss_epoch_{epoch +1}.png')
    if (epoch + 1) % 100 == 0:
        torch.save(model.state_dict(), model_save_path+f'model_epoch_{epoch +1}.pth')
        print(f'已保存模型权重: {model_save_path}model_epoch_{epoch +1}.pth')