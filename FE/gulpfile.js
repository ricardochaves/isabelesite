var gulp = require('gulp');
var browserSync = require('browser-sync');
var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");
var sass = require('gulp-sass');

sass({ indentedSyntax: true })

gulp.task('serve', function () {
    browserSync.init({
        server: {
            baseDir: '.'
        }
    });
});

gulp.task("ts", function () {
    return tsProject.src()
        .pipe(tsProject())
        .js.pipe(gulp.dest("js"))
        .pipe(gulp.dest('../mainapp/static/mainapp/js'))
        .pipe(browserSync.stream());
});

gulp.task('scss', function () {
    return gulp.src('scss/*.sass')
        .pipe(sass())
        .pipe(gulp.dest('css'))
        .pipe(gulp.dest('../mainapp/static/mainapp/css'))
        .pipe(browserSync.stream())
});

gulp.task('watch', ['serve', 'scss', 'ts'], function () {
    gulp.watch('scss/*.sass', ['scss']);
    gulp.watch('ts/*.ts', ['ts']);
    gulp.watch('index.html').on('change', browserSync.reload);
});

gulp.task('default', ['watch']);