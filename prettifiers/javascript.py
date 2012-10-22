from built_in import BuiltInPrettifier

class JavaScriptPrettifier(BuiltInPrettifier):
  def command_line(self):
    # Build the command to run with Popen. TODO: There must be a better way to build
    # the command other than string manipulation. It seems to be a recipe for cross-OS
    # issues.
    prettifier_command = ''
    prettifier_command += self.interpreter()
    prettifier_command += ' "' + self.prettifier_script() + '" -'
    return prettifier_command

  def interpreter(self):
    """Returns the path to the interpreter to use for this prettifier"""
    return '/usr/bin/env python'

  def prettifier_path(self):
    """Returns full path to the directory with the prettifier script"""
    return BuiltInPrettifier.prettifier_path(self, 'js-beautify')

  def prettifier_script(self):
    """Returns full path to the prettifier script"""
    return '%(path)s/python/js-beautify' % {'path': self.prettifier_path()}
