from lib.db.connection import get_connection

class Article:
  def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
    self.id = id
    self.title = title
    self.author_id = author_id
    self.magazine_id = magazine_id

  def save(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
        (self.title, self.author_id, self.magazine_id)
    )
    self.id = cursor.lastrowid
    conn.commit()
    conn.close()

  @classmethod
  def find_by_author(cls, author_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
    rows = cursor.fetchall()
    conn.close()
    return [cls(**row) for row in rows]

  @classmethod
  def find_by_magazine(cls, magazine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
    rows = cursor.fetchall()
    conn.close()
    return [cls(**row) for row in rows]