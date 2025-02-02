/*
 * SPDX-License-Identifier: GPL-3.0-or-later
 * SPDX-FileCopyrightText: 2006-2011, 2013, 2019 Philip Chimento <philip.chimento@gmail.com>
 */

#ifndef CONFIG_FILE_H
#define CONFIG_FILE_H

#include "config.h"

#include <glib.h>
#include <pango/pango.h>

/* Three options for editor font */
typedef enum {
	FONT_STANDARD = 0,
	FONT_MONOSPACE = 1,
	FONT_CUSTOM = 2
} I7PrefsFont;

/* Four different text size options */
typedef enum {
	FONT_SIZE_STANDARD = 0,
	FONT_SIZE_MEDIUM = 1,
	FONT_SIZE_LARGE = 2,
	FONT_SIZE_HUGE = 3
} I7PrefsFontSize;

typedef enum {
  INTERPRETER_GLULXE = 0,
  INTERPRETER_GIT = 1
} I7PrefsInterpreter;

/* Pango point sizes of text size options */
#define DEFAULT_SIZE_STANDARD 10
#define RELATIVE_SIZE_STANDARD 1.0
#define RELATIVE_SIZE_MEDIUM 1.2
#define RELATIVE_SIZE_LARGE 1.4
#define RELATIVE_SIZE_HUGE 1.8

/* Other various settings */
#define DEFAULT_TAB_WIDTH 8

/* Schemas */
#define SCHEMA_SYSTEM "org.gnome.desktop.interface"
#define SCHEMA_PREFERENCES "com.inform7.IDE.preferences"
#define SCHEMA_SKEIN "com.inform7.IDE.preferences.skein"
#define SCHEMA_STATE "com.inform7.IDE.state"

/* Keys */
#define PREFS_AUTHOR_NAME          "author-name"
#define PREFS_FONT_SET             "font-set"
#define PREFS_CUSTOM_FONT          "custom-font"
#define PREFS_FONT_SIZE            "font-size"
#define PREFS_STYLE_SCHEME         "style-scheme"
#define PREFS_TAB_WIDTH            "tab-width"
#define PREFS_TABSTOPS_PADDING     "elastic-tabstops-padding"
#define PREFS_SYNTAX_HIGHLIGHTING  "syntax-highlighting"
#define PREFS_AUTO_INDENT          "auto-indent"
#define PREFS_INDENT_WRAPPED       "indent-wrapped"
#define PREFS_INTELLIGENCE         "intelligence"
#define PREFS_AUTO_NUMBER          "auto-number"
#define PREFS_INTERPRETER          "interpreter"
#define PREFS_CLEAN_BUILD_FILES    "clean-build-files"
#define PREFS_CLEAN_INDEX_FILES    "clean-index-files"
#define PREFS_SHOW_DEBUG_LOG       "show-debug-log"

#define PREFS_STATE_SPELL_CHECK       "spell-check"
#define PREFS_STATE_SHOW_TOOLBAR      "show-toolbar"
#define PREFS_STATE_SHOW_STATUSBAR    "show-statusbar"
#define PREFS_STATE_SHOW_NOTEPAD      "show-notepad"
#define PREFS_STATE_ELASTIC_TABSTOPS  "elastic-tabstops"
#define PREFS_STATE_WINDOW_SIZE       "app-window-size"
#define PREFS_STATE_DIVIDER_POS       "divider-position"
#define PREFS_STATE_EXT_WINDOW_SIZE   "ext-window-size"
#define PREFS_STATE_NOTEPAD_POS       "notepad-position"
#define PREFS_STATE_NOTEPAD_SIZE      "notepad-size"

#define PREFS_SKEIN_HORIZONTAL_SPACING  "horizontal-spacing"
#define PREFS_SKEIN_VERTICAL_SPACING    "vertical-spacing"

#define PREFS_SYSTEM_UI_FONT        "font-name"
#define PREFS_SYSTEM_DOCUMENT_FONT  "document-font-name"
#define PREFS_SYSTEM_MONOSPACE_FONT "monospace-font-name"

extern const char *font_set_enum[], *font_size_enum[], *interpreter_enum[];

GVariant *settings_enum_set_mapping(const GValue *property_value, const GVariantType *expected_type, char **enum_values);
gboolean settings_enum_get_mapping(GValue *value, GVariant *settings_variant, char **enum_values);
void init_config_file(GSettings *prefs);

#endif
