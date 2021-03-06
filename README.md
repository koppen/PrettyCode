# Pretty Code

Unified code prettifier/formatter/beautifer for Sublime Text 2. It works across
languages and syntaxes, giving you one easily accessible command to run to make
your code formatting shine.

## Supported languages

Pretty Code currently supports the following syntaxes:

* __JavaScript__: Via [js-beautify](https://github.com/einars/js-beautify)
* __Ruby__: Via [ruby-beautify](https://github.com/erniebrodeur/ruby-beautify)

## Using

Open the command palette (cmd-shift-p) and choose "Pretty Code: Prettify current
code".

For easier access make a keybinding:

    { "keys": ["super+ctrl+option+p"], "command": "prettify_code" }

... or whatever key combination you prefer.

## Installing

### With Git

Clone the repository in your Sublime Text 2 packages directory:

    git clone https://github.com/koppen/PrettyCode.git

The packages directory is located at:

* OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux: `~/.config/sublime-text-2/Packages/`
* Windows: `%APPDATA%/Sublime Text 2/Packages/`

### Compatibility note

Pretty Code has been developed and tested on OS X. I do not know if it works
in other environments. Pull Requests with compatibility fixes and improvements
are very welcome.
