from lib_lab import *


def test(fun, inp, out):
	z = []
	for i, q in zip(inp, out):
		a = fun(i)
		if a == q:
			z.append(False)
		else:
			z.append((True, a))
	if not all(z):
		print("clr: OK")
	else:
		for i in z:
			print(f"clr: X == `{i[1]}`: {type(i[1])}")


test(clr, [
	"  12,3 21   4 ",
	"    123,25  125 6,47 ",
	"124, 1246  ,  46 ",
	"1.24, 12.46  ,  46 ",
], [
	"12.3 21 4",
	"123.25 125 6.47",
	"124 1246 46 ",
	"1.24 12.46 46",
])

