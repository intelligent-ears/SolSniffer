class ConsoleReporter:
    def __init__(self, issues):
        self.issues = issues

    def display(self):
        if not self.issues:
            print("✅ No issues found.")
            return

        for issue in self.issues:
            print(f"[{issue['type']}] Line {issue['line']}: {issue['message']}")
