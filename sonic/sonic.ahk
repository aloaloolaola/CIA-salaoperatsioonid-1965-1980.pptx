#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance Force


i::
Send w
Send {enter}
return

j::
Send a
Send {enter}
return

k::
Send s
Send {enter}
return

l::
Send d
Send {enter}
return