const path = require("path");
const utils = require("./utils");
const shared = require("./shared.config");

module.exports = {
  mode: "production",
  entry: utils.getPacks("./client/packs"),
  ...shared,
};
