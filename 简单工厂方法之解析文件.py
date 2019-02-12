'''
    使用简单工厂方法实现解析 xml文件以及json文件
'''
import json
import xml.etree.ElementTree as etree
import os

from 简单工厂方法之解析HTTP文件 import DownloadHttpFile


class Parser():
    def __init__(self, path):
        self.f = open(path, 'r', encoding='utf8')

    def __del__(self):
        self.f.close()

    def parse_data(self):
        pass


class JsonParser(Parser):
    def parse_data(self):
        return json.load(self.f)


class XmlParser(Parser):
    def parse_data(self):
        return etree.parse(self.f)



def connect_factory(path):
    handlers = {
        '.json': JsonParser,
        '.xml': XmlParser,
    }
    return handlers.get(os.path.splitext(path)[-1], lambda x: None)(path)

def if_http_ftp(url):
    if url.startswith('http') or url.startswith('http'):
        return connect_factory(path=DownloadHttpFile(url=url).return_path())
    else:
        return connect_factory(path=url)


if __name__ == '__main__':
    conn_api = if_http_ftp('https://www.baidu.com/file.json')
    data = conn_api.parse_data()
    print(data)
