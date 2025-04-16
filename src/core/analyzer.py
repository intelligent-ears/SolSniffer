from src.parser.solidity_parser import parse_solidity
from src.rules.rule_manager import RuleManager
from src.reporters.console_reporter import ConsoleReporter

class Analyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ast = None
        self.issues = []

    def analyze(self):
        print(f"📄 Parsing {self.file_path}...")
        self.ast = parse_solidity(self.file_path)

        print("🔍 Running security rules...")
        rule_manager = RuleManager(self.ast)
        self.issues = rule_manager.run()

        print("📢 Reporting findings...")
        reporter = ConsoleReporter(self.issues)
        reporter.display()

        return self.issues
