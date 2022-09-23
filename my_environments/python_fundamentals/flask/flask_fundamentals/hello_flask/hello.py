from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/user')       
def users():
    return 'Hello every user' 

@app.route('/hmodi')       
def tt():
    return 'Hello every user' 

@app.route('/name')       
def kk():
    return 'Hello every one the name is'+"and the id is:" 


if __name__=="__main__":  
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello!</h1>"

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)