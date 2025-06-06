from lib.db.connection import get_connection

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
    from lib.models.article import Article
    return Article.find_by_author(self.id)

  def magazines(self):
    from lib.models.magazine import Magazine
    return Magazine.find_by_author(self.id)

  def add_article(self, magazine, title):
    from lib.models.article import Article
    article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
    article.save()
    return article

  def topic_areas(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT DISTINCT m.category FROM magazines m
      JOIN articles a ON a.magazine_id = m.id
      WHERE a.author_id = ?
    """, (self.id,))
    results = cursor.fetchall()
    conn.close()
    return [row['category'] for row in results]
