from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('nm')  # Mendapatkan nama dari input form
        return f"Hello, {name}! Welcome to the system."  # Tanggapan setelah input

    # Kode HTML untuk form login
    html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
    </head>
    <body>
        <h2>Login Form</h2>
        <form action="/" method="post">
            <p>Enter Name:</p>
            <input type="text" name="nm" placeholder="Your Name" required>
            <br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''
    return render_template_string(html_code)

@app.errorhandler(404)
def not_found(e):
    return "Page not found. Check the URL.", 404

if __name__ == '_main_':
    app.run(debug=True)