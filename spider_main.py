#coding=utf-8
import url_manager
import html_downloader
import html_outputer
import html_parse
class SpiderMain(object):  
    def __init__(self):  
        self.urls =url_manager.UrlManager()
        self.downloader =html_downloader.HtmlDownloader()  
        self.parser =html_parse.HtmlParse()
        self.outputer =html_outputer.HtmlOutputer()
  
  
    def craw(self, root_url):  
        count = 1  
        self.urls.add_new_url(root_url)#根节点入队  
        while self.urls.has_new_url():#类似广度优先搜索  
            try:  
                new_url = self.urls.get_new_url()#从队列中得到一个新的url  
                print('craw %d : %s'%(count, new_url))#哪个url正在被爬取  
                html_cont = self.downloader.download(new_url)#把这个网页爬下来  
                new_urls, new_data = self.parser.parse(new_url, html_cont)#解析内部的url和数据  
                self.urls.add_new_urls(new_urls)#将又爬到的url添加到队列中  
                self.outputer.collect_data(new_data)#收集数据  
                self.outputer.output_html()#打印数据  
  
                if count == 10:  
                    break  
  
                count += 1  
  
            except Exception as e:  
                print(e)
                print('craw failed')  
  
if __name__ == "__main__":  
    root_url = "http://baike.baidu.com/view/21087.htm" #根节点  
    obj_spider = SpiderMain()  
    obj_spider.craw(root_url)  
