# -*- coding: utf-8 -*-
VPScriptSuperMenuTitle = "skeleton pages"
VPScriptMenuTitle = "update tag list pages"

# Set Shortcut key (optional)
VPShortcutKey = "t"
VPShortcutMask = "control"
import AppKit


def main(windowController, *args, **kwargs):
    document = windowController.document()
    get_tag_dictionary_from_document(
        document
    )

    # thisPage.setDataAsString_("\n")

## LAST MODIFIED : November 23, 2013
## CREATED : November 23, 2013
## AUTHOR : DRYX


def get_tag_dictionary_from_document(
    document
):
    """get tag dictionary from voopoopad document

    **Key Arguments:**
        - ``document`` -- the voopoodad docuemnt

    **Return:**
        - ``tagListDictionary`` -- a dictionary of { tag : [page1, page2, ...], }

    **Todo**
        - @review: when complete, clean get_tag_dictionary_from_document function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    publicTagListPage = document.createNewPageWithName_("tag_list")
    publicTagListPage = document.pageForKey_("tag_list")
    privateTagListPage = document.createNewPageWithName_("private_tag_list")
    privateTagListPage = document.pageForKey_("private_tag_list")
    publicTagListPage.setDataAsString_("")

    pagesToHide = ["$skeleton_page", ]
    tagsToHide = ["$publish", "$skeleton_page", ]

    publicTagDictionary = {}
    publicTagPageData = "# Tag List\n\n"
    privateTagDictionary = {}
    privateTagPageData = "# Tag List\n\n"
    for key in document.keys():
        pageData = publicTagListPage.dataAsAttributedString().string()
        thisPage = document.pageForKey_(key)
        theseTags = thisPage.tagNames()
        uti = thisPage.uti()
        if "markdown" not in uti:
            continue

        if len(theseTags) == 0:
            theseTags = ["untagged"]

        if "$publish" not in theseTags:
            for item in pagesToHide:
                if item not in theseTags:
                    for tag in theseTags:
                        if tag not in tagsToHide:
                            if tag[0] == "$":
                                tag = tag[1:]
                            if tag in privateTagDictionary:
                                privateTagDictionary[tag].append(key)
                            else:
                                privateTagDictionary[tag] = [key]
        else:
            for item in pagesToHide:
                if item not in theseTags:
                    for tag in theseTags:
                        if tag not in tagsToHide:
                            if tag[0] == "$":
                                tag = tag[1:]
                            if tag in publicTagDictionary:
                                publicTagDictionary[tag].append(key)
                            else:
                                publicTagDictionary[tag] = [key]

    import collections
    opublicTagDictionary = collections.OrderedDict(
        sorted(publicTagDictionary.items()))
    for k, v in opublicTagDictionary.iteritems():
        publicTagPageData += '\n#### <i class="icon-tag"></i> ' + \
            k + ' [' + k.replace("#", "") + ']\n\n'
        for val in v:
            publicTagPageData += "%s  \n" % (val)
    publicTagListPage.setDataAsString_(publicTagPageData)

    oprivateTagDictionary = collections.OrderedDict(
        sorted(privateTagDictionary.items()))
    for k, v in oprivateTagDictionary.iteritems():
        privateTagPageData += '\n#### <i class="icon-tag"></i> ' + \
            k + ' [' + k.replace("#", "") + ']\n\n'
        for val in v:
            privateTagPageData += "%s  \n" % (val)
    privateTagListPage.setDataAsString_(privateTagPageData)

    ## TEST THE ARGUMENTS
    ## VARIABLES ##

    return None


# use the tab-trigger below for new function
# x-def-with-logger
