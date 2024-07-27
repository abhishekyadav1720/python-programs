class library:
    def __init__(self):
        self.nobooks=0
        self.books = []
    
    def addbooks(self, books):
        self.books.append(books)
        self.nobooks = len(self.books)
    
    def showinfo(self):
        print(f"there are {self.nobooks} books which are : ")
        for book in self.books:
            print(book)

obj = library()
obj.addbooks("python")
obj.addbooks("dsa")
obj.addbooks("javascript")

obj.showinfo()


