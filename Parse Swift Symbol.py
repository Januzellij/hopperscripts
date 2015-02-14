import subprocess

doc = Document.getCurrentDocument()
sym = doc.getHighlightedWord()
sym = sym.replace("imp___stubs_", "") # handles stdlib symbols
proc = subprocess.Popen(['xcrun','swift-demangle',sym],stdout=subprocess.PIPE,stderr=subprocess.PIPE) # runs xcrun swift-demangle
output, errors = proc.communicate()
if errors is not None:
	doc.log(errors)
if output is not None:
	# output is in the form: "symbol --> demangled info"
	# splits off the demangled info
	func = output.split('>', 1)[1]
	func = func.strip()
	if sym == func:
		doc.log("not a mangled Swift symbol") # the demangle command didn't recognize the input
	else:
		doc.log(func)

