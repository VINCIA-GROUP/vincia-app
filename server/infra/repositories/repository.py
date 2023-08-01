class Repository:
    def __init__(self, connect):    
        self.conn = connect
        
    def commit(self):
        self.conn.commit()