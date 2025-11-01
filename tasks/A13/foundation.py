class Books:
    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published

    def summary(self):
        print(f"\nTitle: {self.title}\nAuthor: {self.author}\nPublished: {self.published}")

# Creating an object
b1 = Books("Atomic Habits", "James Clear", 2018)
b1.summary()
