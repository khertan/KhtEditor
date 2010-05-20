#!/usr/bin/env python

"""KhtEditor a source code editor by Khertan : Editor Window"""

import sys
import re
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from plugins import init_plugin_system, get_plugins_by_capability
import editor
import editor_frame

class Window(QtGui.QMainWindow):
    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self,None)
        self.parent = parent
        
        self.setupFileMenu()
        self.setupHelpMenu()
        self.setupEditor()

        self.setAttribute(QtCore.Qt.WA_Maemo5AutoOrientation, True)
        self.setCentralWidget(self.editor_frame)


    def fileSave(self):
        try:
            self.editor.save()
        except (IOError, OSError), e:
            QtGui.QMessageBox.warning(self, "KhtEditor -- Save Error",
                    "Failed to save %s: %s" % (self.fileName, e))

    def saveAsFile(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self,
                        "KhtEditor -- Save File As",
                        self.editor.fileName, "")
        if not fileName.isEmpty():
            self.editor.fileName = fileName
            self.fileSave()

#    def newFile(self):
#        w = Window(self)
#        w.show()

    def openFile(self, path=QtCore.QString()):
        filename = QtGui.QFileDialog.getOpenFileName(self,
                            "KhtEditor -- Open File")
        if not filename.isEmpty():
            self.loadFile(filename)
        return filename


    def loadFile(self, fileName):
        self.editor.fileName = fileName
        try:
            self.editor.load()
            self.setWindowTitle(QtCore.QFileInfo(self.editor.fileName).fileName())
        except (IOError, OSError), e:
            QtGui.QMessageBox.warning(self, "KhtEditor -- Load Error",
                    "Failed to load %s: %s" % (filename, e))

    def setupEditor(self):
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(12)

        self.editor = editor.Kht_Editor(self)
        self.editor.setFont(font)
        self.editor_frame = editor_frame.Frame(self.editor)
        self.setupToolBar()
        from syntax.python_highlighter import Highlighter
        self.highlighter = Highlighter(self.editor.document())

    def setupToolBar(self):
        self.toolbar = self.addToolBar('Toolbar')
        self.tb_indent = QtGui.QAction(QtGui.QIcon('icons/tb_indent.png'), 'Indent', self)
        self.tb_indent.setShortcut('Ctrl+U')
        self.connect(self.toolbar, QtCore.SIGNAL('triggered()'), self.do_indent)
        self.toolbar.addAction(self.tb_indent)
        self.tb_unindent = QtGui.QAction(QtGui.QIcon('icons/tb_unindent.png'), 'Unindent', self)
        self.tb_unindent.setShortcut('Ctrl+I')
        self.connect(self.toolbar, QtCore.SIGNAL('triggered()'), self.do_unindent)
        self.toolbar.addAction(self.tb_unindent)
        self.tb_execute = QtGui.QAction(QtGui.QIcon.fromTheme('execute'), 'Execute', self)
        self.tb_execute.setShortcut('Ctrl+E')
        self.connect(self.toolbar, QtCore.SIGNAL('triggered()'), self.do_execute)
        self.toolbar.addAction(self.tb_execute)

    def setupFileMenu(self): 
        fileMenu = QtGui.QMenu(self.tr("&File"), self)
        self.menuBar().addMenu(fileMenu)

        fileMenu.addAction(self.tr("New..."), self.parent.newFile,
                QtGui.QKeySequence(self.tr("Ctrl+N", "New")))
        fileMenu.addAction(self.tr("Open..."), self.parent.openFile,
                QtGui.QKeySequence(self.tr("Ctrl+O", "Open")))
        fileMenu.addAction(self.tr("Save As"), self.saveAsFile,
                QtGui.QKeySequence(self.tr("Ctrl+Maj+S", "Save As")))

    def setupHelpMenu(self):
        helpMenu = QtGui.QMenu(self.tr("&Help"), self)
        self.menuBar().addMenu(helpMenu)

        helpMenu.addAction(self.tr("&About"), self.do_about)
        
    def do_about(self):
        self.parent.about(self)
        
    def do_indent(self):
        print "do_indent"
    def do_unindent(self):
        print "do_unindent"
    def do_execute(self,widget,*args):
        print "execute"
    def closeEvent(self,widget,*args):
#        print 'call editor close event'
        self.editor.closeEvent()
        