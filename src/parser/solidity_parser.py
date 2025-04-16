import os
import subprocess
import json

def parse_solidity(file_path: str):
    script_dir = os.path.dirname(__file__)
    parser_path = os.path.join(script_dir, "../../parser.js")
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # 🔁 TEMP FIX: Rewrite call{value:...}("") to workaround parser limitation
    code = code.replace(".call{value:", ".call.value(").replace("}(\"", ", \"") + ")"

    result = subprocess.run(
        ["node", parser_path, file_path],
        input=code.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        print(f"❌ Parsing failed: {result.stderr.decode()}")
        return None

    return json.loads(result.stdout.decode())
