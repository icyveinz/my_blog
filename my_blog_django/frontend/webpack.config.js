const path = require("path");

module.exports = {
    mode: "production",
    entry: {
        testing: [
            "./js/testing/testing.js"
        ]
    },
    output: {
        filename: 'bundled_[name].js',
        path: path.resolve(__dirname, '../static/js'),
    }
};
