# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsPipeline:
    n = 1
    def process_item(self, item, spider):
        # item['title'].replace(' ','')
        # fileName = './new/'+item['title']+'.txt'
        fileName = './new/' + str(self.n) + '.txt'
        self.n+=1
        with open(fileName,'w',encoding='utf-8') as fp:
            fp.write(item['title']+item['content'])
        # print(item)
        return item
