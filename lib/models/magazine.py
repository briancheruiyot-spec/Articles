from lib.db.connection import get_connection

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
    from lib.models.article import Article
    return Article.find_by_magazine(self.id)

  def contributors(self):
    from lib.models.author import Author
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT DISTINCT au.* FROM authors au
      JOIN articles a ON au.id = a.author_id
      WHERE a.magazine_id = ?
    """, (self.id,))
    results = cursor.fetchall()
    conn.close()
    return [Author(**row) for row in results]

  def article_titles(self):
    return [article.title for article in self.articles()]

  def contributing_authors(self):
    from lib.models.author import Author
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT a.author_id, COUNT(*) as count, au.name FROM articles a
      JOIN authors au ON au.id = a.author_id
      WHERE a.magazine_id = ?
      GROUP BY a.author_id
      HAVING count > 2
    """, (self.id,))
    results = cursor.fetchall()
    conn.close()
    return [Author(id=row['author_id'], name=row['name']) for row in results]
