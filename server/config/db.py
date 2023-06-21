from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://sql9627544:LdPH3kIkaV@sql9.freesqldatabase.com:3306/sql9627544")
meta = MetaData()
conn = engine.connect()

# original database conectiorn: "mysql+pymysql://root:password@localhost:3306/vue_fastapi"
