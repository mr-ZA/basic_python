import sqlalchemy as db

username = ""   # shouldn't work wout params
password = ""
ip = ""
new_list = []

engine = db.create_engine(f'postgresql://{username}:{password}@{ip}/')
connection = engine.connect()                       # conneect with creds
if connection:print('[INFO] Successfully connected')
metadata = db.MetaData()                            # get poles, cells, etc...

#queries = ["SELECT datname FROM pg_database;"]      # query RAW
table_init = db.Table("pg_database", metadata, autoload=True, autoload_with=engine)
queries = db.select([db.text("datname"), table_init])   # select [what] from [where] like in RAW
qw = connection.execute(queries)

q_dcit = qw.fetchall()      # receive data from query
print("{}{}".format("Default stdout from db >> ", q_dcit))

if (len(q_dcit) < 100):
    for q in range (len (q_dcit)):
        q_dcit[q] = list(q_dcit[q])

    # [['postgres', 'postgres', 10, 6, 'ru_RU.UTF-8', 'ru_RU.UTF-8', False, True, -1, 12406, '543', '1', 1663, None], ['template1', 'template1', 10, 6, 'ru_RU.UTF-8', 'ru_RU.UTF-8', True, True, -1, 12406, '543', '1', 1663, ...]
    for k in range(len(q_dcit)):
        new_list.append(q_dcit[k][0])   # gets only name of db without extra params

    print("{}{}".format("Reformat step 1 (tuple/list to list[list]) >> ", q_dcit))
    print("{}{}".format("Reformat step 2 (list[list] to normalized list >> ", new_list))
else:
    print("Too much elements")

print('[INFO] Query evaluated')