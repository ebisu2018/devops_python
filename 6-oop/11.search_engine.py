'''

一个搜索引擎由搜索器、索引器、检索器以及用户接口组成
搜索器：其实就是我们常说的爬虫、它能够从互联网中搜集大量的信息，并将之传递给索引器
索引器：理解搜索器搜索到的信息，并从中抽取出索引项，存储到内部的数据库中，等待检索
检索器：根据用户查询的内容，在已经建立好的索引库中快速检索出与之相关的信息，并做相关度评价，以此进行排序
用户接口：其作用就是提供给用户输入查询内容的窗口（例如百度、谷歌的搜索框），并将检索好的内容反馈给用户

'''


class SearchEngineBase:

    def add_corpus(self, file_path):
        with open(file_path, 'rb') as fobj:
            text = fobj.read().decode()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process not implemented')

    def search(self, query):
        raise Exception('search not implemented')


def main(search_engine: SearchEngineBase):
    for file_path in [f'content/{i}.txt' for i in range(1, 6)]:
        search_engine.add_corpus(file_path)

    query = input('Search:')
    results = search_engine.search(query)
    print('found {} result(s):'.format(len(results)))
    for result in results:
        print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


search_engine = SimpleEngine()
main(search_engine)
