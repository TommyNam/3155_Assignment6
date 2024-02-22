from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Hardcoded list of events
events = ["Carnival", "Nascar Event", "Career Fair", "Comedy Show", "Amusement Park Event"]

registered_users = {}

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    event = request.form.get('event')

    # validation
    if not name or not event:
        return "Name and event are required."

    if event not in events:
        return "Invalid event."

    registered_users[name] = event

    # Redirect to registered users
    return redirect(url_for('show_registered_users'))

@app.route('/registered_users')
def show_registered_users():
    return render_template('registered_users.html', registered_users=registered_users)

@app.route('/delete_user/<name>', methods=['POST'])
def delete_user(name):
    if name in registered_users:
        del registered_users[name]

    # Redirect registered users
    return redirect(url_for('show_registered_users'))

if __name__ == '__main__':
    app.run(debug=True)
