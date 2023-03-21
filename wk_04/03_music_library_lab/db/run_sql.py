import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    # Function that runs sql and returns list with contents from db

    # set up var for connection
    conn = None
    # set up empty list to be populated and returned
    results = [] 
    # try to connect to the db
    try:
        conn = psycopg2.connect("dbname='taskmanager'")
        # get cursor from the database
            #  This is an object that steps through rows
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # execute the sql
        cur.execute(sql, values)
        # commit the execution
        conn.commit()
        # get the results 
        results = cur.fetchall()
        # close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the db connection
            conn.close()
    # return the list set up earlier 
    return results



