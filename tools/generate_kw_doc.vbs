' uses rfDoc for managing keywords documentation
' Scans for keywords, generates xml doc files and then it uploads them to the default rfDoc address
' default url used is localhost:8000, should be pointing to rfDoc webpage

Dim oShell
Set oShell = WScript.CreateObject("WScript.shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' folder definitions
localAutomationFolder = oShell.Environment("PROCESS").Item("AUT_DIR")
docFolder = localAutomationFolder &"\doc"

' standard libraries
mobileLibrary = "MobileLibrary"

' generate docs for standard libraries
GenerateDocsForLocalLibrary MobileLibrary

Sub GenerateDocsForLocalLibrary(name)
	oShell.Run "%comspec% /c ""python -m robot.libdoc " &name &" " &docFolder & "\" &name &".xml""",0,True
	oShell.Run "%comspec% /c ""python -m robot.libdoc " &docFolder &"\" &name &".xml " &docFolder &"\" &name &".html""",0,True
End Sub