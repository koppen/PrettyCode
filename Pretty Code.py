import sublime, sublime_plugin
import os

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
    result = os.popen('pwd').read()
    return result

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

