class Article:
    def __init__(self,title,urlToImage,description,url,author):
        self.title=title
        self.urlToImage=urlToImage
        self.description=description
        self.author=author
        self.url=url

class Source:
    def __init__(self,name,description):
        self.name=name
        self.description=description
