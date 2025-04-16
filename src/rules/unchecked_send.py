from src.rules.base_rule import BaseRule
from src.core.ast_walker import ASTWalker

class UncheckedSendRule(BaseRule):
    def run(self):
        def callback(node):
            if node.get("type") == "FunctionCall":
                expression = node.get("expression", {})
                if isinstance(expression, dict) and expression.get("memberName") == "send":
                    line = node.get("loc", {}).get("start", {}).get("line", -1)
                    self.issues.append({
                        "rule": "UncheckedSend",  # ✅ Required for SARIF
                        "type": "UncheckedSend",  # Optional for console
                        "message": "Ether send() should be checked for success.",
                        "line": line,
                        "severity": "Medium"
                    })
        ASTWalker().walk(self.ast, callback)
