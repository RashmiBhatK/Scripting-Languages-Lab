'''9)Python and JavaScript - Shopping Cart Application: Design a simple Shopping Cart application
which allows users to add items to their cart from a list of products. Allow users to view their
cart (items and quantities of each).
'''


from flask import Flask,redirect,render_template,url_for,session,request


app=Flask(__name__)

app.secret_key="secret"

@app.route("/",methods=["GET","POST"])
def store():
 if request.method == "GET":
   return render_template("store.html")
 if request.method == "POST":
   for item in ["eggs","milk","bread"]:
     if item not in session:
       session[item] = int(request.form[item])
     else:
       session[item] += int(request.form[item])
   return redirect(url_for('cart'))
@app.route("/cart",methods=["GET","POST"])
def cart():
  cart=[]
  total=0
  for item in ["eggs","milk","bread"]:
     cart.append({"name":item.capitalize(),"quantity":session[item]})
  for item in ["eggs","milk","bread"]:
     if item == "eggs":
       total += session[item]*5
     elif item == "milk":
       total +=session[item]*5
     elif item == "bread":
       total += session[item]*5
  return render_template("cart.html",cart=cart,total=total)
if __name__ == '__main__':
 app.run()


