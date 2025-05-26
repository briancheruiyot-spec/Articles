from lib.models.author import Author
from lib.models.magazine import Magazine

# Sample interactive debugging
if __name__ == "__main__":
    author = Author(name="Brian Cheruiyot ")
    author.save()

    magazine = Magazine(name="Fluid Mechanincs", category="Mechanical Engineering")
    magazine.save()

    article = author.add_article(magazine, "The Rise of AI")

    print(f"{author.name} wrote: {[a.title for a in author.articles()]}")
    print(f"{author.name} has written in: {[m.name for m in author.magazines()]}")
