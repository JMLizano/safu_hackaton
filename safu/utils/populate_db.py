import sqlite3

conn = sqlite3.connect('safu.db')

sql_create_address_table = """ CREATE TABLE IF NOT EXISTS address (
                                        id varchar PRIMARY KEY,
                                        compromised boolean NOT NULL
                            ); """

sql_create_trans_table = """ CREATE TABLE IF NOT EXISTS transactions (
                                        sender_id varchar(80),
                                        receiver_id varchar(80),
                                        PRIMARY KEY(sender_id, receiver_id),
                                        FOREIGN KEY (sender_id) REFERENCES address (id),
                                        FOREIGN KEY (receiver_id) REFERENCES address (id)
                                    ); """                                    

conn.execute(sql_create_address_table)
conn.execute(sql_create_trans_table)

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
conn.execute('insert into transactions values (\"address1\", \"address2\")')
conn.execute('insert into transactions values (\"address1\", \"address3\")')
conn.execute('insert into transactions values (\"address1\", \"address8\")')

conn.execute('insert into transactions values (\"address2\", \"address4\")')
conn.execute('insert into transactions values (\"address2\", \"address5\")')
conn.execute('insert into transactions values (\"address2\", \"address6\")')
conn.execute('insert into transactions values (\"address2\", \"address7\")')

conn.execute('insert into transactions values (\"address3\", \"address2\")')
conn.execute('insert into transactions values (\"address3\", \"address7\")')

conn.execute('insert into transactions values (\"address5\", \"address9\")')

conn.execute('insert into transactions values (\"address6\", \"address1\")')
conn.execute('insert into transactions values (\"address6\", \"address3\")')
conn.execute('insert into transactions values (\"address6\", \"address4\")')
conn.execute('insert into transactions values (\"address6\", \"address8\")')
conn.execute('insert into transactions values (\"address6\", \"address7\")')

conn.execute('insert into transactions values (\"address7\", \"address4\")')

conn.execute('insert into transactions values (\"address8\", \"address1\")')
conn.execute('insert into transactions values (\"address8\", \"address4\")')
conn.execute('insert into transactions values (\"address8\", \"address6\")')

conn.execute('insert into transactions values (\"address9\", \"address5\")')

conn.execute('insert into transactions values (\"address10\", \"address4\")')

conn.commit()
conn.close()
