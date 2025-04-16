
const parser = require('solidity-parser-antlr');
const fs = require('fs');

const filePath = process.argv[2];
if (!filePath) {
  console.error("No file path provided.");
  process.exit(1);
}

try {
  const content = fs.readFileSync(filePath, 'utf8');
  const ast = parser.parse(content, { loc: true });
  console.log(JSON.stringify(ast, null, 2));
} catch (err) {
  console.error(err.toString());
  process.exit(1);
}
