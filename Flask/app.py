from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form to take number input
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Math Table Generator</title>
</head>
<body>
    <h2>Enter a number to generate its multiplication table:</h2>
    <form method="POST" action="/table">
        <input type="number" name="number" required>
        <button type="submit">Generate Table</button>
    </form>
</body>
</html>
"""

# HTML to show multiplication table
table_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
    <style>
        table, th, td {
            border: 1px solid black;
            padding: 8px;
        }
        table {
            border-collapse: collapse;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h2>Multiplication Table for {{ number }}:</h2>
    <table>
        {% for i in range(1, 11) %}
        <tr>
            <td>{{ number }} x {{ i }}</td>
            <td>{{ number * i }}</td>
        </tr>
        {% endfor %}
    </table>
    <br>
    <a href="/">Go Back</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/table', methods=['POST'])
def table():
    number = int(request.form['number'])
    return render_template_string(table_html, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)