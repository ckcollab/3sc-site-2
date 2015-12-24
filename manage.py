#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "threestrandcode.settings.base")

    from django.core.management import execute_from_command_line

    if 'livereload' in sys.argv:
        from django.core.wsgi import get_wsgi_application
        from livereload import Server
        application = get_wsgi_application()
        server = Server(application)

        # Add your watch
        # server.watch('static/riot/**/*.tag', shell('node_modules/.bin/riot static/riot/ static/riot/compiled.js'))
        server.serve()
    else:
        execute_from_command_line(sys.argv)
