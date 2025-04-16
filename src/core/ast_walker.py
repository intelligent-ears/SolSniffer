class ASTWalker:
    def walk(self, node, callback):
        if isinstance(node, dict):
            callback(node)
            for key in node:
                self.walk(node[key], callback)
        elif isinstance(node, list):
            for item in node:
                self.walk(item, callback)