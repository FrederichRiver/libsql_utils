#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class formStock(Base):
    __tablename__ = 'template_stock'
    trade_date = Column(Date, primary_key=True)
    stock_name = Column(String(20))
    close_price = Column(Float, default=0)
    high_price = Column(Float, default=0)
    low_price = Column(Float, default=0)
    open_price = Column(Float, default=0)
    prev_close_price = Column(Float, default=0)
    change_rate = Column(Float, default=0)
    amplitude = Column(Float, default=0)
    volume = Column(Integer, default=0)
    turnover = Column(Float, default=0)
    adjust_factor = Column(Float, default=1)

    def __str__(self):
        return "<Stock template>"

class formStockManager(Base):
    __tablename__ = 'stock_manager'
    stock_code = Column(String(10), primary_key=True)
    stock_name = Column(String(20))
    orgId = Column(String(25))
    short_code = Column(String(10))
    create_date = Column(Date)
    update_date = Column(Date)
    xrdr_date = Column(Date)
    balance_date = Column(Date)
    income_date = Column(Date)
    cashflow_date = Column(Date)
    flag = Column(String(10))

    def __str__(self):
        return "<Stock Manager>"
