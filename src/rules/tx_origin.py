from src.rules.base_rule import BaseRule
from src.core.ast_walker import ASTWalker

class TxOriginRule(BaseRule):
    def run(self):
        def callback(node):
            if node.get("type") == "MemberAccess" and node.get("memberName") == "origin":
                self.issues.append({
                    "message": "Use of tx.origin for authentication",
                    "location": node.get("loc", {}),
                    "severity": "High",
                    "rule": "TxOrigin"
                })
        ASTWalker().walk(self.ast, callback)