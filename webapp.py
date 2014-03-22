import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/default-message')
def dm():
    return "This is a placeholder"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if flask.request.method == 'POST':
        print "Received: ", flask.request.form
    return flask.render_template('form.html')

if __name__ == '__main__':
    app.run()
