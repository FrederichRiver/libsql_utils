#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class formInvestValue(Base):
    __tablename__ = 'invest_value_template'
    trade_date = Column(Date, primary_key=True)
    value = Column(Float)

class formStrategySet(Base):
    __tablename__ = 'strategy_set'
    idx = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    annulized_return = Column(Float)
    initial_value = Column(Float)
    max_draw = Column(Float)
    sharpe_ratio = Column(Float)
    sotino_ratio = Column(Float)
    beta = Column(Float)
    alpha = Column(Float)
    create_date = Column(DateTime)
    duration = Column(Integer)
    cycle_unit = Column(String(1))

class formAssetTemplate(Base):
    __tablename__ = 'asset_set_template'
    stock_id = Column(String(10), primary_key=True)
    volumn = Column(Integer)

class formOrderSet(Base):
    __tablename__ = 'order_set'
    idx = Column(Integer, primary_key=True)
    trader_name = Column(String(30))
    trade_time = Column(DateTime)
    trade_type = Column(String(2))
    asset_id = Column(String(10))
    volume = Column(Integer)
    price = Column(Float)
    cost = Column(Float)
    commision = Column(Float)
    tax = Column(Float)
