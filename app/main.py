from flask import Flask, render_template, request
from services.ats_engine import calculate_ats_score

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form.get("resume", "")
    job_description = request.form.get("job_description", "")

    result = calculate_ats_score(resume, job_description)

    return render_template(
        "result.html",
        score=result["score"],
        matched=result["matched"],
        missing=result["missing"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# GitHub Actions CI/CD practical demo
