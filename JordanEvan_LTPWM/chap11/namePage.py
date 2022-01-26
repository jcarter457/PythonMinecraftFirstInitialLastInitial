from flask import Flask
app=Flask(__name__)

@app.route("/")
def showName():
    return "BIG HOT MEN!!!! (no virus)"

app.run()