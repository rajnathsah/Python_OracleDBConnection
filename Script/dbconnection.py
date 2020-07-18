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
    con=get_connection('<username>', '<password>', '<host>', '<service/tns name>')
    if con:
        print(con.version)
        print('Connected successfully')
        
        try:
            # create sql statement and execute query and print result
            cur=con.cursor()
            sql_statement='select * from departments order by department_id'
        
            cur.execute(sql_statement)        
            # fetch record at a time by looping
            for result in cur:
                print(result)            
            cur.close()
            
            cur=con.cursor()
            cur.execute(sql_statement)    
            # fetch one record
            res = cur.fetchone()
            print(res)
            cur.close()
            
            cur=con.cursor()            
            cur.execute(sql_statement)
            # fetch many
            res = cur.fetchmany(numRows=2)
            print(res)
            cur.close()
            
            cur=con.cursor()            
            cur.execute(sql_statement)
            # fetch all record at a time
            res = cur.fetchall()
            print(res)
            cur.close()
            
            cur=con.cursor()            
            # define arraysize to reduce network round trip
            cur.arraysize = 100
            cur.execute(sql_statement)
            res = cur.fetchall()
            print(res)
            cur.close()
            
            cur=con.cursor()            
            # bind variable to use soft parse
            cur.prepare('select * from departments where department_id= :id')
            cur.execute(None,{'id':210})
            res = cur.fetchall()
            print(res)
            
            cur.execute(None, {'id':110})
            res = cur.fetchall()
            print(res)
            cur.close()
                                                
            # insert multiple rows at time to improve performance
            rows = [(1,'first'),
                    (2,'second'),
                    (3,'third'),
                    (4,'fourth'),
                    (5,'fifth'),
                    (6,'sixth'),
                    (7,'seventh')]
            
            cur = con.cursor()
            cur.bindarraysize = 7
            cur.setinputsizes(int,20)
            cur.executemany("insert into mytab(id, data) values (:1,:2)",rows)
            con.commit()
            cur.close()
            
            # query the inserted data
            cur = con.cursor()
            cur.execute('select * from mytab')
            res = cur.fetchall()
            print(res)
            cur.close()
            
            # calling function with parameter and printing returned value
            cur = con.cursor()
            res = cur.callfunc('myfunc', cx_Oracle.NUMBER, (2,'abc'))
            con.commit()
            print(res)
            cur.close()
            
            # calling procedure with parameter
            cur = con.cursor()
            res = cur.callproc('myproc',(123,'bcd'))            
            cur.close()
            
        except Exception as ex:
            print('Error in executing sql statement : {} '.format(ex))
        finally:
            # post execution close connection in finally block
            close_connection(con)        
    else:
        print('No connection')    
