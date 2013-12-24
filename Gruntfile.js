module.exports = function (grunt)
{

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: 'build/<%= pkg.name %>.min.js'
      }
    },


    less: {
      development: {
        options: {
          paths: [".static/css"],
          compress: false,
          yuicompress: false,
          optimization: 2
        },
        files: {
          // target.css file: source.less file
          "./static/css/style.css": "./src/less/style.less"
        }
      },
      release: {
        options: {
          paths: [".static/css"],
          compress: true,
          yuicompress: true,
          optimization: 2
        },
        files: {
          // target.css file: source.less file
          "./static/css/style.css": "./src/less/style.less"
        }
      }
    },

    jade: {
      development: {
        options: {
          data: {
            debug: true
          },
          pretty: true
        },
        files: {
          "./static/index.html": "./src/templates/index.jade"
        }
      },
      release: {
        options: {
          data: {
            debug: false
          }
        },
        files: {
          "./static/index.html": "./src/templates/index.jade"
        }
      }
    },

    watch: {
      styles: {
        // Which files to watch (all .less files recursively in the less directory)
        files: ['./src/less//**/*.less', './src/templates//**/*.jade'],
        tasks: ['less:development', 'jade:development'],
        options: {
          nospawn: true
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jade');

  grunt.registerTask('default', ['watch']);

};