"""
与google交互
"""

# google两套 API:
#     老旧的API 和 API,这些需要开发者密钥。要求独一无二的开发者密钥让匿名变得不可能,一些我们以努力获得成功的脚本将不能用。
# 幸运的是老旧的版本任然允许一天之中进行一系列的查询,大约每天 30 次搜索结果。用于收集信息的话30 次结果足够了解一个组织网站的信息了。

class Google_Result:
    def __init__(self,title,text,url):
        self.title = title
        self.text = text
        self.url = url

        def __repr__(self):
            return self.title

def google(search_term):
    ab = anonBrowser()
    search_term = urllib.quote_plus(search_term)
    response = ab.open('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + search_term)
    objects = json.load(response)
    results = []
    for result in objects['responseData']['results']:
        url = result['url']
        title = result['titleNoFormatting']
        text = result['content']
        new_gr = Google_Result(title, text, url)
        results.append(new_gr)
    return results