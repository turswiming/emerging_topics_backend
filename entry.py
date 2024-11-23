import uvicorn
from find_mate import check_mate_similarity
import os

def is_docker():
    """
    检测当前程序是否运行在 Docker 容器内。

    返回:
        bool: 如果在 Docker 容器内运行，返回 True，否则返回 False。
    """
    # 方法1：检查 /.dockerenv 文件是否存在
    if os.path.exists('/.dockerenv'):
        return True

    # 方法2：检查 /proc/1/cgroup 中的关键字
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            cgroup_content = f.read()
            container_keywords = ['docker', 'kubepods', 'containerd', 'lxc', 'podman']
            if any(keyword in cgroup_content for keyword in container_keywords):
                return True
    except FileNotFoundError:
        pass

    # 方法3（可选）：检查 /proc/self/mountinfo 中的挂载点
    try:
        with open('/proc/self/mountinfo', 'rt') as f:
            mountinfo_content = f.read()
            if 'docker' in mountinfo_content or 'overlay' in mountinfo_content:
                return True
    except FileNotFoundError:
        pass

    return False


if is_docker():
    print("Running inside Docker")
else:
    print("Not running inside Docker")

if True:


    
    similarities = check_mate_similarity(
        "i wanna learn english",
        ["i can teach english",
         " i love cat and i want to hold one","i wanna learn english"])
    print(similarities)

    #following code handing the api
    
    #this line  will execute the fastapi_service.py first
    from fastapi_service import app

    port = 8800
    if is_docker():
        # for docker to expose the port
        print("Running inside Docker")
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        print("Not running inside Docker")
        # for local machine to read the port
        uvicorn.run(app, host="127.0.0.1", port=port)
