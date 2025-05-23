from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Example: handle form submission here if needed
        name = request.form.get('name')
        email = request.form.get('email')
        # Process form data as required
        return f"Received name: {name}, email: {email}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
