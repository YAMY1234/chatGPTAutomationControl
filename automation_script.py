import pyautogui
import pyperclip
import time

# 配置像素点位置
# CONFIG = {
#     "input_text_position": (718, 613),   # 输入文字位置
#     "send_button_position": (1598, 1035), # 发送按钮位置
#     "scroll_trigger_position": (1000, 600), # 滚动触发位置
#     "copy_button_position": (808, 796),  # 复制按钮位置
#     "scroll_amount": -100,               # 向下滚动单位
#     "scroll_duration": 30,               # 滚动持续时间（秒）
#     "scroll_interval": 1                 # 滚动间隔（秒）
# }

CONFIG = {
    "input_text_position": (int(297 * 2 / 3), int(730 * 2 / 3)),  # 输入文字位置
    "send_button_position": (int(1006 * 2 / 3), int(730 * 2 / 3)),  # 发送按钮位置
    "scroll_trigger_position": (int(500 * 2 / 3), int(500 * 2 / 3)),  # 滚动触发位置
    "copy_button_position": (int(199 * 2 / 3), int(556 * 2 / 3)),  # 复制按钮位置
    "scroll_amount": -100,               # 向下滚动单位
    "scroll_duration": 20,               # 滚动持续时间（秒）
    "scroll_interval": 1                 # 滚动间隔（秒）
}

def automate_text_interaction(input_content: str) -> str:
    """
    自动化操作，将输入内容传入，执行系列操作后返回剪贴板中的输出内容。

    :param input_content: 输入内容的字符串
    :return: 剪贴板中获取的输出内容
    """
    # 0. 将输入内容复制到剪贴板
    pyperclip.copy(input_content)

    # 1. 点击输入文字位置
    pyautogui.click(*CONFIG["input_text_position"])
    time.sleep(0.5)  # 防止操作过快

    # 2. 粘贴内容 (Ctrl+V 或 Command+V)
    pyautogui.hotkey('ctrl', 'v')  # Windows/Linux
    # pyautogui.hotkey('command', 'v')  # MacOS
    time.sleep(0.5)

    # 3. 点击发送按钮
    pyautogui.click(*CONFIG["send_button_position"])
    time.sleep(0.5)

    # 点击滚动触发位置
    pyautogui.click(*CONFIG["scroll_trigger_position"])
    time.sleep(0.5)

    # 4. 向下滚动，持续指定时间
    start_time = time.time()  # 记录开始时间
    while time.time() - start_time < CONFIG["scroll_duration"]:
        pyautogui.scroll(CONFIG["scroll_amount"])  # 向下滚动单位
        time.sleep(CONFIG["scroll_interval"])  # 滚动间隔

    # 5. 点击复制按钮
    pyautogui.click(*CONFIG["copy_button_position"])
    time.sleep(0.5)

    # 6. 获取剪贴板中的内容并返回
    output_content = pyperclip.paste()
    return output_content


# 示例调用
if __name__ == "__main__":
    input_text = "讲解一下pyautogui.scroll(-100) 这个-100的含义!"
    time.sleep(5)  # 给用户时间切换到目标窗口
    result = automate_text_interaction(input_text)
    print("Output content from clipboard:", result)
