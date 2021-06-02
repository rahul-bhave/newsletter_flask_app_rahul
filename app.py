from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            department = request.form['department']

            with sql.connect("newsletter.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()


            department_id = cur.execute('SELECT id FROM Department WHERE department_name = (?);',(department,)).fetchone()['id']


            cur.execute("INSERT INTO employee (name,email, department_id) VALUES (?,?,?)",(name, email, department_id))

            con.commit()
            msg = "Record successfully added"

        except Exception as e:
            print(e)
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            con.close()

    return render_template("new.html")

if __name__ == '__main__':
    app.run(debug = True)