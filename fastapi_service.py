from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

# 假设数据库中匹配的潜在搭子数据
potential_companion_db = [
    {"id": "1", "activity_type": "hiking", "age": "25", "gender": "male"},
    {"id": "2", "activity_type": "painting", "age": "30", "gender": "female"},
]

# 假设数据库中的用户信息
user_db = {
    "1": {"age": "25", "gender": "male", "city": "Shanghai", "introduction": "I love hiking",
          "contact_info": "1234567890"},
    "2": {"age": "30", "gender": "female", "city": "Beijing", "introduction": "I love painting",
          "contact_info": "0987654321"},
}


@app.get("/admin/searchCompanion")
async def search_companion(activity_type: str, age: str, gender: str, requirements: str):
    # 根据查询参数过滤潜在搭子数据
    data = [companion for companion in potential_companion_db if
            companion["activity_type"] == activity_type and
            companion["age"] == age and
            companion["gender"] == gender]
    response_data = {"code": 200, "data": json.dumps(data)}
    return response_data


@app.get("/admin/getPotentialCompanion")
async def get_potential_companion():
    # 返回所有潜在搭子数据
    data = potential_companion_db
    response_data = {"code": 200, "data": json.dumps(data)}
    return response_data


@app.get("/admin/updateUserInfo")
async def update_user_info(user_id: str, age: str, gender: str, city: str, introduction: str, contact_info: str):
    # 更新用户信息
    if user_id in user_db:
        user_db[user_id] = {
            "age": age,
            "gender": gender,
            "city": city,
            "introduction": introduction,
            "contact_info": contact_info
        }
        data = {"message": "User info updated successfully"}
        response_data = {"code": 200, "data": json.dumps(data)}
    else:
        data = {"message": "User not found"}
        response_data = {"code": 404, "data": json.dumps(data)}
    return response_data


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8888)
