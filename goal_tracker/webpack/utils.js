const path = require("path");
const fs = require("fs");
const process = require("process");

function getPacks(directory) {
  const directoryPath = path.join(process.cwd(), directory);
  const files = fs.readdirSync(directoryPath);
  const packs = {};
  files.forEach(file => (packs[file.split(".")[0]] = `${directory}/${file}`));
  return packs;
}

module.exports = {
  getPacks,
};
