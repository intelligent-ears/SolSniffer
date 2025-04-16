import json

class JSONReporter:
    def __init__(self, issues):
        self.issues = issues

    def save(self, output_path):
        with open(output_path, 'w') as f:
            json.dump(self.issues, f, indent=2)
        print(f"\U0001F4C1 JSON report saved to {output_path}")