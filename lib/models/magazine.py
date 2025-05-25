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