# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShapeToPostgisDialog
                                 A QGIS plugin
 Shape file to Postgis Table
                             -------------------
        begin                : 2013-05-24
        copyright            : (C) 2013 by Innotech
        email                : info@innotechyazilim.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from qgis.core import *
from PyQt4.Qt import *
import qgis
import ogr
import os
import sys
from os.path import splitext
from os.path import basename
from os.path import dirname
from ui_transformtopostgis import Ui_TransformToPostgis
# create the dialog for zoom to point
class TransformToPostgisDialog(QtGui.QDialog):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self, iface.mainWindow())
        # Set up the user interface from Designer.
        self.ui = Ui_TransformToPostgis()
        self.ui.setupUi(self)

        settings = QSettings()
        settings.beginGroup("PostgreSQL/connections")
        self.ui.DataCon.addItems(settings.childGroups())
        settings.endGroup()

        self.ui.cmprc.addItem("Create New Table")
        self.ui.cmprc.addItem("Delete Existing Table and Create New Table")
        self.ui.cmprc.addItem("Update Existing Table")

        self.ui.cmftyp.addItem("Esri Shapefile")
        self.ui.cmftyp.addItem("MapInfo File")
        self.ui.cmftyp.addItem("GML")
        self.ui.cmftyp.addItem("ArcGIS Personal GeoDatabase")

        QtCore.QObject.connect(self.ui.btnok, QtCore.SIGNAL( "clicked()" ), self.run )
        QtCore.QObject.connect(self.ui.btnbrowse, QtCore.SIGNAL( "clicked()" ), self.OpenFileDialog )


    def run(self):

        settings = QSettings()
        mysetting = self.ui.DataCon.currentText()
        mySettings = "/PostgreSQL/connections/" + mysetting

        if self.ui.cmprc.currentText() == "Create New Table" :
            command = "ogr2ogr -progress -append -f \"PostgreSQL\" PG:\"dbname="+settings.value(mySettings+"/database").toString()+" user="+settings.value(mySettings+"/username").toString()+" password=" +settings.value(mySettings+"/password").toString()+"\" \""+str(self.ui.txtout.text())+"\""
            os.system(str(command))
        elif self.ui.cmprc.currentText() =="Delete Existing Table and Create New Table":
            command = "ogr2ogr -progress -overwrite -f \"PostgreSQL\" PG:\"dbname="+settings.value(mySettings+"/database").toString()+" user="+settings.value(mySettings+"/username").toString()+" password=" +settings.value(mySettings+"/password").toString()+"\" \""+str(self.ui.txtout.text())+"\""
            os.system(str(command))
        else:
            command = "ogr2ogr -progress -update -f \"PostgreSQL\" PG:\"dbname="+settings.value(mySettings+"/database").toString()+" user="+settings.value(mySettings+"/username").toString()+" password=" +settings.value(mySettings+"/password").toString()+"\" \""+str(self.ui.txtout.text())+"\""
            os.system(str(command))


    def OpenFileDialog(self):

        file_type = ""
        if self.ui.cmftyp.currentText() == "Esri Shapefile":
            file_type = '*.shp'
        elif self.ui.cmftyp.currentText() == "MapInfo File":
            file_type = "*.tab"
        elif self.ui.cmftyp.currentText() == "GML":
            file_type = '*.gml'
        else:
            file_type = '*.mdb *.gdb'

        settings = QtCore.QSettings()
        key = '/UI/lastShapefileDir'
        outDir = settings.value(key).toString()
        filter = 'Files ('+str(file_type)+')'
        outFilePath = QtGui.QFileDialog.getOpenFileName(self, self.tr('Select a '+str(self.ui.cmftyp.currentText())), outDir, filter)
        outFilePath = unicode(outFilePath)
        
        if outFilePath:
            root, ext = splitext(outFilePath)
            outDir = dirname(outFilePath)
            settings.setValue(key, outDir)

        self.ui.txtout.setText(QString(outFilePath))
