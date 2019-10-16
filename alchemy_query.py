import sqlalchemy as db
import sqlalchemy_utils as sqlutils

# ============================================================<Creds here>===============================================================================================================================================
username = "user"
password = "123"
ip = "192.168.1.1"
new_list = []

engine = db.create_engine(f'postgresql://{username}:{password}@{ip}/')
connection = engine.connect()                       # connect with creds
if connection:print('[INFO] Successfully connected')
metadata = db.MetaData()                            # get poles, cells, etc...
# ======================================================================================================================================================================================================================

# ============================================= ["SELECT datname FROM pg_database;"] ====================================================================================================================================
table_init = db.Table("pg_database", metadata, autoload=True, autoload_with=engine)
queries = db.select([db.text("datname"), table_init])   # select [what] from [where] like in RAW
print ("\n1)_____Get all databases from system table of Postrgres_____")
qw = connection.execute(queries)
if qw:
    print('[SYS] Query evaluated')

q_dcit = qw.fetchall()      # receive data from query
print("{}{}".format("Default stdout from db >> ", q_dcit))

if (len(q_dcit) < 100):
    for q in range (len (q_dcit)):
        q_dcit[q] = list(q_dcit[q])

    # [['postgres', 'postgres', 10, 6, 'ru_RU.UTF-8', 'ru_RU.UTF-8', False, True, -1, 12406, '543', '1', 1663, None], ['template1', 'template1', 10, 6, 'ru_RU.UTF-8', 'ru_RU.UTF-8', True, True, -1, 12406, '543', '1', 1663, ...]
    for k in range(len(q_dcit)):
        new_list.append(q_dcit[k][0])   # gets only name of db without extra params

    print("{}{}".format("Reformat step 1 (tuple/list (IDGAF) to list[list]) >> ", q_dcit))
    print("{}{}\n".format("Reformat step 2 (list[list] to normalized list >> ", new_list))
else:
    print("Too much elements")
# ======================================================================================================================================================================================================================

# ========================================== CREATE DATABASE testdb OWNER postgres TABLESPACE DEFAULT; =================================================================================================================
print("2) Creating database with SQLalchemy")
url = "postgresql://user:123@192.168.1.1/testerdb"
engine2 = db.create_engine(url)
try:
    connection2 = engine2.connect()                       # connect with creds
    print("[INFO] Database already exists >>> " + str(engine.url))
except:
    sqlutils.create_database(url)
    print("[INFO] DBase created succesfully >>> " + str(engine.url))
    connection2 = engine2.connect()  # connect with creds

# ALTER DATABASE name OWNER TO new_owner;
print("[INFO] Changing owner of freshy DB (RAW only)>>> \n...")
if connection.execute ("ALTER DATABASE testerdb OWNER TO postgres;"):
    print('[SYS] Query evaluated')
    print("[INFO] Owner changed succesfully")
# ====================================================================================================================================================================================================================

# ===============================================================================<Get value after AGRA045 from SQL>===================================================================================================
username = ""
password = ""
ip = ""
new_list = []

engine = db.create_engine(f'postgresql://{username}:{password}@{ip}/ma3')
connection = engine.connect()                       # connect with creds
if connection:print('[INFO] Successfully connected\n')
table_init = db.Table('nnr000', metadata, autoload=True, autoload_with=engine)

# qw = connection.execute("select * from nnr000 where nnr_codigo = '22' order by nnr_filial, nnr_codigo;")
query = db.select([db.text("*"), table_init]).where(table_init.columns.nnr_codigo == '22').order_by(table_init.columns.nnr_filial)
qw = connection.execute(query)

# make array from trashy execute result:
if qw:
    qw = qw.fetchall()
    print(qw)

# if qw:
#     print("Value founded")
#     qw = qw.fetchall()
#     print(qw)
# else:
#     print("Value not found")
# ====================================================================================================================================================================================================================

#PSQL mini HELP
# su -l user (123)
# ALTER USER user WITH ENCRYPTED PASSWORD '123';
# SELECT datname FROM pg_database;  //all databases

# Handler of cmdline args
# if len(sys.argv) >= 2:
#     username = sys.argv[1]
#     password = sys.argv[2]
#     ip = sys.argv[3]