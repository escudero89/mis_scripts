# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012 Cristian Gabriel Escudero escudero89@gmail.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('ureyes')

import gtk
import logging
logger = logging.getLogger('ureyes')

from ureyes_lib import Window
from ureyes.AboutUreyesDialog import AboutUreyesDialog
from ureyes.PreferencesUreyesDialog import PreferencesUreyesDialog

import os

from ureyes_lib import eyehealth

# See ureyes_lib.Window.py for more details about how this class works
class UreyesWindow(Window):
    __gtype_name__ = "UreyesWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UreyesWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutUreyesDialog
        self.PreferencesDialog = PreferencesUreyesDialog

        # Code for other initialization actions should be added here.

        A = eyehealth.eyehealth()
        

