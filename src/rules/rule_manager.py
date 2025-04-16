from src.rules.reentrancy import ReentrancyRule
from src.rules.unchecked_send import UncheckedSendRule
from src.rules.tx_origin import TxOriginRule

class RuleManager:
    def __init__(self, ast):
        self.ast = ast
        self.issues = []

    def run(self):
        def traverse(node):
            if isinstance(node, dict):
                node_type = node.get("type")

                # Reentrancy check
                if node_type == "FunctionCall":
                    expr = node.get("expression", {})
                    if isinstance(expr, dict) and expr.get("type") == "MemberAccess":
                        if "call" in expr.get("memberName", ""):
                            self.issues.append({
                                "type": "Reentrancy",
                                "message": "Potential reentrancy via .call()",
                                "line": node.get("loc", {}).get("start", {}).get("line", -1)
                            })

                # tx.origin check
                if "tx.origin" in str(node):
                    self.issues.append({
                        "type": "InsecureAuth",
                        "message": "Usage of tx.origin is insecure for authentication.",
                        "line": node.get("loc", {}).get("start", {}).get("line", -1)
                    })

                # send() check
                if node_type == "FunctionCall":
                    if "send" in str(node.get("expression", {})):
                        self.issues.append({
                            "type": "UncheckedSend",
                            "message": "Ether send() should be checked for success.",
                            "line": node.get("loc", {}).get("start", {}).get("line", -1)
                        })

                for key in node:
                    traverse(node[key])

            elif isinstance(node, list):
                for item in node:
                    traverse(item)

        traverse(self.ast)
        return self.issues
