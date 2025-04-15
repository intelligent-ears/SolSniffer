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
``` 
🔍 Usage

Run the analyzer on a Solidity file:

python -m src.main path/to/contract.sol

Example:

python -m src.main tests/contracts/VulnerableContract.sol

📁 Output

    🖥️ Console output of findings

    🧾 VulnerableContract_report.json – all findings in JSON

    🧪 VulnerableContract_report.sarif.json – GitHub-compatible SARIF format

📚 Implemented Rules
Rule ID	Description	Severity
UncheckedSend	Detects send() calls without checks	Medium

🤝 Contributing

Want to improve SolSniffer? Found a bug? Contributions are welcome!
📜 License

© intelligent-ears 2025
