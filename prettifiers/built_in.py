import sublime
import os
import subprocess

class BuiltInPrettifier:
  """Generic prettifier that is distributed with PrettyCode"""

  def pipe_to_prettifier(self, text):
    """Pipes text to the prettifier command via STDIN, returning STDOUT"""

    proc = subprocess.Popen(
      self.command_line(),
      shell=True,
      stdin=subprocess.PIPE,
      stderr=subprocess.PIPE,
      stdout=subprocess.PIPE
    )

    # Pipe the source to the prettifier via STDIN
    output = proc.communicate(text)[0]
    return output

  def prettifier_path(self):
    """Full path to the directory containing prettifiers or a specific prettifier if given"""
    pwd = os.path.join(sublime.packages_path(), 'PrettyCode')
    return os.path.join(pwd, 'lib', self.prettifier_name())

  def prettifier_script(self):
    """Full path to the prettifier script"""
    return os.path.join(self.prettifier_path(), self.relative_script_path())

  def run(self, source):
    return self.pipe_to_prettifier(source.encode('utf8'))
