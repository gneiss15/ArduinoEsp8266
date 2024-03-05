#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ConfirmDialog( title, text ):
    import tkinter
    from tkinter import messagebox
    rootWin = tkinter.Tk() # Create the object
    rootWin.overrideredirect( 1 ) # Avoid it appearing and then disappearing quickly
    #rootWin.iconbitmap("PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
    rootWin.withdraw() # Hide the window as we do not want to see this one
    return messagebox.askyesno( title, text, parent = rootWin )
print( ConfirmDialog( 'Question', 'Ok to do ?' ) )
"""
class Gui:
  def __init__( self ):
    try:
      import tkinter
      self.rootWin = tkinter.Tk() # Create the object
      self.rootWin.overrideredirect( 1 ) # Avoid it appearing and then disappearing quickly
      #parent.iconbitmap("PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
      self.rootWin.withdraw() # Hide the window as we do not want to see this one
      self.Askyesno = self.AskyesnoTk
    except:
      self.Askyesno = self.AskyesnoNoTk
  def AskyesnoTk( self, title, text ):
    from tkinter import messagebox
    return messagebox.askyesno( title, text, parent = self.rootWin )
  def AskyesnoNoTk( self, title, text ):
    print( "tkinter not available, Cant ask user: '%s'. No assumed!" % text )
    return False
    
print( Gui().Askyesno( 'Question', 'Ok to do ?' ) )
"""    
  
"""
import os
import sys
import platform
import argparse
import shutil
import subprocess


import pyautogui
res = pyautogui.confirm( text = "text" , title = "title", buttons = [ 'OK', 'Cancel' ] )
print( "pyautogui: %s" % res )

import tkinter
parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
#parent.iconbitmap("PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one
from tkinter import messagebox
res = messagebox.askyesno('title', 'text', parent=parent ) # Yes / No

import easygui
easygui.ynbox('text', 'title', ('Yes', 'No'))
"""

