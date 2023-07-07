class Repository:
    def __init__(self, connect):    
        self.conn = connect
        
    def unit_of_work(self):
        self.conn.commit()