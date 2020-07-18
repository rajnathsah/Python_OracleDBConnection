# Import cx_Oracle module
import cx_Oracle

''' get_connection function to connect to oracle and return connection object.
    This function takes oracle username, password, and tns name as input and return connection object on successful connection.
    In case of any error, this method handles it print the error and return none.
'''
def get_connection(username, password, tnsname):
    try:                    
        return cx_Oracle.connect(username, password, tnsname)
    except Exception as ex:
        print('Error in Oracle database connection : {}'.format(ex))
        return None

''' close_connection function closes the connection and in case of any error, it handles it and print the error.
'''
def close_connection(con):
    try:
        con.close()
        print('Connection closed successfully.')
    except Exception as ex:
        print('Error in closing connection :{}'.format(ex))    

'''main method to call get_connection and close_connection function to connect and close connection respectively.
'''
if __name__=='__main__':
    # call get_connection function using database details    
    con=get_connection(<username>, <password>, <tnsnames>)
    if con:
        print(con.version)
        print('Connected successfully')      
        close_connection(con)
    else:
        print('No connection')    