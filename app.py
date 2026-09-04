from flask import Flask, request, render_template

app = Flask(__name__)

index = {
    "python": ["https://www.python.org/"],
    "github": ["https://github.com/"],
    "google": ["https://www.google.com/"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "").lower().strip()
    results = index.get(query, [])
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
