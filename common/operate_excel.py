"""
操作步骤
    将表格的数据读取成[{},{}...]
    字典的键:表格中的第一行
    字典的值:表格中的其他行
    excel数据    Python数据
    1            str
    2            整数
    3            日期
    4            布尔值
"""
import xlrd
from xlutils.copy import copy

# 创建工具类,操作Excel表格
class OperationExcel:
    def __init__(self,filename):
        """
        初始化类,每次传入文件名
        :param:filename: 文件路径+文件名
        """
        self.filename =filename
        self.table = xlrd.open_workbook(filename)

    def get_data_by_index(self,index=0):
        """
        通过索引读取数据
        :param:index 索引值
        :return:
        """
        sheet = self.table.sheet_by_index(index)
        return self._get_data_info(sheet)

    def get_data_by_name(self,name):
        """
        通过表名读取数据
        :param name:
        :return:
        """
        sheet = self.table.sheet_by_name(name)
        return self._get_data_info(sheet)

    def _get_data_info(self,sheet):
        """
        获取数据的详情
        :param sheet:
        :return:
        """
        keys = sheet.row_values(0)  # 将表格的第一行作为字典的键
        rows = sheet.nrows  # 获取表中的总行数
        cols = sheet.ncols  # 获取表中的总列数
        data_list = []  # 放置读取的数据
        for row in range(1, rows):  # 遍历行
            value_list = []  # 放置每行的数据
            for col in range(cols):  # 遍历列
                value = self._read_cell(sheet, row, col)
                value_list.append(value)
            tmp = zip(keys, value_list)  # 使用zip函数组合键和值
            data_list.append(dict(tmp))  # 将字典添加到列表中
        return data_list

    def _read_cell(self,sheet,row,col):
        """
        处理单元格数据类型
        :param sheet:
        :return:
        """
        # sheet = self.table.sheet_by_index(0)
        cell = sheet.cell_value(row,col)  # 单元格数据
        cell_type = sheet.cell_type(row,col)  # 获取单元格的数据类型
        if cell_type == 1:  # 当单元格数据类型为str
            cell = cell  # 不对数据做任何处理
        elif cell_type == 2 and cell % 1 == 0:  # 当单元格数据类型为整数时
            cell = int(cell) # 转为int类型
        elif cell_type == 4:  # 当单元格数据类型布尔值
            cell = True if cell == 1 else False  # 三目运算符
        return cell

    def write_data(self, data):
        """
        更新表格数据
        1.使用xlutils库   pip install xlutils
        from xlutils.copy import copy
        2.先复制旧的表格
        3.写入新数据
        4.复写老数据
        5.保存表格
        :param list: 写入的数据格式列表格式
        :return:
        """
        # 得到需要修改的表
        old_sheet = self.table.sheet_by_index(0)
        # 复制老表格
        new_table = copy(self.table)
        new_sheet = new_table.get_sheet(0)
        # 写入新数据  new_sheet.write(行,列,值)
        # 最好写在第一行
        # list = ["jerry","123456","123456@qq.com","110"]
        for i in range(len(data)):
            new_sheet.write(1, i, data[i])
        # 复写老数据
        for row in range(1, old_sheet.nrows):  # 遍历老数据行号
            for col in range(old_sheet.ncols):  # 遍历老数据列
                new_sheet.write(row + 1, col, old_sheet.cell_value(row, col))

        # 保存数据
        new_table.save(self.filename)

if __name__ == '__main__':
        oper = OperationExcel("../data/data.xls")
        data = ["jerry", "123457", "123456@qq.com", "112"]
        oper.write_data(data)