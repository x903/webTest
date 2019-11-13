from selenium import webdriver
import unittest

class Driver:

    def __init__(self):
        
        self.browser = webdriver.Chrome()

    def open_browser(self):
        """
        Do something for browser
        :return: browser
        """
        # 窗口最大化
        self.browser.maximize_window()

        # 打开地址链接
        url = 'file:///C:/Python/webTest/file/new%201.html'
        self.browser.get(url)
        return self.browser

    def close_browser(self):
        """
        quit browser
        :return:
        """
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()