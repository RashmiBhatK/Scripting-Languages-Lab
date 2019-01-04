'''10)Python and JavaScript – Student Registration: Design a HTML form that displays
● Two text fields to input the user’s USN and Date of Birth.
● Three text boxes to input three marks.
Validate the data entry on the server side using Javascript so that null values are not accepted
for all the five text boxes.
Validate the entry on server-side using Python to ensure that USN is accepted in a proper
pattern as well as date validations are done.
Calculate the average using Python on server-side and display the result.'''


from flask import Flask,redirect,request,url_for,render_template
import time
import re

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def fun():
  if request.method == "GET":
    return render_template("indexJS.html")
  if request.method == "POST":
    if request.form["usn"] == "" or request.form["dob"] == "":
       msg="All form fields are required"
       return render_template("indexJS.html",msg=msg)

    try:
        time.strptime(request.form["dob"],"%d/%m/%Y")
    except ValueError:
        msg="Date is invalid"
        return render_template("indexJS.html",msg=msg)

    usn_pattern="^[0-9][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
    if not re.match(usn_pattern,request.form["usn"]):
        msg="usn is invalid"
        return render_template("indexJS.html",msg=msg)

    s1=int(request.form["m1"])
    s2=int(request.form["m2"])
    s3=int(request.form["m3"])
    avg=(s1+s2+s3)/3

  return render_template("success.html",avg=avg)

if __name__ == '__main__':
 app.run()


