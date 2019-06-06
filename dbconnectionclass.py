import cx_Oracle

''' Python class to connect to database and close connection automatically
'''
class Dbconnection:
    # method to initialize con variable and connect to database
    def __init__(self,dbusername,dbpassword,dbhostname,dbservicename):
        self.con=None
        try:            
            self.con=cx_Oracle.connect('{user}/{passwd}@{host}/{service}'.format(user=dbusername,passwd=dbpassword,host=dbhostname,service=dbservicename))
            print('Connection created')
        except Exception as ex:
            print('Error in database connection : {}'.format(ex))
    
    # method to return self
    def __enter__(self):        
        return self
    
    # method called automatically to close the connection
    def __exit__(self, exception_type, exception_value, traceback):        
        try:
            self.con.close()
            print('Closed connection')
        except Exception as ex:
            print('Error in closing connection : {}'.format(ex))

if __name__=='__main__':
    with Dbconnection('<username>', '<password>', '<database host name/ip name>', '<oracle service name>') as dbcon:
        # check connection object and then write data processing logic
        if dbcon.con:    
            try:
                cur=dbcon.con.cursor()
                sql_statement='select * from departments order by department_id'
                
                cur.execute(sql_statement)
                
                for result in cur:
                    print(result)
                    
            except Exception as ex:
                print('Error in data processing : {}'.format(ex))
        else:
            print('Connection failed.')
