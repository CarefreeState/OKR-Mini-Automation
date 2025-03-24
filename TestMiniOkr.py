import datetime
import time
import os

import minium

numFlag = "03"

def getPath(str):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d/%H%M%S%f")[:-3]
    return f"{timestamp}-{str}.png"

# pip3 install minium
# pip3 install minium==1.4.0
# pip install pytest
# pip uninstall minium
# minitest -c config.json -m TestMiniOkr -g
# python -m http.server 12345 -d outputs # 防跨域可以这个
class TestMiniOkr(minium.MiniTest):

    def shot(self, str):
        path = f"D:/pythonwork/OKR-Mini-Automation/outputs/OKR-System/Mini/{numFlag}/{getPath(str)}"
        output_path = os.path.join(os.path.dirname(__file__), path)
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))
        if os.path.exists(output_path):
            os.remove(output_path)
        self.app.screen_shot(output_path)  # 截图并存到`output_path`文件夹中
        self.assertTrue(os.path.isfile(output_path))

    def waitGet(self, str, cotains):
        # 等待页面加载完毕
        page = self.app.get_current_page()
        page.wait_for(str, 5)
        return page.get_element(str, text_contains=cotains)

    def clickElement(self, str, cotains):
        self.waitGet(str, cotains).click()

    def switchTabToOkrPerson(self):
        time.sleep(1)
        # 跳转到个人 OKR 页（默认 pages 开头，无需重复）
        self.app.switch_tab("okrPerson")
        if self.app.get_current_page().wait_for("text.uni-icons.uniui-close", 1):
            self.clickElement("text.uni-icons.uniui-close", "")

    def creteOkr(self):
        self.switchTabToOkrPerson()
        # 点击创建 OKR 按钮
        self.clickElement("button.button", "创建OKR")
        self.clickElement("button.butt", "返回")
        self.clickElement("button.button", "创建OKR")
        self.clickElement("button.butt", "创建")
        self.shot("creteOkr")

    def firstQuadrantInit(self):
        self.switchTabToOkrPerson()
        self.clickElement(".editButton.blue", "查看/编辑")
        # 选中输入框输入
        self.waitGet("textarea.inputBox", "").input("Minium 自动化测试")
        # 选中日历输入
        self.clickElement(".uni-date__x-input", "选择日期时间")
        self.clickElement("view > view.uni-calendar__content.uni-calendar--fixed.uni-calendar--ani-show.uni-calendar__content-mobile > view.uni-calendar__header.uni-calendar__header-mobile > view:nth-child(3)", "")
        self.clickElement("view > view.uni-calendar-item__weeks-box-item", "16")
        self.clickElement("view.uni-datetime-picker--btn", "确认")
        self.clickElement("view.addButton.blue", "确认")
        self.shot("firstQuadrantInit")

    def firstQuadrant(self):
        # 添加关键结果
        self.switchTabToOkrPerson()
        self.clickElement(".editButton.blue", "查看/编辑")
        # 选中输入框输入
        self.clickElement("view.firstQButton.longButton.blue", "添加关键结果")
        self.waitGet("textarea.inputBox", "").input("Minium 自动化测试关键结果1")
        self.waitGet("slider", "").slide_to(100)
        self.clickElement("view.addButton.blue", "确认")

        self.clickElement(".firstQButton.longButton.blue", "添加关键结果")
        self.waitGet("textarea.inputBox", "").input("Minium 自动化测试关键结果2")
        self.waitGet("slider", "").slide_to(70)
        self.clickElement("view.addButton.blue", "确认")

        self.clickElement(".firstQButton.longButton.blue", "添加关键结果")
        self.waitGet("textarea.inputBox", "").input("Minium 自动化测试关键结果3")
        self.waitGet("slider", "").slide_to(40)
        self.clickElement("view.addButton.blue", "确认")

        self.clickElement(".firstQButton.longButton.blue", "添加关键结果")
        self.waitGet("textarea.inputBox", "").input("Minium 自动化测试关键结果4")
        self.waitGet("slider", "").slide_to(0)
        self.clickElement("view.addButton.blue", "确认")
        self.shot("firstQuadrant")

        self.clickElement(".firstQButton.shortButton.blue", "返回")
        self.shot("firstQuadrant")

    def otherQuadrant(self):
        self.switchTabToOkrPerson()
        self.clickElement(".editButton.yellow", "查看/编辑")
        self.shot("secondQuadrant")
        self.clickElement("view.backButton.yellow", "返回")
        self.clickElement(".editButton.green", "查看/编辑")
        self.shot("thirdQuadrant")
        self.clickElement("view.backButton.green", "返回")
        self.clickElement(".editButton.red", "查看/编辑")
        self.shot("fourthQuadrant")
        self.clickElement("view.backButton.red", "返回")

    def dayRecord(self):
        self.clickElement("text.uni-icons.uniui-plusempty", "")
        self.shot("dayRecord")
        self.clickElement("text.uni-icons.uniui-plusempty", "")
        self.shot("dayRecord")

    def endOkr(self):
        self.switchTabToOkrPerson()
        self.clickElement(".editButton.blue", "查看/编辑")
        self.clickElement("view.firstQButton.middleButton.blue", "结束")
        self.native.handle_modal("确认")
        self.waitGet("slider", "").slide_to(50)
        self.waitGet("textarea.summaryInput", "").input("Minium 自动化测试结果通过率 100%")
        self.clickElement("view.addButton.blue", "确认")
        self.shot("endOkr")

    def testCreateOkrCore(self):
        # 登录
        # self.mini.clear_auth()
        # self.page.get_element("page > view > view.login > button").click()
        # 创建 OKR
        self.shot("startup")
        self.creteOkr()
        # self.app.screen_shot()
        # 创建初始化第一象限
        self.firstQuadrantInit()
        # 创建初始化第一象限
        self.firstQuadrant()
        # 其他象限
        self.otherQuadrant()
        # 日记录按钮
        self.dayRecord()
        # 结束 OKR
        self.endOkr()
        # 结束
        self.shot("shutdown")
        self.mini.shutdown()

