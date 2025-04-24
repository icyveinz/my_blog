const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const path = require('path');

gulp.task('styles', function () {
    return gulp.src('sass/**/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(cleanCSS())
        .pipe(rename({ suffix: '.min' }))
        .pipe(gulp.dest('../static/css'));
});

gulp.task('default', gulp.parallel('styles'));