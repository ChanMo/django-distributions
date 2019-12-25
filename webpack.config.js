const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: './distributions/static/distributions/src/app.js',
  output: {
    path: path.resolve('./distributions/static/distributions/dist/'),
    filename: 'app.js'
  },
  plugins: [
    //new CleanWebpackPlugin()
  ],
  module: {
    rules: [
      {test:/\.js$/, exclude:/node_modules/, use:{
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react']
        }
      }}
    ]
  },
  devtool: 'inline-source-map',
  optimization: {
    minimizer: [new UglifyJsPlugin()],
  },
  devServer: {
    contentBase: path.resolve('./distributions/templates/distributions/'),
  },
}
