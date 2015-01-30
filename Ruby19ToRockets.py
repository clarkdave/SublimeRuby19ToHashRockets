import sublime, sublime_plugin, re

class Ruby19ToRocketsCommand(sublime_plugin.TextCommand):

  hash_find_re = r'([\w]+): '
  hash_repl_re = r':\1 => '

  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        s = self.view.substr(region)
        s = re.sub(self.hash_find_re, self.hash_repl_re, s)
        self.view.replace(edit, region, s)
