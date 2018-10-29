var gulp = require("gulp");
var browserSync = require("browser-sync");
var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");
var sass = require("gulp-sass");
let cleanCSS = require("gulp-clean-css");
var concat = require("gulp-concat");
let merge = require("merge2");

var uglifyes = require("uglify-es");
var composer = require("gulp-uglify/composer");
var uglify = composer(uglifyes, console);

gulp.task("serve", function() {
  browserSync.init({
    server: {
      baseDir: "."
    }
  });
});

gulp.task("ts", function() {
  ts_ts = tsProject
    .src()
    .pipe(tsProject())
    .js.pipe(gulp.dest("js"));
  // .pipe(browserSync.stream());

  concat_ts = gulp
    .src(["./js/*.js"])
    .pipe(concat("all.js"))
    .pipe(gulp.dest("./dist"))
    .pipe(gulp.dest("../mainapp/static/mainapp/js"))
    .pipe(browserSync.stream());

  return merge(ts_ts, concat_ts);
});

gulp.task("scss", function() {
  css_ts = gulp
    .src("scss/*.sass")
    .pipe(sass({ indentedSyntax: true }))
    .pipe(gulp.dest("css"));
  // .pipe(browserSync.stream());

  concat_ts = gulp
    .src(["./css/*.css"])
    .pipe(concat("all.css"))
    .pipe(cleanCSS({ compatibility: "ie8" }))
    .pipe(gulp.dest("./dist"))
    .pipe(gulp.dest("../mainapp/static/mainapp/css"))
    .pipe(browserSync.stream());

  return merge(css_ts, concat_ts);
});

gulp.task("watch", ["serve", "scss", "ts"], function() {
  gulp.watch("scss/*.sass", ["scss"]).on("change", browserSync.reload);
  gulp.watch("ts/*.ts", ["ts"]).on("change", browserSync.reload);
  gulp.watch("index.html").on("change", browserSync.reload);
});

gulp.task("default", ["watch"]);
