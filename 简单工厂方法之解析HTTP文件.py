'''
    此类的关键作用是配合简单工厂类处理HTTP FTP 上的文件
    因为之前的解析文件类里面写的是路径 所以这块我们先行下载文件
    DownloadFile 是父类 里面3个方法
        init 主要是传入和初始化需要的变量
        download 下载文件
        return_path 返回文件路径

'''
import os
import requests


class DownloadFile(object):
    def __init__(self, url):
        self.url = url
        self.save_path = './files'
        self.path = ''

    def download(self):
        pass

    def return_path(self):
        self.download()
        return self.path


class DownloadHttpFile(DownloadFile):

    def download(self):

        try:
            f = open(self.save_path + os.sep + self.url.split('/')[-1], 'w', encoding='utf8')
            f.write(requests.get(url=self.url).content.decode())
            f.close()
            self.path = self.save_path + os.sep + self.url.split('/')[-1]
        except FileOpenFail as e:
            raise e


class FileOpenFail(Exception):
    pass



if __name__ == '__main__':
    download_api = DownloadHttpFile(url='https://baidu.com/file.json')
    print(download_api.return_path())
