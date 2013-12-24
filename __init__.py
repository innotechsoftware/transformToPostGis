# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShapeToPostgis
                                 A QGIS plugin
 Shape file to Postgis Table
                             -------------------
        begin                : 2013-05-24
        copyright            : (C) 2013 by Innotech
        email                : aa@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Transform to PostGIS"
def description():
    return "transform differen spatial data like GML, Esri Shapefile, ArcGIS Personal GeoDatabase, MapInfo etc. to PostgreSQL\Postgis Database with OGR Libraries"
def version():
    return "Version 1.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load ShapeToPostgis class from file ShapeToPostgis
    from transformtopostgis import TransformToPostgis
    return TransformToPostgis(iface)
