const path = require("path");
const utils = require("./utils");

module.exports = {
  mode: "development",
  entry: "./client/packs/tests",
  output: {
    path: path.resolve("./client/static/client/js"),
    filename: "[name].js",
    chunkFilename: "[id]-[chunkhash].js",
    publicPath: "/static/",
  },
  devServer: {
    overlay: true,
    port: 3000,
    hot: true,
    compress: true,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
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
  devtool: "inline-source-map",
};
