from src.rules.base_rule import BaseRule
from src.core.ast_walker import ASTWalker

class ReentrancyRule(BaseRule):
    def run(self):
        def callback(node):
            if node.get("type") == "FunctionCall" and "call" in str(node.get("expression", {})):
                self.issues.append({
                    "message": "Potential reentrancy vulnerability",
                    "location": node.get("loc", {}),
                    "severity": "High",
                    "rule": "Reentrancy"
                })
        ASTWalker().walk(self.ast, callback)