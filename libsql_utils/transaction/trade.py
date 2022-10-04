#!/usr/bin/python3
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, MetaData, Date, Float, select
from sqlalchemy.orm import Session
from ..model.trade import formAssetTemplate, formInvestValue, formStrategySet, formAssetTemplate, formOrderSet
from ..model.stock import formStock
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)

def update_invest_value(engine, tablename: str, df: list):
    """
    更新净值
    engine: orm engine
    tablename: operating table name
    df: data insert into table
    """
    with Session(engine) as session:
        obj_list = []
        formInvestValue.__table__.name = tablename
        for item in df:
            obj_list.append(formInvestValue(trade_date=item[0], value=item[1]))
        session.add_all(obj_list)
        session.commit()
    return 1

def create_strategy(engine):
    # 创建策略表
    with Session(engine) as session:
        query = select(formStrategySet.name)
        table_list = session.execute(query).all()
        for item in table_list:
            formInvestValue.__table__.name = item[0]
            if not formInvestValue.__table__.exists(engine):
                formInvestValue.__table__.create(engine)
        session.commit()
    return 1

def create_asset_set(engine):
    """
    创建资产组合
    """
    with Session(engine) as session:
        query = select(formStrategySet.name)
        table_list = session.execute(query).all()
        for item in table_list:
            formAssetTemplate.__table__.name = f"asset_{item[0]}"
            if not formAssetTemplate.__table__.exists(engine):
                formAssetTemplate.__table__.create(engine)
        session.commit()
    return 1

def get_current_day(engine, stock_id: str, day: str):
    with Session(engine) as session:
        formStock.__table__.name = stock_id
        query = select(formStock.trade_date, formStock.open_price, formStock.close_price, formStock.high_price, formStock.low_price).where(formStock.trade_date==day)
        data = session.execute(query).all()
        session.commit()
    return data

def get_n_day_before_date(engine, stock_id: str, e: str, n: int):
    with Session(engine) as session:
        formStock.__table__.name = stock_id
        end_date = datetime.strptime(e, '%Y-%m-%d')
        start_date = end_date - timedelta(days=n)
        s = start_date.strftime('%Y-%m-%d')
        query = select(formStock.trade_date, formStock.open_price, formStock.close_price, formStock.high_price, formStock.low_price).where(formStock.trade_date.between(s, e))
        data = session.execute(query).all()
        session.commit()
    return data

def get_from_date_to_date(engine, stock_id: str, s: str, e: str):
    with Session(engine) as session:
        formStock.__table__.name = stock_id
        query = select(formStock.trade_date, formStock.open_price, formStock.close_price, formStock.high_price, formStock.low_price).where(formStock.trade_date.between(s, e))
        data = session.execute(query).all()
        session.commit()
    return data



def post_order(engine, order):
    with Session(engine) as session:
        ods = []
        for item in order:
            ods.append(formOrderSet(
                trader_name=item["trader_name"],
                trade_time=item["trade_time"],
                trade_type=item["trade_type"],
                asset_id=item["asset_id"],
                volume=item["volume"],
                price=item["price"]
                )
                )
        session.add_all(ods)
        session.commit()
    return 1


if __name__ == '__main__':
    from ..engine import engine_init
    import sqlalchemy
    eng = engine_init('localhost', 'root', '6414939', 'trade')
    eng2 = engine_init('localhost', 'root', '6414939', 'stock')
    # df = [('2021-08-01', 8.7), ('2021-08-02', 9.1)]
    # create_strategy(eng)
    # create_asset_set(eng)
    d = get_current_day(eng2, 'SH600000', '2020-09-23')
    print(d)
    order_set = [
        {
        "trader_name": "strategy_cambrian",
        "trade_time": "2022-9-23 11:24:31",
        "trade_type": "s",
        "asset_id": "SZ300015",
        "volume": 300,
        "price": 25.83,
        "cost": 26.37,
        "commision": 2.53,
        "tax": 0.35
    }
    ]
    # post_order(eng, order_set)
    x = get_n_day_before_date(eng2, 'SH600000', '2000-01-01', 10)
    print(x)
    x = get_from_date_to_date(eng2, 'SH600000', '1999-01-01', '2000-12-1')
    print(x)