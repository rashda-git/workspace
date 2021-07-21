from flask import Flask,jsonify,request,g
import mysql.connector

app=Flask(__name__)


def connect_db():
    sql = mysql.connector.connect(user='flaskuser', password='flaskuser',
                              host='127.0.0.1',
                              database='flaskapp')
    
    return sql

def get_db():
    if not hasattr(g,'conn'):
        g.conn = connect_db()
    return g.conn
    
@app.teardown_appcontext
def close_connection(error):
    if hasattr(g,"conn"):
        g.conn.close()



@app.route('/query')
def query():
    
    a=request.args.get('a')
    b=request.args.get('b')

    arr_a = [float(x) for x in a.split(',')]
    arr_b = [float(x) for x in b.split(',')]
    db = get_db()
    cursor = db.cursor()
    query = 'INSERT INTO RESULT (A,B,SUM,SUB,MUL,DIVISION) VALUES(%s,%s,%s,%s,%s,%s)'
    for i in range(len(arr_a)):
        data = (arr_a[i],
                arr_b[i],
                arr_a[i]+arr_b[i],
                arr_a[i]-arr_b[i],
                arr_a[i]*arr_b[i],
                arr_a[i]/arr_b[i]
             )
        cursor.execute(query,data)
        
    db.commit()




    return "<h1>Success</h1>"

@app.route('/results')
def results():
    db = get_db()

    curr = db.cursor(dictionary=True)
    curr.execute('SELECT * FROM RESULT')
    data = curr.fetchall()
    result  = [ {
        'a':x['a'],
        'b': x['b'],
        'add': x['sum'],
        'sub': x['sub'],
        'mul': x['mul'],
        'div': x['division']
    } for x in data]
    print(data)
    return  jsonify(result)

@app.route('/deleteall')
def deleteall():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('delete  FROM RESULT')
    db.commit()

    return '<h1>Success</h1>'
if __name__=='__main__' :
    app.run(debug=True)    