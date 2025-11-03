class ContentCreator:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self):
        print("Creating content...")

class YouTuber(ContentCreator):
    def work(self):
        print("Recording and editing videos...")

class Blogger(ContentCreator):
    def work(self):
        print("Writing and publishing articles...")

creator1 = YouTuber("Ananya", "YouTuber")
creator2 = Blogger("Vikram", "Blogger")

creators = [creator1, creator2]

for creator in creators:
    print(f"\nCreator: {creator.name}")
    print(f"Role: {creator.role}")
    print("Task:", end=" ")
    creator.work()
