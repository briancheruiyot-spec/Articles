from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
  def __init__(self, id=None, name=None, category=None):
    self.id = id
    self.name = name
    self.category = category

  def save(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO magazines (name, category) VALUES (?, ?)",
      (self.name, self.category)
    )
    self.id = cursor.lastrowid
    conn.commit()
    conn.close() 

  @classmethod
  def find_by_author(cls, author_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT DISTINCT m.* FROM magazines m
      JOIN articles a ON m.id = a.magazine_id
      WHERE a.author_id = ?
    """, (author_id,))
    rows = cursor.fetchall()
    conn.close()
    return [cls(**row) for row in rows]

  def articles(self):
    return Article.find_by_magazine(self.id)