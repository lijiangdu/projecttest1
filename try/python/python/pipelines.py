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
#         # �ڱ��ش���teacher.json�ļ�
#         self.filename = open('teacher.json','w')
#
#     def process_item(self, item, spider):
#         # python����ת��Ϊjson�ַ���
#         text = json.dumps(dict(item),ensure_ascii = False) + '\n'
#         # д��
#         self.filename.write(str(text.encode('utf-8')))
#         return item
#
#     def close_spider(self,spider):
#
#         self.filename.close()