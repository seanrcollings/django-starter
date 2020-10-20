const path = require("path");
const utils = require("./utils");

const thing = utils.getPacks("client/packs");
console.log(thing);

module.exports = {
  entry: utils.getPacks("./client/packs"),
  output: {
    path: path.resolve(__dirname, "../../client/static/client/js"), // Should be in STATICFILES_DIRS
    filename: "[name].js",
    chunkFilename: "[id]-[chunkhash].js",
    publicPath: "/static/",
  },
  devServer: {
    port: 3000,
    writeToDisk: true,
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
};
