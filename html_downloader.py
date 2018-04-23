#coding=utf-8
import urllib3
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        http=urllib3.PoolManager()
        r=http.request('get', url)
        if r.status!=200:
            return None
        return r.data.decode('utf-8')
