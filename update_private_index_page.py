# -*- coding: utf-8 -*-
"""
Written by @thespacedoctor November 26, 2013
"""
VPScriptSuperMenuTitle = "skeleton pages"
VPScriptMenuTitle = "update private index page"

# Set Shortcut key (optional)
VPShortcutKey = "o"
VPShortcutMask = "control"
import AppKit


def main(windowController, *args, **kwargs):
    private = True
    totalOnIndexPage = 10

    document = windowController.document()
    textView = windowController.textView()
    indexPage = document.pageForKey_("index")
    indexPage.setDataAsString_("")

    pagesToHide = ["skeleton_page", ]

    dateCreatedDictionary = {}
    indexPageData = ""
    for key in document.keys():
        thisPage = document.pageForKey_(key)
        pageDate = thisPage.createdDate()
        theseTags = thisPage.tagNames()

        if private is False and "publish" not in theseTags:
            continue
        elif "skeleton_page" not in theseTags:
            dateCreatedDictionary[pageDate] = key

    import collections
    odateCreatedDictionary = collections.OrderedDict(
        reversed(sorted(dateCreatedDictionary.items())))
    count = 0
    for k, v in odateCreatedDictionary.iteritems():
        if count == totalOnIndexPage:
            break
        elif document.pageForKey_(v).uti() == "net.daringfireball.markdown":
            count += 1
            pageData = document.pageForKey_(v).dataAsAttributedString().string()
            indexPageData += """\n\n%s\n\n *** """ % (pageData,)

    indexPage.setDataAsString_(indexPageData)

    ## TEST THE ARGUMENTS
    ## VARIABLES ##

    return None


# use the tab-trigger below for new function
# x-def-with-logger
