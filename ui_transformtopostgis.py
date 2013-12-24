# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_shapetopostgis.ui'
#
# Created: Fri May 24 11:01:52 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TransformToPostgis(object):
    def setupUi(self, TransformToPostgis):
        TransformToPostgis.setObjectName(_fromUtf8("TransformToPostgis"))
        TransformToPostgis.resize(400, 300)

        self.HLayout = QtGui.QVBoxLayout(TransformToPostgis)
        self.HLayout.setObjectName(_fromUtf8("HLayout"))

        self.horizontalGroupBox = QtGui.QGroupBox(TransformToPostgis)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.horizontalGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        self.label3 = QtGui.QLabel(TransformToPostgis)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.gridLayout.addWidget(self.label3, 0, 0, 1, 2)

        self.cmftyp = QtGui.QComboBox(TransformToPostgis)
        self.cmftyp.setObjectName(_fromUtf8("cmftyp"))
        self.gridLayout.addWidget(self.cmftyp, 1, 0, 1, 2)

        self.hboxlayout1 = QtGui.QHBoxLayout(TransformToPostgis)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))

        self.label1 = QtGui.QLabel(TransformToPostgis)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.hboxlayout1.addWidget(self.label1)
        
        self.txtout = QtGui.QLineEdit(TransformToPostgis)
        self.txtout.setObjectName(_fromUtf8("txtout"))
        self.hboxlayout1.addWidget(self.txtout)
        
        self.btnbrowse = QtGui.QPushButton(TransformToPostgis)
        self.btnbrowse.setObjectName(_fromUtf8("btnbrowse"))
        self.hboxlayout1.addWidget(self.btnbrowse)
        self.gridLayout.addLayout(self.hboxlayout1, 2, 0, 1, 2)
        self.HLayout.addWidget(self.horizontalGroupBox)


        self.horizontalGroupBox1 = QtGui.QGroupBox(TransformToPostgis)
        self.horizontalGroupBox1.setObjectName(_fromUtf8("horizontalGroupBox1"))
        self.gridLayout1 = QtGui.QGridLayout(self.horizontalGroupBox1)
        self.gridLayout1.setObjectName(_fromUtf8("gridLayout1"))

        self.label2 = QtGui.QLabel(TransformToPostgis)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout1.addWidget(self.label2, 3, 0, 1, 2)

        self.cmprc = QtGui.QComboBox(TransformToPostgis)
        self.cmprc.setObjectName(_fromUtf8("cmprc"))
        self.gridLayout1.addWidget(self.cmprc, 4, 0, 1, 2)

        self.label = QtGui.QLabel(TransformToPostgis)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout1.addWidget(self.label, 5, 0, 1, 2)
        
        self.DataCon = QtGui.QComboBox(TransformToPostgis)
        self.DataCon.setObjectName(_fromUtf8("DataCon"))
        self.gridLayout1.addWidget(self.DataCon, 6, 0, 1, 2)

        
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        
        self.btnok = QtGui.QPushButton(TransformToPostgis)
        self.btnok.setObjectName(_fromUtf8("btnok"))
        self.hboxlayout.addWidget(self.btnok)
        
        self.btncancel = QtGui.QPushButton(TransformToPostgis)
        self.btncancel.setObjectName(_fromUtf8("btncancel"))
        self.hboxlayout.addWidget(self.btncancel)
        self.gridLayout1.addLayout(self.hboxlayout, 7, 0, 1, 2)
        self.HLayout.addWidget(self.horizontalGroupBox1)

        QtCore.QObject.connect(self.btncancel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), TransformToPostgis.reject)
        self.retranslateUi(TransformToPostgis)
        QtCore.QMetaObject.connectSlotsByName(TransformToPostgis)

    def retranslateUi(self, TransformToPostgis):
        TransformToPostgis.setWindowTitle(QtGui.QApplication.translate("TransformToPostgis", "TransformToPostgis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TransformToPostgis", "Data Connection:", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("TransformToPostgis", "Input File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("TransformToPostgis", "Update Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("TransformToPostgis", "Input File Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnok.setText(QtGui.QApplication.translate("TransformToPostgis", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btncancel.setText(QtGui.QApplication.translate("TransformToPostgis", "CANCEL", None, QtGui.QApplication.UnicodeUTF8))
        self.btnbrowse.setText(QtGui.QApplication.translate("TransformToPostgis", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalGroupBox.setTitle(QtGui.QApplication.translate("TransformToPostgis", "Input Files", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalGroupBox1.setTitle(QtGui.QApplication.translate("TransformToPostgis", "Output", None, QtGui.QApplication.UnicodeUTF8))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TransformToPostgis = QtGui.QDialog()
    ui = Ui_TransformToPostgis()
    ui.setupUi(TransformToPostgis)
    TransformToPostgis.show()
    sys.exit(app.exec_())

