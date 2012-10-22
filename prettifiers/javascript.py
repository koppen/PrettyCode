import sublime
import os
import subprocess

class JavaScriptPrettifier:
  def run(self, source):
    pwd = os.path.join(sublime.packages_path(), 'PrettyCode')
    python_interpreter = '/usr/bin/env python'

    prettifier_path = os.path.join(pwd, 'lib', 'js-beautify')
    prettifier_script = '%(path)s/python/js-beautify' % {'path': prettifier_path}

    # Build the command to run with Popen. TODO: There must be a better way to build
    # the command other than string manipulation. It seems to be a recipe for cross-OS
    # issues.
    prettifier_command = ''
    prettifier_command += python_interpreter
    prettifier_command += ' "' + prettifier_script + '" -'

    proc = subprocess.Popen(
      prettifier_command,
      shell=True,
      stdin=subprocess.PIPE,
      stderr=subprocess.PIPE,
      stdout=subprocess.PIPE
    )
    output = proc.communicate(source.encode('utf8'))[0]
    return output

