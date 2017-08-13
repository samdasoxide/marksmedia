var gulp = require('gulp');
var less = require('gulp-less');
var browsersync = require('browser-sync').create();


// Tasks
gulp.task('less', function(){
	return gulp.src('theme/static/less/main.less')
		.pipe(less())
        .pipe(gulp.dest('theme/static/css'))
        .pipe(browsersync.reload({
        	stream: true
        }))
});

gulp.task('browsersync', function(){
	browsersync.init({
		server: {
			baseDir: 'output'
		}
	})
});

// Watchers
gulp.task('watch',['browsersync', 'less'], function(){
	gulp.watch('theme/static/less/**/*.less', ['less']);
	gulp.watch('output/**/*.html', browsersync.reload);
});
