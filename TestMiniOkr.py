import minium

# pip3 install minium
# pip install pytest
# minitest -c config.json -m TestMiniOkr -g
# python -m http.server 12345 -d outputs # 防跨域可以这个
class TestMiniOkr(minium.MiniTest):

    def test01(self):
        # v1 = self.page.get_element("view", inner_text="aaa") # 找内部文本为 aaa 的 view 元素
        # v1 = self.page.get_element("view", "aaa") # 找内部文本为 aaa 的 view 元素
        # v1.click()

        # self.mini.clear_auth();
        self.page.get_element("page > view > view.login > button").click()

        # 草泥马的测个大概就好了，一些场景就是实现不了我也没办法