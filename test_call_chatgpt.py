import requests

# 目标服务的 IP 和端口
url = "http://54.153.23.83:80/call_chatgpt"

def test_call_chatgpt():
    """
    测试 /call_chatgpt 接口的功能。
    """
    # 构造请求的 JSON 数据
    input_text = "测试调用 ChatGPT 的自动化功能"
    payload = {"input_text": input_text}

    try:
        # 发送 POST 请求
        response = requests.post(url, json=payload)

        # 打印响应结果
        if response.status_code == 200:
            print("成功调用接口：")
            print(response.json())
        else:
            print("调用失败：")
            print(response.status_code, response.text)

    except Exception as e:
        print("请求出现错误：", e)

if __name__ == "__main__":
    test_call_chatgpt()