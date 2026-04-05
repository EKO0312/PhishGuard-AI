# 🛡️ PhishGuard AI — Email Phishing Analyzer

> AI-powered phishing email detection tool built by **Olojede Emmanuel Kolade**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![AI Powered](https://img.shields.io/badge/AI-Powered-purple)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)

---

## 🔍 What It Does

PhishGuard AI analyzes email content and detects phishing attempts using an AI analysis engine. Paste any suspicious email and instantly receive:

- ✅ **Risk Score** (0–100)
- 🚩 **Red Flags** detected (spoofed domains, urgency tactics, suspicious links)
- 🛡️ **Safe Signals** (legitimate sender patterns)
- 🔬 **Technical Analysis** (header anomalies, encoding tricks)
- 💡 **Actionable Recommendation**

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/EKO0312/PhishGuard-AI.git
cd PhishGuard-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export ANTHROPIC_API_KEY="your_api_key_here"

# 4. Run
python app.py

# 5. Open browser at http://localhost:5000
```

---

## 🧠 How It Works

1. User pastes email content into the web interface
2. Flask backend sends it to the AI analysis engine with a custom-built cybersecurity detection prompt
3. The engine analyzes for 20+ phishing indicators including spoofed domains, urgency language, malicious links, and header anomalies
4. Results are returned as structured JSON and displayed visually with risk scoring

---

## 💡 Use Cases

- Personal email protection
- Security awareness training for small businesses
- SOC analyst triage tool
- Cybersecurity education and research

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python + Flask | Backend API |
| AI Analysis Engine | Threat detection & risk scoring |
| HTML / CSS / JavaScript | Frontend interface |

---

## 📊 Sample Output

```
Risk Score:       85 / 100
Risk Level:       HIGH RISK
Verdict:          Email shows multiple phishing indicators

Red Flags:
  🚩 Sender domain does not match display name
  🚩 Urgent language designed to pressure action
  🚩 Link destination differs from displayed URL
  🚩 Generic greeting — not personalized

Recommendation:   Do not click any links. Report to IT security team.
```

---

## 👨‍💻 Author

**Olojede Emmanuel Kolade**
Cybersecurity & AI Security Enthusiast | Nigeria 🇳🇬
Google Cybersecurity Certificate (In Progress) | AI Governance Certified

---

## 📄 License

MIT License — free to use and modify.
