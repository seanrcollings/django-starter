const path = require("path");
const utils = require("./utils");

module.exports = {
  mode: "production",
  entry: utils.getPacks("./client/packs"),
  output: {
    path: path.resolve("./client/static/client/js"),
    filename: "[name].js",
    chunkFilename: "[id]-[chunkhash].js",
    publicPath: "/static/",
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          "style-loader",
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },
    ],
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js"],
  },
};
