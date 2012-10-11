import sublime, sublime_plugin
import os
import subprocess

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
    output = proc.communicate(source)[0]
    return output

class PrettifyCodeCommand(sublime_plugin.TextCommand):

  # Sets up supported prettifiers, mapped by their syntax names in lowercase
  PRETTIFIERS = {
    'ruby': RubyPrettifier
  }

  def run(self, edit):
    if not self.supported_syntax(self.syntax()):
      sublime.error_message("No prettifier is defined for %s" % [self.syntax()])
      return None

    self.edit = edit

    for region in self.source_regions():
      self.prettify_region(region)

  def syntax(self):
    """Returns the lowercased syntax name used in the active view."""
    syntax = self.view.settings().get('syntax')
    language = syntax.split('/')
    return language[1].lower()

  def supported_syntax(self, syntax):
    """Returns True if syntax has an associated prettifier."""
    return PrettifyCodeCommand.PRETTIFIERS.has_key(syntax)

  def prettify_region(self, region):
    """Replaces region with the prettified version."""
    result = self.prettified_region(region)
    self.view.replace(self.edit, region, result)

  def prettified_region(self, region):
    """Returns the prettified version of region."""
    prettifier = PrettifyCodeCommand.PRETTIFIERS[self.syntax()]
    return prettifier().run(self.view.substr(region))

  def region_with_all_text(self):
    """Returns a region covering all text in the currently active view."""
    return sublime.Region(0, self.view.size())

  def selected_regions(self):
    """Returns the currently selected text."""
    return self.view.sel()

  def source_regions(self):
    """Returns the source texts to prettify as regions."""
    def non_empty(region):
      return not region.empty()

    regions = self.selected_regions()
    non_empty_regions = filter(non_empty, regions)

    if len(non_empty_regions) == 0:
      # Nothing selected, use everything
      return [self.region_with_all_text()]
    else:
      return non_empty_regions
