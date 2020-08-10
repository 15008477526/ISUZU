import unittest
import HTMLTestRunnerPlugins
import time

# 确认测试用例文件路径
test_dir = './script'
# 将测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(test_dir)
# 指定测试报告位置
report_dir = './report'
# 命名测试报告存放位置
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_filename = report_dir + '/' + now + 'report.html'
with open(report_filename, 'wb') as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title='自动化测试报告',
        description='登录页面自动化',
        stream=fp
    )
    # 执行测试用例套件中的测试用例
    runner.run(discover)

vin = ["ISUTEST2584093167"]
print(vin[0])
