# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os
import subprocess

# Load all the prettifier wrappers
from prettifiers import *

class PrettifyCodeCommand(sublime_plugin.TextCommand):

  # Sets up supported prettifiers, mapped by their syntax names in lowercase
  PRETTIFIERS = {
    'ruby': ruby.RubyPrettifier
  }

  def run(self, edit):
    if not self.supported_syntax(self.syntax()):
      sublime.error_message("No prettifier is defined for " + self.syntax())
      return None

    self.edit = edit

    for region in self.source_regions():
      self.prettify_region(region)

  def syntax(self):
    """Returns the syntax name used in the active view."""
    syntax = self.view.settings().get('syntax')
    language = syntax.split('/')
    return language[1]

  def supported_syntax(self, syntax):
    """Returns True if syntax has an associated prettifier."""
    return PrettifyCodeCommand.PRETTIFIERS.has_key(syntax.lower())

  def prettify_region(self, region):
    """Replaces region with the prettified version."""
    result = self.prettified_region(region)
    self.view.replace(self.edit, region, result.decode('utf8'))

  def prettified_region(self, region):
    """Returns the prettified version of region."""
    prettifier = PrettifyCodeCommand.PRETTIFIERS[self.syntax().lower()]
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
