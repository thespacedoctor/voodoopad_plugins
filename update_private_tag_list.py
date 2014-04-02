# -*- coding: utf-8 -*-
VPScriptSuperMenuTitle = "skeleton pages"
VPScriptMenuTitle = "update private tag list page"

# Set Shortcut key (optional)
VPShortcutKey = "y"
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
    document,
    private=True
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

    tagListPage = document.pageForKey_("_tag_list")
    tagListPage.setDataAsString_("")

    pagesToHide = ["$skeleton_page", ]
    tagsToHide = ["$publish", "$skeleton_page", ]

    tagDictionary = {}
    tagPageData = "# Tag List\n\n"
    for key in document.keys():
        pageData = tagListPage.dataAsAttributedString().string()
        thisPage = document.pageForKey_(key)
        uti = thisPage.uti()
        if "markdown" not in uti:
            continue

        theseTags = thisPage.tagNames()

        if len(theseTags) == 0:
            theseTags = ["untagged"]

        if private is False and "$publish" not in theseTags:
            continue
        else:
            for item in pagesToHide:
                if item not in theseTags:
                    for tag in theseTags:
                        if tag not in tagsToHide:
                            if tag[0] == "$":
                                tag = tag[1:]
                            if tag in tagDictionary:
                                tagDictionary[tag].append(key)
                            else:
                                tagDictionary[tag] = [key]

    import collections
    otagDictionary = collections.OrderedDict(sorted(tagDictionary.items()))
    for k, v in otagDictionary.iteritems():

        tagPageData += '\n#### <i class="icon-tag"></i>  ' + \
            k + ' [' + k.replace("#", "") + ']\n\n'
        for val in v:
            tagPageData += "%s  \n" % (val)

    tagListPage.setDataAsString_(tagPageData)

    ## TEST THE ARGUMENTS
    ## VARIABLES ##

    return None


# use the tab-trigger below for new function
# x-def-with-logger
