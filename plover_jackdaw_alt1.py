KEYS=tuple("4SCTWHNRIEAXZxzaournlgchtsey")
IMPLICIT_HYPHEN_KEYS=KEYS
SUFFIX_KEYS=()
NUMBER_KEY=None
NUMBERS={}
UNDO_STROKE_STENO=None


KEYMAPS = {
    'Gemini PR': {
		"4"    : "S1-",
		"S"    : "S2-",
		"C"    : "T-",
		"T"    : "K-",
		"W"    : "P-",
		"H"    : "W-",
		"N"    : "H-",
		"R"    : "R-",
		"I"    : ('#1', '#2', '#3', '#4', '#5', '#6'),
		"E"    : "A-",
		"A"    : "O-",
		"X"    : "*1",
		"Z"    : "*2",
		"x"    : "*3",
		"z"    : "*4",
		"a"    : "-E",
		"o"    : "-U",
		"u"    : ('#7', '#8', '#9', '#A', '#B', '#C'),
		"r"    : "-F",
		"n"    : "-R",
		"l"    : "-P",
		"g"    : "-B",
		"c"    : "-L",
		"h"    : "-G",
		"t"    : "-T",
		"s"    : "-S",
		"e"    : "-D",
		"y"    : "-Z",
		"no-op": ("Fn", "pwr", "res1", "res2"),
    },
}
ORTHOGRAPHY_RULES= {}
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

DICTIONARIES_ROOT = 'asset:plover_jackdaw_alt1:'
DEFAULT_DICTIONARIES = ('jackdaw_custom.json', 'jackdaw_default.py',)
