import subprocess

doc = Document.getCurrentDocument()
sym = doc.getHighlightedWord()
sym = sym.replace("imp___stubs_", "") # handles stdlib symbols that start with imp___stubs_
proc = subprocess.Popen(['xcrun','swift-demangle',sym],stdout=subprocess.PIPE,stderr=subprocess.PIPE) # uses the xcrun swift-demangle command in Xcode
output, errors = proc.communicate()
if errors is not None:
	doc.log(errors)
if output is not None:
	func = output.split('>', 1)[1] # output is in the form: symbol --> demangled info
	func = func.strip()
	if sym == func:
		doc.log("not a mangled Swift symbol") # the demangle command didn't find anything
	else:
		doc.log(func)

