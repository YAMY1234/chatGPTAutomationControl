from flask import Flask, request, jsonify
import pyautogui
import pyperclip
import time
from automation_script import automate_text_interaction

app = Flask(__name__)

@app.route('/call_chatgpt', methods=['POST'])
def call_chatgpt():
    """
    Flask 路由接口，用于调用 automate_text_interaction。
    """
    try:
        # 获取请求中的输入内容
        data = request.get_json()
        if not data or 'input_text' not in data:
            return jsonify({"error": "Missing 'input_text' parameter"}), 400

        input_text = data['input_text']

        # 调用自动化操作函数
        result = automate_text_interaction(input_text)
        return jsonify({"status": "success", "output": result}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 运行 Flask 应用
    app.run(host='0.0.0.0', port=80, debug=True)