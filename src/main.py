
from src.core.analyzer import Analyzer
from src.reporters.json_reporter import JSONReporter
from src.reporters.sarif_reporter import SARIFReporter
import sys
import os

def main():
    if len(sys.argv) < 2:
        print(r"Usage: python -m src.main tests/contracts/VulnerableContract.sol")
        exit(1)

    target_path = sys.argv[1]

    if os.path.isdir(target_path):
        from src.core.contract_loader import get_solidity_files
        files = get_solidity_files(target_path)
    else:
        files = [target_path]

    for file_path in files:
        analyzer = Analyzer(file_path)
        issues = analyzer.analyze()
        print("-" * 50)

        base_name = os.path.basename(file_path).replace(".sol", "")

        json_reporter = JSONReporter(issues)
        json_reporter.save(f"{base_name}_report.json")

        sarif_reporter = SARIFReporter(issues)
        sarif_reporter.save(f"{base_name}_report.sarif.json")

if __name__ == "__main__":
    main()
