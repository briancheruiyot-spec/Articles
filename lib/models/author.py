from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.magazine import Magazine

class Author:
  def __init__(self, id=None, name=None):
    self.id = id
    self.name = name