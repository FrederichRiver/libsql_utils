from sqlalchemy import create_engine as _create_engine

def engine_init(host: str, acc: str, pw: str, db: str, eng_type='mysql', encoding='utf-8'):
    if eng_type == 'mysql':
        url = f"mysql+pymysql://{acc}:{pw}@{host}:3306/{db}"
    engine = _create_engine(url, encoding=encoding, echo=False)
    return engine