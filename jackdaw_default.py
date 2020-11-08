LONGEST_KEY=1
import re
from typing import Dict, Optional, List, Sequence, cast
main_regex=re.compile("".join(f"([{component}]*)" for component in 
	"4SCTWHNR IEA XZxz aou rnlgchtsey"
	.split()))
rulesUnsorted: Sequence[Dict[str, str]]=(  # taken from "Learn Plover!" website. Might be inaccurate with respect to the original patent.
	{
		# left hand obvious
		'4': 'a',
		'S': 's',
		'C': 'c',
		'T': 't',
		'W': 'w',
		'H': 'h',
		'N': 'n',
		'R': 'r',

		# left hand required
		'CTWH': 'b',
		'CT': 'd',
		'CTH': 'f',
		'SCT': 'g',
		'TWN': 'j',
		'TWH': 'k',
		'NR': 'l',
		'WN': 'm',
		'CW': 'p',
		'TNR': 'q',
		'TN': 'v',
		'STW': 'x',
		'HN': 'y',
		'CN': 'z',

		# left hand optional
		'4SCTWH': 'abb',
		'4CHN': 'acc',
		'4CHNR': 'accl',
		'4CHR': 'accr',
		'4TWHN': 'ackn',
		'4CTW': 'add',
		'4CTN': 'adv',
		'4CTHN': 'aff',
		'4SCTHR': 'affr',
		'4SCTHN': 'aft',
		'4SCTW': 'agg',
		'4WNR': 'all',
		'4CWN': 'amm',
		'4SN': 'ann',
		'4SCWN': 'app',
		'4SCWNR': 'appl',
		'4SCWR': 'appr',
		'4SR': 'arr',
		'4SCN': 'ass',
		'4TW': 'att',
		'CTWHN': 'by',
		'CTNR': 'del',
		'CTWN': 'dem',
		'CTWR': 'der',
		'CTN': 'dev',
		'TWNR': 'jer',
		'HR': 'rh',
		'SR': 'ser',
		'STWNR': 'serv',
	},
	{
		'I': 'i',
		'IE': 'u',
		'E': 'e',
		'EA': 'o',
		'A': 'a',
	},
	cast(Dict[str, str], {}),
	{
		'a': 'a',
		'ao': 'e',
		'o': 'o',
		'ou': 'i',
		'u': 'u',
	},
	{
		# right hand obvious
		'r': 'r',
		'n': 'n',
		'l': 'l',
		'g': 'g',
		'c': 'c',
		'h': 'h',
		't': 't',
		's': 's',
		'e': 'e',
		'y': 'y',

		# right hand required (to be fair, you can type this with the left hand anyway, but it takes another stroke)
		'gc': 'b',
		'nlg': 'd',
		'gch': 'f',
		'gt': 'k',
		'ngh': 'm',
		'lc': 'p',
		'nl': 's',
		'nh': 'v',
		'lgh': 'x',
		'lh': 'z',

		# right hand optional
		'lgc': 'bl',
		'gct': 'ck',
		'rng': 'gn',
		'lgct': 'ckl',
		'ncs': 'nces',
		'nlc': 'sp',
		'ht': 'th',
		'nct': 'tion',
		'cht': 'tch',
		'vs': 'ves',
		'rnh': 'wn',
		'rlh': 'wl',
		'lhs': 'zes',
	},
)
rules: Sequence[Dict[str, str]]=tuple(
		dict(sorted(rule.items(), key=lambda x: -len(x[0])))
		for rule in rulesUnsorted
			)
 
def riffle(parts: List[str], join: str)->List[str]:
	assert parts
	result=[parts[0]]
	for x in parts[1:]:
		result.extend((join, x))
	return result

def replace(string: str, rule: Dict[str, str])->str:
	if not rule: return string  # (special case for middle)

	parts: Sequence[str]=(string,)  #even indices: raw, odd indices: replaced
	for key, value in rule.items():
		new=[]
		for index, part in enumerate(parts):
			if index&1:
				new.append(part)
			else:
				new.extend(riffle(part.split(key), value))
		parts=new

	assert not any(parts[::2]), f"{string=} {parts=}"
	return "".join(parts[1::2])

def lookup(strokes: List[str])->str:
	assert len(strokes)==1
	stroke=strokes[0]
	match=main_regex.fullmatch(stroke)
	assert match
	components=[replace(match[index+1], rule) for index, rule in enumerate(rules)]
	middle=components.pop(2) # substring of XZxz
	main="".join(components)

	if not main:
		return "{#}"

	result=main
	if middle: result="{^}"+result
	return result
