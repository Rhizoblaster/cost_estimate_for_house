
from flask import Flask, render_template, request

app = Flask(__name__)

def estimate_cost(sqft, num_bathrooms, num_stories, has_garage):
    base_cost_per_sqft = 150
    extra_bathroom_cost = 10000
    extra_story_cost = 50000
    garage_cost = 20000

    estimate = sqft * base_cost_per_sqft
    if num_bathrooms > 2:
        estimate += (num_bathrooms - 2) * extra_bathroom_cost
    if num_stories > 1:
        estimate += (num_stories - 1) * extra_story_cost
    if has_garage:
        estimate += garage_cost

    return estimate

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sqft = int(request.form['sqft'])
        num_bathrooms = int(request.form['num_bathrooms'])
        num_stories = int(request.form['num_stories'])
        has_garage = True if request.form.get('has_garage') else False
        estimate = estimate_cost(sqft, num_bathrooms, num_stories, has_garage)
        return render_template('result.html', estimate=estimate)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
