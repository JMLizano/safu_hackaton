from sqlalchemy import create_engine
from environs import Env

env = Env()
env.read_env()

engine = create_engine(env.str('DATABASE_URL'))
conn = engine.connect()

sql_create_address_table = """ CREATE TABLE IF NOT EXISTS address (
                                        id VARCHAR(50),
                                        compromised BOOLEAN NOT NULL,
                                        PRIMARY KEY (id)
                            ); """

sql_create_trans_table = """ CREATE TABLE IF NOT EXISTS transactions (
                                        sender_id varchar(80),
                                        receiver_id varchar(80),
                                        extra_data varchar(80),
                                        PRIMARY KEY(sender_id, receiver_id),
                                        FOREIGN KEY (sender_id) REFERENCES address (id),
                                        FOREIGN KEY (receiver_id) REFERENCES address (id)
                                    ); """                                    


# CLEAN EVERYTHIN
conn.execute('drop table if exists transactions')
conn.execute('drop table if exists address')

# CREATE TABLES
conn.execute(sql_create_address_table)
conn.execute(sql_create_trans_table)

# CREATE INDEX
conn.execute('CREATE INDEX address_ind ON address (id ASC)')

# ADDRESS
conn.execute('insert into address(id, compromised) values (\"address1\",  0)')
conn.execute('insert into address(id, compromised) values (\"address2\",  0)')
conn.execute('insert into address(id, compromised) values (\"address3\",  0)')
conn.execute('insert into address(id, compromised) values (\"address4\",  0)')
conn.execute('insert into address(id, compromised) values (\"address5\",  1)')
conn.execute('insert into address(id, compromised) values (\"address6\",  0)')
conn.execute('insert into address(id, compromised) values (\"address7\",  0)')
conn.execute('insert into address(id, compromised) values (\"address8\",  0)')
conn.execute('insert into address(id, compromised) values (\"address9\",  0)')
conn.execute('insert into address(id, compromised) values (\"address10\", 1)')

# TRANSACTIONS
conn.execute('insert into transactions values (\"address1\", \"address2\", \"testdata1\")')
conn.execute('insert into transactions values (\"address1\", \"address3\", \"testdata1\")')
conn.execute('insert into transactions values (\"address1\", \"address8\", \"testdata1\")')

conn.execute('insert into transactions values (\"address2\", \"address4\", \"testdata2\")')
conn.execute('insert into transactions values (\"address2\", \"address5\", \"testdata2\")')
conn.execute('insert into transactions values (\"address2\", \"address6\", \"testdata2\")')
conn.execute('insert into transactions values (\"address2\", \"address7\", \"testdata2\")')

conn.execute('insert into transactions values (\"address3\", \"address2\", \"testdata3\")')
conn.execute('insert into transactions values (\"address3\", \"address7\", \"testdata3\")')

conn.execute('insert into transactions values (\"address5\", \"address9\", \"testdata4\")')

conn.execute('insert into transactions values (\"address6\", \"address1\", \"testdata5\")')
conn.execute('insert into transactions values (\"address6\", \"address3\", \"testdata5\")')
conn.execute('insert into transactions values (\"address6\", \"address4\", \"testdata5\")')
conn.execute('insert into transactions values (\"address6\", \"address8\", \"testdata5\")')
conn.execute('insert into transactions values (\"address6\", \"address7\", \"testdata5\")')

conn.execute('insert into transactions values (\"address7\", \"address4\", \"testdata6\")')

conn.execute('insert into transactions values (\"address8\", \"address1\", \"testdata7\")')
conn.execute('insert into transactions values (\"address8\", \"address4\", \"testdata7\")')
conn.execute('insert into transactions values (\"address8\", \"address6\", \"testdata7\")')

conn.execute('insert into transactions values (\"address9\", \"address5\", \"testdata8\")')

conn.execute('insert into transactions values (\"address10\", \"address4\", \"testdata9\")')

conn.close()
