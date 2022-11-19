# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    fp = None
    #重写父类的一个方法，该方法发只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./tengx.txt','w',encoding='utf-8')

    #专门用来处理item类型对象
    #该方法可以接收爬虫文件提交过来的item对象
    #该方法每接收到一个item对象就会调用一次
    def process_item(self, item, spider):
        name = item['name']
        message = item['message']
        self.fp.write(name + ':' + message + '\n')
        return item#会传输给下一个即将执行的管道类
    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()

class mysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into film values("%s","%s")'%(item["name"],item["message"]))
            self.conn.commit()
        except:
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


#爬虫文件返回的是一个item只会提交给优先级较高的一个管道类