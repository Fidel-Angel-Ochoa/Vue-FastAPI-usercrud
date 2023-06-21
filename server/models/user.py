from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# meta is used to give to the table more features from sql table.
users = Table("users", meta,
              Column("id",Integer, primary_key=True),
              Column("name",String(50)),
              Column("email",String(50)),
              Column("password",String(255))
              )
meta.create_all(engine)