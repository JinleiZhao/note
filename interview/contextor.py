'''
构造上下问管理器，需要用到__enter__ , __exit__
'''

class MyDataBase:
    
    def __init__(self):
        self.connected = False
    
    def __enter__(self):
        self.connect()
        return self  #f需要返回值

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.close()
        print(exc_type, exc_val, exc_tb)

    def connect(self):
        self.connected = True
    
    def close(self):
        self.connected = False
    
    def query(self):
        if self.connected:
            return 'quert data'
        else:
            raise  ValueError('Cound not connect database')


def handle_query():
    with MyDataBase() as db:
        print(db.query())

handle_query()