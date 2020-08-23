var gulp = require("gulp"),
    sass = require("gulp-sass"),
    postcss = require("gulp-postcss"),
    autoprefixer = require("autoprefixer"),
    cssnano = require("cssnano"),
    sourcemaps = require("gulp-sourcemaps"),
    ts = require('gulp-typescript'),
    concat = require('gulp-concat'),
    cleanCSS = require('gulp-clean-css'),
    browserSync = require("browser-sync").create(),
    log = require('fancy-log'),
    critical = require('critical').stream;

var tsProject = ts.createProject('tsconfig.json');
var uglify = require('gulp-uglify-es').default;

var paths = {
    styles: {
        // By using styles/**/*.sass we're telling gulp to check all folders for any sass file
        src: "scss/*.sass",
        // Compiled files will end up in whichever folder it's found in (partials are not compiled)
        dest: "css/"
    },

    ts: {
        src: "ts/*.ts",
        dest: "js/"
    },

    css: {
        src: "css/*css",
        dest: "css/"
    },

    js:{
        src: "js/*.js",
        dest: "js/"
    }

    // Easily add additional paths
    // ,html: {
    //  src: '...',
    //  dest: '...'
    // }
};

function in_line_critical_css(){
    return gulp
        .src('./index.html')
        .pipe(
          critical({
            base: '.',
            inline: true,
            css: ['dist/all.css'],
              target: {
    html: 'index-critical.html',
  },
          })
        )
        .on('error', err => {
          log.error(err.message);
        })
        .pipe(gulp.dest('dist'));
}


function concatCss() {
    return gulp
        .src(['css/a_reset.css','css/b_pure.css','css/main.css'])
        .pipe(concat('all.min.css'))
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest(paths.css.dest));
}

function concatJs() {
    return gulp
        .src(paths.js.src)
        .pipe(concat('all.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(paths.js.dest));
}

function style() {
    return gulp
        .src(paths.styles.src)
        // Initialize sourcemaps before compilation starts
        .pipe(sourcemaps.init())
        .pipe(sass())
        .on("error", sass.logError)
        // Use postcss with autoprefixer and compress the compiled file using cssnano
        .pipe(postcss([autoprefixer(), cssnano()]))
        // Now add/write the sourcemaps
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(paths.styles.dest))
        // Add browsersync stream pipe after compilation
        .pipe(browserSync.stream());
}


function ts() {
    return gulp
        .src(paths.ts.src)
        .pipe(sourcemaps.init())
        .pipe(tsProject())
        .js.pipe(gulp.dest(paths.ts.dest));
}



// A simple task to reload the page
function reload() {
    browserSync.reload();
}

// Add browsersync initialization at the start of the watch task
function watch() {
    browserSync.init({
        // You can tell browserSync to use this directory and serve it as a mini-server
        server: {
            baseDir: "."
        },
        // proxy: "localhost"
        // If you are already serving your website locally using something like apache
        // You can use the proxy setting to proxy that instead
        // proxy: "yourlocal.dev"
    });
    gulp.watch(paths.styles.src, style);
    gulp.watch(paths.ts.src, ts);
    // We should tell gulp which files to watch to trigger the reload
    // This can be html or whatever you're using to develop your website
    // Note -- you can obviously add the path to the Paths object
    //gulp.watch("src/*.html", reload);
    gulp.watch("index.html").on('change', in_line_critical_css);
    gulp.watch("index.html").on('change', browserSync.reload);

}

// We don't have to expose the reload function
// It's currently only useful in other functions


// Don't forget to expose the task!
exports.watch = watch;
exports.in_line_critical_css = in_line_critical_css;
// Expose the task by exporting it
// This allows you to run it from the commandline using
// $ gulp style
exports.style = style;
exports.ts = ts;

/*
 * Specify if tasks run in series or parallel using `gulp.series` and `gulp.parallel`
 */
var build = gulp.parallel( gulp.series( ts, concatJs), gulp.series( style, concatCss), watch);

/*
 * You can still use `gulp.task` to expose tasks
 */
//gulp.task('build', build);

/*
 * Define default task that can be called by just running `gulp` from cli
 */
gulp.task('default', build);