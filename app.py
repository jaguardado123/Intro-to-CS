# Import libraries and packages, they contain additional functions.
from flask import Flask, render_template

# Create web application using Flask
app = Flask(__name__)

# Create our routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutpage.html')
    
# Start our web application
if __name__ == "__main__":
    app.run()