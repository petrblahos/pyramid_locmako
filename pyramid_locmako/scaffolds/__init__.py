import subprocess
import sys

from pyramid.scaffolds import PyramidTemplate

class LocmakoTemplate(PyramidTemplate):
    _template_dir = 'pyramid_locmako'
    summary = 'pyramid project with Mako and Localization'

    def post(self, command, output_dir, vars):
        print "=== POST", command, output_dir, vars
        subprocess.call([ sys.executable, "setup.py", "extract_messages" ], cwd=output_dir)
        while 1:
            lc = raw_input("Language to initialize: (enter to skip)")
            if not lc:
                break
            if 2!=len(lc) or not lc.isalpha():
                print "sorry, need 2 letters, nothing more"
                continue
            subprocess.call([ sys.executable, "setup.py", "init_catalog", "-l", lc ], cwd=output_dir)
        subprocess.call([ sys.executable, "setup.py", "update_catalog" ], cwd=output_dir)
        subprocess.call([ sys.executable, "setup.py", "compile_catalog" ], cwd=output_dir)
        return super(self.__class__, self).post(command, output_dir, vars)

    def pre(self, command, output_dir, vars):
        return super(self.__class__, self).pre(command, output_dir, vars)

    def template_dir(self):
        return super(self.__class__, self).template_dir()

    def render_template(self, content, vars, filename=None):
        return super(self.__class__, self).render_template(content, vars, filename)

