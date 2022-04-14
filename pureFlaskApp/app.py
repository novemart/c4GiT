from flask import Flask, request

app = Flask(__name__)

@app.route('/home')
def welcome():
    return "Hello you!"

# endpoint with parameter
@app.route('/home/<name>')
def welcome_with_name(name):
    return "Hello "+ name


@app.route('/home', methods=['POST'])
def welcome_post():
    data = request.get_json()
    print(data)
    return data['name'] + data['surname']


if __name__=='__main__':
    app.run(debug=True)