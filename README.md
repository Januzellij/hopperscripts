hopperscripts
-
Collection of scripts I've written for the excellent <a href="http://www.hopperapp.com">Hopper disassembler</a>.

* Parse Swift Symbol.py

Extremely useful for reversing Swift binaries. Requires Xcode to be installed. Just click on a mangled Swift symbol and run. The demangled symbol will be logged in the document window.

Ex. Click on the symbol 

```
__TFC6Annota18NoteViewController23textViewDidBeginEditingfS0_FCSo10UITextViewT_
```
and run.

```
Annota.NoteViewController.textViewDidBeginEditing (Annota.NoteViewController)(ObjectiveC.UITextView) -> ()
```
is logged in the document window.