from typing import List
import torch
import os
from download_model import downloader
from sentence_transformers import SentenceTransformer
from model import DualInputModel
class DeepLearningModel:
    _instance = None
    SBERTmodel = None
    linear_model = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DeepLearningModel, cls).__new__(cls, *args, **kwargs)
            downloader().download_models()
            cls.SBERTmodel = SentenceTransformer("model_files")
            #load model from weight
            cls.linear_model = DualInputModel(768,768,800)
            weights_path = "model_epoch.pth"  # 替换为您的权重文件路径
            if os.path.exists(weights_path):
                cls.load_model_weights(weights_path)
            else:
                print(f"权重文件未找到: {weights_path}")

        return cls._instance
    @classmethod
    def load_model_weights(cls, weights_path):
        """
        从权重文件加载模型权重。

        Args:
            weights_path (str): 权重文件的路径。
        """
        try:
            state_dict = torch.load(weights_path, map_location=torch.device('cpu'))  # 根据需要修改设备
            cls.linear_model.load_state_dict(state_dict)
            cls.linear_model.eval()  # 设置为评估模式
            print("模型权重加载成功。")
        except Exception as e:
            print(f"加载模型权重时出错: {e}")
    
def find_mate_from_groups(query_text:str, group_text:List[str]) -> int:
    # Find the mate of query_text in group_text
    # Return the index of query_text in group_text
    #todo: implement the function
    similarities = check_mate_similarity(query_text,group_text)
    #return highest index
    index = similarities.index(max(similarities))
    return index

@torch.no_grad
def check_mate_similarity(query_text:str, group_text:List[str]) -> List[float]:
    # Check the similarity of query_text with group_text
    # Return the similarity is above a certain threshold
    #todo: implement the function
    results = []
    for text in group_text:
        for i in range(len(text)):
            vec = DeepLearningModel().SBERTmodel.encode(text[i])
            query_vec = DeepLearningModel().SBERTmodel.encode(query_text)
            #convert vec and query_vec to torch tensor
            vec_tensor = torch.tensor(vec, dtype=torch.float32)
            query_vec_tensor = torch.tensor(query_vec, dtype=torch.float32)

            # 将一维张量转换为二维张量，形状从 [feature_dim] -> [1, feature_dim]
            vec_tensor = vec_tensor.unsqueeze(0)
            query_vec_tensor = query_vec_tensor.unsqueeze(0)
            similarity = DeepLearningModel().linear_model.forward(query_vec_tensor,vec_tensor)
            similarity = similarity.item()
        results.append(similarity)
    return results
