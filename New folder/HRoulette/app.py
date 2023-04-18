from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Function to read in details for page
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

def index():
    return render_template('index.html')

@app.route('/')
def homePage():
    name = "Welcome to the Healthy Roulette!"
    details = readDetails('static/details.txt')
    return render_template("base.html", name=name, aboutMe=details)

@app.route('/meal')
def get_meal():
    meal_options = ["Oatmeal with Fruit", "Grilled Chicken Salad", "Baked Salmon with Vegetables", "Quinoa Salad with Chicken", "Turkey Chili", "Roasted Vegetable Stir-Fry"]
    meal_suggestion = random.choice(meal_options)
    return render_template('meal.html', meal=meal_suggestion)

@app.route('/user/<name>')
def greet(name):
    return f'<p>still {name}?</p>'

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