from flask import Flask, render_template, request
import os
import yelp_api

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    food = request.values.get('food')
    results = None
    if address:
        results = yelp_api.get_businesses(address, food)
    return render_template('index.html', businesses=results)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)