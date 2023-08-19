# plover-jackdaw-alt1
Jackdaw-similar keyboard plugin for Plover.

### Installation

Refer to https://github.com/openstenoproject/plover/wiki/Manually-Installing-Plugins.

Then, restart Plover, go to Configure → System, select "Jackdaw Alt1" system.

If you don't use either Keyboard or Gemini PR machine, you will likely see a "Keymap is invalid, behavior undefined" error. Go to "Machine" tab of "Configure" window, and configure a keymap.

I wrote this long ago, so I don't really remember how it's supposed to be used, but I think:
* the keymap is designed to be compatible with a Georgi -- that is, steno keyboard, so the layout is something like
   ```
   4 C W N (X)    |    (x) r l c t (e)
   S T H R (Z)    |    (z) n g h s (y)
      (I) E A           a o (u)
   ```
   Generally uppercase characters are on the left side, and lowercase characters are on the right side.
   The key labeled `4` is just because there are too many keys labeled `a` already.

   The Georgi has 4 `*` keys total and 3 thumb keys on each half.

   On a normal keyboard, they correspond to
   ```
   q w e r (t)    |    (y) u i o p ([)
   a s d f (g)    |    (h) j k l ; (')
      (x) c v           n m (,)
   ```
   by default.
* Because of lack of space, the suffix keys `-ing`, `-ed`, etc. are not included (and I forgot how they're supposed to be typed).
* If any of the `XZxz` keys are included in a stroke, the output word will be stitched to the previous word.

Other than that, refer to the source code...

By default, the `SKWRAEBG` or `STHREagh` stroke is used to toggle the system (English stenotype ↔ Jackdaw alt1).
You'll need to add a translation `"SKWRAEBG": "{plover:switch_system:Jackdaw alt1}"` in your normal dictionary yourself,
and install the [corresponding plugin](https://github.com/nsmarkop/plover_system_switcher).

### Theory

Based on the tutorial on [Learn Plover!](https://www.openstenoproject.org/learn-plover/jackdaw.html) site,
and the linked patent.

See `jackdaw_default.py` for the details (namely, a mapping from (key stroked) → (output)),
and `jackdaw_custom.json` for the strokes not defined by the rules.

### Utilities

* `generate-typey-type-lessons.py`: convert Python dictionary format
(can be copied from `jackdaw_default.py`) to Typey Type compatible custom lessons.

