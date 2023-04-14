from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read in details for page
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route('/')
def homePage():
    name = "Francisco Orta"
    details = readDetails('static/details.txt')
    return render_template("base.html", name=name, aboutMe=details)

@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # if request.form['name']:
        #     name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])

    return render_template('form.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=2000)