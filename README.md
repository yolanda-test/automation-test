# 百度聊天功能自动化测试

这是一个使用Selenium和pytest框架编写的百度聊天功能自动化测试项目。

## 项目结构

```
automation-test/
├─ src/                 # 源代码目录
│  └─ baidu.py         # 百度相关功能实现
├─ test/               # 测试用例目录
│  └─ test_baidu_chat.py  # 百度聊天功能测试用例
├─ chromedriver        # Chrome浏览器驱动
├─ pytest.ini          # pytest配置文件
└─ README.md           # 项目说明文档
```

## 功能模块

### src/baidu.py

包含百度相关的功能实现：

- `create_driver(visible: bool = True)`: 创建并配置Chrome浏览器实例
- `open_baidu(driver: webdriver.Chrome, wait_seconds: int = 5)`: 打开百度网站
- `find_chat_textarea(driver: webdriver.Chrome, wait_seconds: int = 10)`: 查找聊天输入框
- `find_search_button(driver: webdriver.Chrome, wait_seconds: int = 10)`: 查找搜索按钮
- `search_poem(driver: webdriver.Chrome, poem_name: str)`: 搜索指定诗歌
- `verify_poem_content(driver: webdriver.Chrome, poem_lines: list[str])`: 验证诗歌内容是否完整显示

### test/test_baidu_chat.py

包含百度聊天功能的测试用例：

- `test_baidu_chat_functionality`: 测试百度聊天功能，搜索并验证诗歌《沁园春·雪》的完整显示

## 配置文件

### pytest.ini

pytest的配置文件，包含：

- 默认测试选项
- 自定义标记（baidu, chat, smoke）
- 测试发现模式

## 安装依赖

```bash
python3 -m pip install pytest selenium --trusted-host mirrors.aliyun.com
```

## 运行测试

```bash
# 运行所有测试
python3 -m pytest

# 运行指定测试文件
python3 -m pytest test/test_baidu_chat.py

# 运行测试并显示详细信息
python3 -m pytest -v

# 运行特定标记的测试
python3 -m pytest -m "baidu and chat"
```

## 测试结果

测试通过后，将显示以下结果：

```
================================== test session starts ===================================
platform darwin -- Python 3.13.3, pytest-9.0.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
cachedir: .pytest_cache
rootdir: /Users/chenguang/Documents/GitHub/automation-test
configfile: pytest.ini
testpaths: test
collected 1 item                                                                          

test/test_baidu_chat.py::test_baidu_chat_functionality PASSED                      [100%]

=================================== 1 passed in 14.63s ===================================
```

## 注意事项

1. 确保已安装Chrome浏览器
2. 确保chromedriver版本与Chrome浏览器版本匹配
3. 测试默认以无头模式运行，如需查看浏览器界面，可将`create_driver`函数中的`visible`参数设置为`True`