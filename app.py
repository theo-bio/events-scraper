from flask import Flask, render_template_string

app = Flask(__name__)

FACEBOOK_PAGES_FILE = "facebook_pages.txt"

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Facebook Events Scraper UI</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        h1 { color: #3b5998; }
        ul { line-height: 2; }
        .url { color: #1877f2; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Facebook Pages Being Scraped</h1>
    {% if pages %}
        <ul>
        {% for page in pages %}
            <li><span class="url">{{ page }}</span></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No Facebook pages listed.</p>
    {% endif %}
    <p>Edit <code>facebook_pages.txt</code> to change this list.</p>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        with open(FACEBOOK_PAGES_FILE, "r") as f:
            # Ignore comment lines and blank lines
            pages = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except Exception:
        pages = []
    return render_template_string(TEMPLATE, pages=pages)

if __name__ == "__main__":
    app.run(debug=True)