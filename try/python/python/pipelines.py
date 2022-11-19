# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PythonPipeline:
    def process_item(self, item, spider):
        return item

# import json
# class ItcastspiderPipeline(object):
#     def __init__(self):
#         # 在本地创建teacher.json文件
#         self.filename = open('teacher.json','w')
#
#     def process_item(self, item, spider):
#         # python类型转化为json字符串
#         text = json.dumps(dict(item),ensure_ascii = False) + '\n'
#         # 写入
#         self.filename.write(str(text.encode('utf-8')))
#         return item
#
#     def close_spider(self,spider):
#
#         self.filename.close()