from sanic import Sanic
from sanic import response as res

app = Sanic()

prods = {'1': 'Apple', '2':'Banana', '3': 'Grapes', '4': 'Custard Apple'}

@app.route("/")
def index(request):
    return res.text("Hello World!!")

@app.route("/home")
def index(request):
    return res.text("Hello Home!!")

@app.route("/members")
def members(request):
    p = {"1": 'Ravi', "2": "Bhargav", "3": "Ram"}
    return res.json(p)

@app.route("/products")
def products(request):
    return res.json(prods)

@app.route("/products/<id>")
def single_prod(request, id):
    return res.json(prods[id])

if __name__ == "__main__": 
    app.run(port=8000, debug=True)
