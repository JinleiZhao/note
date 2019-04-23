from contextlib import  contextmanager

class Database:
    def __init__(self):
        self.connected = False
    
    def connect(self):
            self.connected = True
    
    def close(self):
        self.connected = False
    
    def query(self):
        if self.connected:
            return 'quert data'
        else:
            raise  ValueError('Cound not connect database')

'函数实现上下文管理器'
@contextmanager
def database_():
    db = Database()
    try:
        if not db.connected:
            db.connect()
        yield db
    except:
        db.close()

def handle_query():
    with database_() as db:
        print(db.query())

handle_query()
