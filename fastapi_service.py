from fastapi import FastAPI
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
    # 可以根据需要添加其他源
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 允许的源
    allow_credentials=True,           # 是否允许发送 cookies 等凭证信息
    allow_methods=["*"],              # 允许的HTTP方法
    allow_headers=["*"],              # 允许的HTTP头
)
# 假设数据库中匹配的潜在搭子数据
potential_companion_db = [
    {
        "user_number": "165899233", "user_id": "干冰不是冰", "age": "25", "gender": "男", "city": "上海", "introduction": "I love hiking",
        "contact_info": {
            "qq": "1234567890",
            "wechat": "",
            "email": ""
        }
    },
    {
        "user_number": "27384206", "user_id": "大王派我来巡山", "age": "30", "gender": "女", "city": "北京", "introduction": "I love painting",
        "contact_info": {
            "qq": "0987654321",
            "wechat": "",
            "email": ""
        }
    },
]

# 假设数据库中的用户信息
user_db = {
    "2850673": {"user_id": "蜡笔大新", "age": "25", "gender": "男", "city": "上海", "introduction": "I love hiking",
          "contact_info":{
              "qq": "1234567890",
              "wechat": "",
              "email": ""
          }
    },
    "4698730": {"user_id": "梵高的向日葵哈哈", "age": "30", "gender": "女", "city": "北京", "introduction": "I love painting",
           "contact_info":{
              "qq": "1689521433",
              "wechat": "fangao_",
              "email": "9965478233"
          }},
}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/admin/searchCompanion")
async def search_companion(requirements: str):
    print(requirements)
    # 根据查询参数过滤潜在搭子数据
    data = "收到需求，正在查询中 ... "
    response_data = {"code": 200, "data": json.dumps(data)}
    return response_data


@app.get("/admin/getPotentialCompanion")
async def get_potential_companion():
    # 返回所有潜在搭子数据
    data = potential_companion_db
    response_data = {"code": 200, "data": json.dumps(data)}
    return response_data


@app.get("/admin/getUserInfo/{user_number}")
async def get_user_info(user_number: str):
    # 获取用户信息
    print(f"Received user_id: {user_number}")  # 打印接收到的user_id
    if user_number in user_db:
        user_info = user_db[user_number]
        response_data = {
            "code": 200,
            "data": json.dumps(user_info)
        }
    else:
        data = {"message": "User not found"}
        response_data = {"code": 404, "data": json.dumps(data)}
    return response_data


@app.get("/admin/updateUserInfo")
async def update_user_info(user_id: str, user_number: str, age: str, gender: str, city: str, introduction: str, contact_info: str):
    # 更新用户信息
    if user_number in user_db:
        try:
            contact_info_dict = json.loads(contact_info)
        except json.JSONDecodeError:
            return {"code": 400, "data": json.dumps({"message": "Invalid contact_info format"})}

        user_db[user_number] = {
            "user_id": user_id,
            "age": age,
            "gender": gender,
            "city": city,
            "introduction": introduction,
            "contact_info": contact_info_dict
        }
        data = {"message": "User info updated successfully"}
        response_data = {"code": 200, "data": json.dumps(data)}
    else:
        data = {"message": "User not found"}
        response_data = {"code": 404, "data": json.dumps(data)}
    return response_data


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8800)
