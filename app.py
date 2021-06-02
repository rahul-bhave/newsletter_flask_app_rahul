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
                cur = con.cursor()

            cur.execute("INSERT INTO employee (name,email, department_id) VALUES (?,?,?)",(name, email, department))

            con.commit()
            msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            con.close()

    return render_template("new.html")

if __name__ == '__main__':
    app.run(debug = True)