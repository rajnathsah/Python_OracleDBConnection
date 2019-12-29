# Import cx_Oracle module
import cx_Oracle

''' get_connection method to connect to oracle and return connection object.
    This method takes oracle username, password, hostname/ip address and oracle service name as input and return connection object on successful connection.
    In case of any error, this method handles it print the error and return none.
'''
def get_connection(username, password,hostname,servicename):
    try:            
        return cx_Oracle.connect('{user}/{passwd}@{host}/{service}'.format(user=username,passwd=password,host=hostname,service=servicename))
    except Exception as ex:
        print('Error in Oracle database connection : {}'.format(ex))
        return None

''' close_connection method closes the connection and in case of any error, it handles it and print the error.
'''
def close_connection(con):
    try:
        con.close()
        print('Connection closed successfully.')
    except Exception as ex:
        print('Error in closing connection :{}'.format(ex))    

'''main method to call get_connection method and close_connection method to connect and close connection.
'''
if __name__=='__main__':
    # call connection method using database details    
    con=get_connection('<username>', '<password>', '<database host name/ip name>', '<oracle service name>')
    if con:
        print(con.version)
        print('Connected successfully')
        
        try:
            # create sql statement and execute query and print result
            cur=con.cursor()
            sql_statement='select * from departments order by department_id'
        
            cur.execute(sql_statement)        
        
            for result in cur:
                print(result)
        except Exception as ex:
            print('Error in executing sql statement : {} '.format(ex))
        finally:
            # post execution close connection in finally block
            close_connection(con)        
    else:
        print('No connection')    
