def Y_response():
    data={
        "code": 200,
        "msg": "成功",
    }
    print(data.get("code"))

    return data

def N_response():
    data={
        "code": 500,
        "msg": "失败",
    }
    return data

if __name__ == "__main__":
    Y_response()
    N_response()