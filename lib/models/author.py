from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.magazine import Magazine

class Author:
  def __init__(self, id=None, name=None):
    self.id = id
    self.name = name

  def save(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
    self.id = cursor.lastrowid
    conn.commit()
    conn.close()

  @classmethod
  def find_by_id(cls, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    return cls(**row) if row else None
  
  def articles(self):
    return Article.find_by_author(self.id)

  def magazines(self):
    return Magazine.find_by_author(self.id)

  def add_article(self, magazine, title):
    article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
    article.save()
    return article