class RubyPrettifier:
  def run(self, source):
    pwd = os.path.join(sublime.packages_path(), 'PrettyCode')
    ruby_interpreter = '/usr/bin/env ruby'

    prettifier_path = os.path.join(pwd, 'lib', 'ruby-beautify')
    prettifier_script = '%(path)s/bin/rbeautify' % {'path': prettifier_path}

    # Build the command to run with Popen. TODO: There must be a better way to build
    # the command other than string manipulation. It seems to be a recipe for cross-OS
    # issues.
    prettifier_command = ''
    prettifier_command += ruby_interpreter
    prettifier_command += ' -I "' + prettifier_path + '/lib' + '"'
    prettifier_command += ' "' + prettifier_script + '"'

    proc = subprocess.Popen(
      prettifier_command,
      shell=True,
      stdin=subprocess.PIPE,
      stderr=subprocess.PIPE,
      stdout=subprocess.PIPE
    )
    output = proc.communicate(source.encode('utf8'))[0]
    return output

