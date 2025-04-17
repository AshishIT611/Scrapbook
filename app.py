from flask import Flask,render_template,request,flash
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="ashish143@"
app.config["MYSQL_DB"]="scrapbook1"
mysql=MySQL(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/write",methods=["GET","POST"])
def write():
    success=None
    if request.method=="POST":
        title=request.form["title"]
        content=request.form["content"]
        date=request.form["date"]
        try:
            cur=mysql.connection.cursor()
            cur.execute("INSERT INTO scrap VALUES(%s,%s,%s)",(title,content,date))
            mysql.connection.commit()
            cur.close()
            success="Insertted Successfully"
        except Exception as e:
            success=f"Error:{str(e)}"
    return render_template("write.html",success=success)
@app.route("/read")
def read():
    result=None
    try:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM scrap")
        result=cur.fetchall()
        cur.close()
    except Exception as e:
        result=f"Error:{str(e)}"
    return render_template("read.html",result=result)
if __name__=="__main__":
    app.run(debug=True)