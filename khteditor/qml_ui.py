from PySide.QtGui import QApplication
#from PySide.QtCore import QSettings
from PySide import QtDeclarative

import sys
#import time
#import random

from qmleditor import QmlTextEditor
from plugins.plugins_api import init_plugin_system

class KhtEditor(QApplication):
    def __init__(self):

        QApplication.__init__(self,sys.argv)
        self.setOrganizationName("Khertan Software")
        self.setOrganizationDomain("khertan.net")
        self.setApplicationName("KhtEditor")
		
        QtDeclarative.qmlRegisterType(QmlTextEditor,'net.khertan.qmlcomponents',1,0,'QmlTextEditor')

        #Initialization of the plugin system
        init_plugin_system()        
                    
#        self.view = QtDeclarative.QDeclarativeView()
#        self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
#        self.view.setSource('qml_ui.qml')

        self.view = QtDeclarative.QDeclarativeView()
        self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.view.setSource('qml/Main.qml')

        self.view2 = QtDeclarative.QDeclarativeView()
        self.view2.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.view2.setSource('qml/Main.qml')

        self.view.showFullScreen()
        self.view2.showFullScreen()

if __name__ == '__main__':
    sys.exit(KhtEditor().exec_())
