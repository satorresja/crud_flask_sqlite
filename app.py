from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    connection = sql.connect("ToDo_data_base.db")
    connection.row_factory = sql.Row
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM ToDo_data_base ORDER BY Task ASC""")
    rows = cursor.fetchall()
    # connection.close()
    return render_template("index.html", rows=rows)


@app.route("/add_task", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        task = request.form["task"]
        completed = request.form.get("completed", False)
        connection = sql.connect("ToDo_data_base.db")
        cursor = connection.cursor()
        cursor.execute(
            "insert into ToDo_data_base(TASK,COMPLETED) values (?,?)", (task, completed)
        )
        connection.commit()
        flash("Task Added", "success")
        return redirect(url_for("index"))
    return render_template("add_task.html")


@app.route("/edit_task/<string:id>", methods=["POST", "GET"])
def edit_task(id):
    if request.method == "POST":
        task = request.form["task"]
        print(task)
        completed = request.form.get("completed", False)
        print(completed)
        connection = sql.connect("ToDo_data_base.db")
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE ToDo_data_base SET task=?,completed=? WHERE id=?""",
            (task, completed, id),
        )
        connection.commit()
        flash("Task Updated", "success")
        return redirect(url_for("index"))
    connection = sql.connect("ToDo_data_base.db")
    connection.row_factory = sql.Row
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM ToDo_data_base where id=?""", (id,))
    row = cursor.fetchone()
    print(row)
    return render_template("edit_task.html", row=row)


@app.route("/delete_task/<string:id>", methods=["GET"])
def delete_task(id):
    connection = sql.connect("ToDo_data_base.db")
    cursor = connection.cursor()
    cursor.execute("""delete from ToDo_data_base where ID=?""", (id,))
    connection.commit()
    flash("Task Deleted", "warning")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.secret_key = "lamasfacil"
    app.run(debug=True)
