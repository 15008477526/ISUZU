# 导入

import jsonpath


class GetKeyword:

    @staticmethod
    def get_value_by_keyword(data, keywrod):
        '''
        获取关键字对应的值,如果有多个默认取第一个
        :param data:源数据----接口返回值
        :param keywrod:返回值内的字段
        :return:
        '''
        return jsonpath.jsonpath(data, f'$..{keywrod}')[0]

    @staticmethod
    def get_values_by_keyword(data, keywrod):   # 获取关键字对应的值,取所有的值
        return jsonpath.jsonpath(data, f'$..{keywrod}')


