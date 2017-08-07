from flask import Flask, session, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = 'd41d8cd98f00b204e9800998ecf8427e'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['html_name']
    if len(name) < 1:
        flash('Must include name...')

    city = request.form['html_city']
    if len(city) < 1:
        flash('City cannot be empty...')

    stacks = request.form['html_stacks']
    if len(stacks) < 1:
        flash('Please include the number of stacks completed...')

    favorite = request.form['html_favorite']
    if len(favorite) < 1:
        flash('Favorite language cannot be empty...')

    graduation = request.form['html_graduation']
    if len(graduation) < 1:
        flash('Must include graduation date...')

    comments = request.form['html_comments']
    if len(comments) < 1:
        flash('Must include comments (no more than 120 characters...)')
    elif len(comments) < 121:
        flash('Comments must be 120 characters or less...')
        

    print comments
    
    return render_template('success.html', name=name, city=city, stacks=stacks, favorite=favorite, graduation=graduation, comments=comments)

app.run(debug=True)