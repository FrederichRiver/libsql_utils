#!/usr/bin/python3
# libsql_utils/model/news.py

from sqlalchemy import Column, String, Integer, Text, Date
from sqlalchemy.orm import declarative_base

article_base = declarative_base()

class formArticle(article_base):
    __tablename__ = 'article'
    idx = Column(Integer)
    title = Column(String(50), primary_key=True)
    url = Column(String(50), unique=True)
    author = Column(String(20))
    release_date = Column(Date)
    source = Column(String(20))
    content = Column(Text)


class formNews(article_base):
    __tablename__ = 'news'
    idx = Column(Integer, unique=True)
    title = Column(String(50))
    url = Column(String(50), primary_key=True)
    author = Column(String(20))
    release_date = Column(Date)
    source = Column(String(20))
    filename = Column(String(35))