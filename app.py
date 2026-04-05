"""
PhishGuard AI - Email Phishing Analyzer
Author: Olojede Emmanuel Kolade
GitHub: github.com/EKO0312/PhishGuard-AI
"""

from flask import Flask, render_template, request, jsonify
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an expert cybersecurity analyst specializing in email phishing detection.

When given an email (headers + body), analyze it and respond ONLY in this exact JSON format:

{
  "risk_score": <number 0-100>,
  "risk_level": "<SAFE | LOW | MEDIUM | HIGH | CRITICAL>",
  "verdict": "<one sentence summary>",
  "red_flags": ["<flag1>", "<flag2>", ...],
  "safe_signals": ["<signal1>", "<signal2>", ...],
  "recommendation": "<what the user should do>",
  "technical_details": "<brief technical explanation>"
}

Be accurate. If no red flags exist, say it's safe. Never fabricate flags."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    email_content = data.get("email_content", "").strip()

    if not email_content:
        return jsonify({"error": "No email content provided"}), 400

    if len(email_content) > 5000:
        return jsonify({"error": "Email too long. Paste max 5000 characters."}), 400

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this email for phishing indicators:\n\n{email_content}"
                }
            ]
        )

        import json
        result_text = message.content[0].text
        result = json.loads(result_text)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
