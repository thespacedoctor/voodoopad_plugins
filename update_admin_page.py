# -*- coding: utf-8 -*-
"""
Written by @thespacedoctor November 26, 2013
"""
VPScriptSuperMenuTitle = "skeleton pages"
VPScriptMenuTitle = "update admin page"

# Set Shortcut key (optional)
VPShortcutKey = "a"
VPShortcutMask = "control"
import AppKit


def main(windowController, *args, **kwargs):

    document = windowController.document()
    textView = windowController.textView()
    page = document.createNewPageWithName_("_admin")
    adminPage = document.pageForKey_("_admin")
    adminPage.setDataAsString_("")

    adminPageData = """
# Admin Page

## @lists

@action  
@soon  
@review  
@waiting_on  

## Pages to process

"""

    processList = []

    for key in document.keys():
        thisPage = document.pageForKey_(key)
        theseTags = thisPage.tagNames()

        if "$publish" not in theseTags and "$private" not in theseTags and "$skeleton_page" not in theseTags:
            if "alias" not in thisPage.uti() and "com.fm.url" not in thisPage.uti():
                uti = thisPage.uti()
                uuid = thisPage.uuid()
                processList.append(
                    """| %(key)s | %(uti)s | [voodoopad](x-voodoopad-item://%(uuid)s) |""" %
                    locals())

    processList = sorted(processList)
    processList.insert(0, "|:---|:---|:---|")
    processList.insert(0, "| Page Link | Kind | Voodoopad Link |")
    for page in processList:
        adminPageData = """%(adminPageData)s\n%(page)s  """ % locals()

    adminPage.setDataAsString_(adminPageData)
    document.openPageWithTitle_("_admin")

    ## TEST THE ARGUMENTS
    ## VARIABLES ##

    return None


# use the tab-trigger below for new function
# x-def-with-logger
