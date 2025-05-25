from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
  def __init__(self, id=None, name=None, category=None):
    self.id = id
    self.name = name
    self.category = category

  