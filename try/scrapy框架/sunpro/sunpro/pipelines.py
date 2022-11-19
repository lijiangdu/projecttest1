# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunproPipeline:
    def process_item(self, item, spider):
        #判定item类型
        #将数据写入数据库时，根据两次的name进行比对
        if item.__class__.__name__ =='DetailItem':
            print(item['new_name'],item['introduce'])
        else:
            print(item['name'],item['author'])
        return item
