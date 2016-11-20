hopperscripts
-
Collection of scripts I've written for the excellent <a href="http://www.hopperapp.com">Hopper disassembler</a>. Scripts go in /Users/\<user>/Library/Application Support/Hopper/Scripts/.

* Parse Swift Symbol.py (Requires Xcode)

Just click on a mangled Swift symbol, run the script, and the demangled symbol will be logged in the document window. Super useful for reversing Swift binaries.

Ex. Click on the symbol 

```
__TFC6Annota18NoteViewController23textViewDidBeginEditingfS0_FCSo10UITextViewT_
```
and run.

```
Annota.NoteViewController.textViewDidBeginEditing (Annota.NoteViewController)(ObjectiveC.UITextView) -> ()
```
is logged in the document window.

Stdlib symbols such as

```
imp___stubs___TFSsa6C_ARGVGVSs20UnsafeMutablePointerGS_VSs4Int8__
```
work just fine too.

NOTE: this has been built into Hopper v4. The code will remain for users of Hopper v3.