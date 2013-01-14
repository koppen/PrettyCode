from built_in import BuiltInPrettifier

class JavaScriptPrettifier(BuiltInPrettifier):
  def command_line(self):
    # Build the command to run with Popen. TODO: There must be a better way to build
    # the command other than string manipulation. It seems to be a recipe for cross-OS
    # issues.
    prettifier_command = ''
    prettifier_command += self.interpreter()
    prettifier_command += ' "' + self.prettifier_script() + '"'

    if self.translate_tabs_to_spaces:
        prettifier_command += ' --indent-size=' + str(self.tab_size)
    else:
        prettifier_command += ' --indent-with-tabs'

    prettifier_command += ' -' # STDIN
    print prettifier_command

    return prettifier_command

  def interpreter(self):
    """Returns the path to the interpreter to use for this prettifier"""
    return '/usr/bin/env python'

  def prettifier_name(self):
    """The name of the prettifier project used for this Prettifier"""
    return 'js-beautify'

  def relative_script_path(self):
    """Path to the actual prettifier script, relative to the prettifier path"""
    return "python/js-beautify"
