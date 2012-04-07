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

import gtk
import logging
logger = logging.getLogger('ureyes_lib')

from . helpers import get_builder, show_uri, get_help_uri
from . preferences import preferences

# This class is meant to be subclassed by UreyesWindow.  It provides
# common functions and some boilerplate.
class Window(gtk.Window):
    __gtype_name__ = "Window"

    # To construct a new instance of this method, the following notable 
    # methods are called in this order:
    # __new__(cls)
    # __init__(self)
    # finish_initializing(self, builder)
    # __init__(self)
    #
    # For this reason, it's recommended you leave __init__ empty and put
    # your initialization code in finish_initializing
    
    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated BaseUreyesWindow object.
        """
        builder = get_builder('UreyesWindow')
        new_object = builder.get_object("ureyes_window")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initializing should be called after parsing the UI definition
        and creating a UreyesWindow object with it in order to finish
        initializing the start of the new UreyesWindow instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self, True)
        self.PreferencesDialog = None # class
        self.preferences_dialog = None # instance
        self.AboutDialog = None # class

        preferences.connect('changed', self.on_preferences_changed)

        # Optional Launchpad integration
        # This shouldn't crash if not found as it is simply used for bug reporting.
        # See https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/Coding
        # for more information about Launchpad integration.
        try:
            import LaunchpadIntegration
            LaunchpadIntegration.add_items(self.ui.helpMenu, 1, True, True)
            LaunchpadIntegration.set_sourcepackagename('ureyes')
        except ImportError:
            pass

        # Optional application indicator support
        # Run 'quickly add indicator' to get started.
        # More information:
        #  http://owaislone.org/quickly-add-indicator/
        #  https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators
        try:
            from ureyes import indicator
            # self is passed so methods of this class can be called from indicator.py
            # Comment this next line out to disable appindicator
            self.indicator = indicator.new_application_indicator(self)
        except ImportError:
            pass

    def on_mnu_contents_activate(self, widget, data=None):
        show_uri(self, "ghelp:%s" % get_help_uri())

    def on_mnu_about_activate(self, widget, data=None):
        """Display the about box for ureyes."""
        if self.AboutDialog is not None:
            about = self.AboutDialog() # pylint: disable=E1102
            response = about.run()
            about.destroy()

    def on_mnu_preferences_activate(self, widget, data=None):
        """Display the preferences window for ureyes."""

        """ From the PyGTK Reference manual
           Say for example the preferences dialog is currently open,
           and the user chooses Preferences from the menu a second time;
           use the present() method to move the already-open dialog
           where the user can see it."""
        if self.preferences_dialog is not None:
            logger.debug('show existing preferences_dialog')
            self.preferences_dialog.present()
        elif self.PreferencesDialog is not None:
            logger.debug('create new preferences_dialog')
            self.preferences_dialog = self.PreferencesDialog() # pylint: disable=E1102
            self.preferences_dialog.connect('destroy', self.on_preferences_dialog_destroyed)
            self.preferences_dialog.show()
        # destroy command moved into dialog to allow for a help button

    def on_mnu_close_activate(self, widget, data=None):
        """Signal handler for closing the UreyesWindow."""
        self.destroy()

    def on_destroy(self, widget, data=None):
        """Called when the UreyesWindow is closed."""
        # Clean up code for saving application state should be added here.
        gtk.main_quit()

    def on_preferences_changed(self, widget, data=None):
        logger.debug('main window received preferences changed')
        for key in data:
            logger.debug('preference changed: %s = %s' % (key, preferences[key]))

    def on_preferences_dialog_destroyed(self, widget, data=None):
        '''only affects gui
        
        logically there is no difference between the user closing,
        minimising or ignoring the preferences dialog'''
        logger.debug('on_preferences_dialog_destroyed')
        # to determine whether to create or present preferences_dialog
        self.preferences_dialog = None

