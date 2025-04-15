# 🕵️‍♂️ SolSniffer

SolSniffer is a static analysis tool for **Solidity smart contracts**, built in Python. It detects common vulnerabilities and generates clean reports in both **JSON** and **SARIF** formats for easy integration with tools like GitHub Code Scanning.

---

## 🚀 Features

- ✅ Parses Solidity smart contracts using a JS-based parser
- 🛡️ Detects critical vulnerabilities like unchecked `send()` calls
- 📊 Outputs findings in:
  - Console view
  - JSON report
  - SARIF (Static Analysis Results Interchange Format) report

---

## 📦 Installation

**Requirements:**

- Python 3.9 or newer
- Node.js (used for parsing Solidity code)

**Setup:**

```bash
git clone https://github.com/intelligent-ears/SolSniffer.git
cd SolSniffer
pip install -r requirements.txt
npm install
