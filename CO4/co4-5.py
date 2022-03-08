class Publisher:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Publisher = ", self.name)
class book(Publisher):
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print("Title = ", self.title)
        print("Author = ", self.author)
class Python(book):
    def __init__(self,publisher,title,author,price,noOfPages):
        self.price = price
        self.noOfPages = noOfPages
        book.__init__(self,title,author)
        Publisher.__init__(self,publisher)
    def display(self):
        super().display()
        print("Price = ",self.price)
        print("No Of Pages = ",self.noOfPages)
k = Python("Marvel Comics","SpiderMan","StanLee",500,800)
k.display()