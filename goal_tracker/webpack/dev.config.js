const utils = require("./utils");
const shared = require("./shared.config");

module.exports = {
  mode: "development",
  entry: utils.getPacks("./client/packs"),
  devtool: "inline-source-map",
  ...shared,
};
