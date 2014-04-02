# -*- coding: utf-8 -*-
"""
Written by @thespacedoctor November 26, 2013
"""
VPScriptSuperMenuTitle = "skeleton pages"
VPScriptMenuTitle = "update index pages"

# Set Shortcut key (optional)
VPShortcutKey = "p"
VPShortcutMask = "control"
import AppKit


def main(windowController, *args, **kwargs):
    totalOnIndexPage = 10

    document = windowController.document()
    ## PESSTO WIKI HAS ITS OWN UNIQUE INDEX PAGE
    if "pessto" in document.lastComponentOfFileName():
        return None

    ## CLEAR INDEX PAGES
    textView = windowController.textView()
    publicIndexPage = document.createNewPageWithName_("index")
    publicIndexPage = document.pageForKey_("index")
    page = document.createNewPageWithName_("private_index")
    privateIndexPage = document.pageForKey_("private_index")
    publicIndexPage.setDataAsString_("")
    privateIndexPage.setDataAsString_("")

    pagesToHide = ["$skeleton_page", ]

    publicDateCreatedDictionary = {}
    privateDateCreatedDictionary = {}
    publicIndexPageData = ""
    privateIndexPageData = ""
    for key in document.keys():
        thisPage = document.pageForKey_(key)
        pageDate = thisPage.createdDate()
        theseTags = thisPage.tagNames()

        if "$publish" not in theseTags and "$skeleton_page" not in theseTags:
            privateDateCreatedDictionary[pageDate] = key
        elif "$skeleton_page" not in theseTags:
            publicDateCreatedDictionary[pageDate] = key

    ## PRINT TO THE PUBLIC INDEX
    import collections
    opublicDateCreatedDictionary = collections.OrderedDict(
        (sorted(publicDateCreatedDictionary.items())))
    count = 0
    for k, v in opublicDateCreatedDictionary.iteritems():
        if count == totalOnIndexPage:
            break
        elif document.pageForKey_(v).uti() == "net.daringfireball.markdown":
            count += 1
            pageData = document.pageForKey_(v).dataAsAttributedString().string()
            publicIndexPageData += """\n\n%s\n\n *** """ % (pageData,)

    publicIndexPage.setDataAsString_(publicIndexPageData)

    ## PRINT TO THE PRIVATE INDEX
    oprivateDateCreatedDictionary = collections.OrderedDict(
        (sorted(privateDateCreatedDictionary.items())))
    count = 0
    for k, v in oprivateDateCreatedDictionary.iteritems():
        if count == totalOnIndexPage:
            break
        elif document.pageForKey_(v).uti() == "net.daringfireball.markdown":
            count += 1
            pageData = document.pageForKey_(v).dataAsAttributedString().string()
            privateIndexPageData += """\n\n%s\n\n *** """ % (pageData,)

    privateIndexPage.setDataAsString_(publicIndexPageData)

    ## TEST THE ARGUMENTS
    ## VARIABLES ##

    return None


# use the tab-trigger below for new function
# x-def-with-logger
