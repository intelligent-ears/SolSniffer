import json

class SARIFReporter:
    def __init__(self, issues):
        self.issues = issues

    def save(self, output_path):
        sarif = {
            "version": "2.1.0",
            "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0.json",
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "SolSniffer",
                            "informationUri": "https://example.com",
                            "rules": [
                                {
                                    "id": issue.get("rule", "UnknownRule"),
                                    "shortDescription": {"text": issue.get("message", "")},
                                    "defaultConfiguration": {"level": issue.get("severity", "warning").lower()}
                                } for issue in self.issues
                            ]
                        }
                    },
                    "results": [
                        {
                            "ruleId": issue.get("rule", "UnknownRule"),
                            "level": issue.get("severity", "warning").lower(),
                            "message": {"text": issue.get("message", "")},
                            "locations": [
                                {
                                    "physicalLocation": {
                                        "artifactLocation": {"uri": issue.get("location", {}).get("source", "")},
                                        "region": {
                                            "startLine": issue.get("location", {}).get("start", {}).get("line", 0),
                                            "startColumn": issue.get("location", {}).get("start", {}).get("column", 0)
                                        }
                                    }
                                }
                            ]
                        } for issue in self.issues
                    ]
                }
            ]
        }

        with open(output_path, 'w') as f:
            json.dump(sarif, f, indent=2)
        print(f"\U0001F4C1 SARIF report saved to {output_path}")
