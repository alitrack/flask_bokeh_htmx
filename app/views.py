from app.kmenas import get_clusters,cols
from . import app

from flask import request,render_template

x,y,cluster = cols[0],cols[0],4 #'sepal_length','sepal_length',3
@app.get("/")
def home():
    #cols =["sepal_length" , "sepal_width" , "petal_length" , "petal_width"]

    return render_template("kmeans.html",cols=cols,title="Home")

@app.post("/kmeans")
def post_kmeans():
    global x,y,cluster
    if 'x'  in request.form:
        x = request.form['x']
    if 'y'  in request.form:
        x = request.form['y']
    if 'cluster'  in request.form:
        cluster = int(request.form['cluster'])
    script, div=get_clusters(x,y,cluster)
    return render_template("viz/bokeh.html",script=script,div=div)
