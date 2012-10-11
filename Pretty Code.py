import sublime, sublime_plugin
import os
import subprocess

class PrettifyCodeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.edit = edit

    for region in self.source_regions():
      self.prettify_region(region)

  # Replaces region with the prettified version
  def prettify_region(self, region):
    result = self.prettified_region(region)
    self.view.replace(self.edit, region, result)

  # Returns the prettified version of region
  def prettified_region(self, region):
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
    output = proc.communicate(self.view.substr(region))[0]
    return output

  def view(self):
    return self.edit.active_view()

  # Returns a region covering all text in the currently active view
  def region_with_all_text(self):
    return sublime.Region(0, self.view.size())

  # Returns the currently selected text
  def selected_regions(self):
    return self.view.sel()

  # Returns the source texts to prettify as regions
  def source_regions(self):
    def non_empty(region):
      return not region.empty()

    regions = self.selected_regions()
    non_empty_regions = filter(non_empty, regions)

    if len(non_empty_regions) == 0:
      # Nothing selected, use everything
      return [self.region_with_all_text()]
    else:
      return non_empty_regions

