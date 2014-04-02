# -*- coding: utf-8 -*-
"""
Written by @thespacedoctor January 14, 2014
"""
VPScriptSuperMenuTitle = "export"
VPScriptMenuTitle = "export voodoopad doc as pickle"

# Set Shortcut key (optional)
VPShortcutKey = "e"
VPShortcutMask = "control"
import AppKit


def main(windowController, *args, **kwargs):

    import yaml

    document = windowController.document()
    documentName = document.fileName()
    documentDict = {}
    documentDict["metadata"] = {}
    documentDict["metadata"]["documentName"] = documentName

    for key in document.keys():

        thisPage = document.pageForKey_(key)
        # skip page aliases
        if "page-alias" in thisPage.uti():
            continue

        # new dictionary for each page
        documentDict[key] = {}

        # an entry for each attribute of page
        documentDict[key]["title"] = thisPage.displayName()
        documentDict[key]["createdDate"] = str(thisPage.createdDate())
        documentDict[key]["modifiedDate"] = str(thisPage.modifiedDate())
        documentDict[key]["tagNames"] = list(thisPage.tagNames())
        documentDict[key]["uti"] = str(thisPage.uti())
        documentDict[key]["url"] = str(thisPage.url())
        documentDict[key]["uuid"] = str(thisPage.uuid())

        if "markdown" in thisPage.uti():
            documentDict[key][
                "content"] = thisPage.dataAsAttributedString().string()
        else:
            documentDict[key]["content"] = None

    for item in dir(thisPage):
        print item

    pathToWriteFile = "/Users/Dave/Library/Containers/com.flyingmeat.VoodooPad5/Data/Library/Application Support/VoodooPad/PlugIns/tmp.txt"
    try:

        writeFile = open(pathToWriteFile, 'w')
    except IOError, e:
        message = 'could not open the file %s' % (pathToWriteFile,)
        log.critical(message)
        raise IOError(message)

    writeFile.write("\n\nCAMLType()",)
    writeFile.write(
        thisPage.CAMLType())

    writeFile.write("\n\nSCTExtractTitle()",)
    writeFile.write(str(thisPage.SCTExtractTitle().encode('UTF-8')))
    writeFile.write("\n\nSCTUserInterfaceItemIdentifier()",)
    writeFile.write(str(thisPage.SCTUserInterfaceItemIdentifier()))
    writeFile.write("\n\naliasAddress()",)
    writeFile.write(str(thisPage.aliasAddress()))
    writeFile.write("\n\naliasDisplayNames()",)
    writeFile.write(str(thisPage.aliasDisplayNames()))
    writeFile.write("\n\naliases()",)
    writeFile.write(str(thisPage.aliases()))
    writeFile.write("\n\nallPropertyKeys()",)
    writeFile.write(str(thisPage.allPropertyKeys()))
    writeFile.write("\n\nallowsWeakReference()",)
    writeFile.write(str(thisPage.allowsWeakReference()))
    writeFile.write("\n\nappleScriptCategoryNames()",)
    writeFile.write(str(thisPage.appleScriptCategoryNames()))
    writeFile.write("\n\nattributeKeys()",)
    writeFile.write(str(thisPage.attributeKeys()))
    writeFile.write("\n\nattributes()",)
    writeFile.write(str(thisPage.attributes()))
    writeFile.write("\n\nattributesForSaving()",)
    writeFile.write(str(thisPage.attributesForSaving()))
    writeFile.write("\n\nautoContentAccessingProxy()",)
    writeFile.write(str(thisPage.autoContentAccessingProxy()))

    writeFile.write("\n\nawakeFromNib()",)
    writeFile.write(str(thisPage.awakeFromNib()))
    writeFile.write("\n\ncachedData()",)
    writeFile.write(str(thisPage.cachedData()))
    writeFile.write("\n\ncategories()",)
    writeFile.write(str(thisPage.categories()))

    writeFile.write("\n\nclassCode()",)
    writeFile.write(str(thisPage.classCode()))
    writeFile.write("\n\nclassDescription()",)
    writeFile.write(str(thisPage.classDescription()))
    writeFile.write("\n\nclassForArchiver()",)
    writeFile.write(str(thisPage.classForArchiver()))
    writeFile.write("\n\nclassForCoder()",)
    writeFile.write(str(thisPage.classForCoder()))
    writeFile.write("\n\nclassForKeyedArchiver()",)
    writeFile.write(str(thisPage.classForKeyedArchiver()))
    writeFile.write("\n\nclassForPortCoder()",)
    writeFile.write(str(thisPage.classForPortCoder()))

    writeFile.write("\n\nclassName()",)
    writeFile.write(str(thisPage.className()))
    writeFile.write("\n\nclearDataConflict()",)
    writeFile.write(str(thisPage.clearDataConflict()))
    writeFile.write("\n\nclearProperties()",)
    writeFile.write(str(thisPage.clearProperties()))
    writeFile.write("\n\ncontainedByKeyName()",)
    writeFile.write(str(thisPage.containedByKeyName()))
    writeFile.write("\n\ncopyMainThreadProxy()",)
    writeFile.write(str(thisPage.copyMainThreadProxy()))
    writeFile.write("\n\ncreatedDate()",)
    writeFile.write(str(thisPage.createdDate()))

    writeFile.write("\n\ndata()",)
    writeFile.write(str(thisPage.data()))
    # writeFile.write("\n\ndataAsAttributedString()",)
    # writeFile.write(str(thisPage.dataAsAttributedString().encode('UTF-8')))

    writeFile.write("\n\ndataAsFileAliasURL()",)
    writeFile.write(str(thisPage.dataAsFileAliasURL()))
    writeFile.write("\n\ndataConflictKey()",)
    writeFile.write(str(thisPage.dataConflictKey()))

    writeFile.write("\n\ndataHash()",)
    writeFile.write(str(thisPage.dataHash().encode('UTF-8')))
    # writeFile.write("\n\ndealloc()",)
    # writeFile.write(thisPage.dealloc())

    writeFile.write("\n\ndescription()",)
    writeFile.write(str(thisPage.description().encode('UTF-8')))
    writeFile.write("\n\ndescriptionNoPasswords()",)
    writeFile.write(str(thisPage.descriptionNoPasswords().encode('UTF-8')))
    writeFile.write("\n\ndictionaryRepresentation()",)
    writeFile.write(str(thisPage.dictionaryRepresentation()))
    writeFile.write("\n\ndisplayForUTI()",)
    writeFile.write(str(thisPage.displayForUTI()))
    writeFile.write("\n\ndisplayName()",)
    writeFile.write(str(thisPage.displayName().encode('UTF-8')))
    writeFile.write("\n\ndoc()",)
    writeFile.write(str(thisPage.doc()))
    writeFile.write("\n\ndocument()",)
    writeFile.write(str(thisPage.document()))
    writeFile.write("\n\ndocumentBackgroundColor()",)
    writeFile.write(str(thisPage.documentBackgroundColor()))
    writeFile.write("\n\neditId()",)
    writeFile.write(str(thisPage.editId()))

    writeFile.write("\n\nencryptHint()",)
    writeFile.write(str(thisPage.encryptHint()))
    writeFile.write("\n\nencryptPass()",)
    writeFile.write(str(thisPage.encryptPass()))
    writeFile.write("\n\nencryptState()",)
    writeFile.write(str(thisPage.encryptState()))
    writeFile.write("\n\nencrypted()",)
    writeFile.write(str(thisPage.encrypted()))
    writeFile.write("\n\nentityName()",)
    writeFile.write(str(thisPage.entityName()))
    writeFile.write("\n\nexposedBindings()",)
    writeFile.write(str(thisPage.exposedBindings()))
    writeFile.write("\n\nextraData()",)
    writeFile.write(str(thisPage.extraData()))
    # writeFile.write("\n\nfinalize()",)
    # writeFile.write(str(thisPage.finalize().encode('UTF-8')))
    writeFile.write("\n\nflushKeyBindings()",)
    writeFile.write(str(thisPage.flushKeyBindings()))

    writeFile.write("\n\nhasDataConflict()",)
    writeFile.write(str(thisPage.hasDataConflict()))

    writeFile.write("\n\nhash()",)
    writeFile.write(str(thisPage.hash()))

    writeFile.write("\n\nimageSubtitle()",)
    writeFile.write(str(thisPage.imageSubtitle()))
    writeFile.write("\n\nimageTitle()",)
    writeFile.write(str(thisPage.imageTitle()))
    writeFile.write("\n\ninetURL()",)
    writeFile.write(str(thisPage.inetURL()))
    # writeFile.write("\n\ninit()",)
    # writeFile.write(thisPage.init())

    writeFile.write("\n\ninterVooodooPadPage()",)
    writeFile.write(str(thisPage.interVooodooPadPage()))
    writeFile.write("\n\nisEncrypted()",)
    writeFile.write(str(thisPage.isEncrypted()))
    writeFile.write("\n\nisFault()",)
    writeFile.write(str(thisPage.isFault()))
    writeFile.write("\n\nisFileAlias()",)
    writeFile.write(str(thisPage.isFileAlias()))
    writeFile.write("\n\nisNull()",)
    writeFile.write(str(thisPage.isNull()))
    writeFile.write("\n\nisPageAlias()",)
    writeFile.write(str(thisPage.isPageAlias()))
    writeFile.write("\n\nisPlainText()",)
    writeFile.write(str(thisPage.isPlainText()))
    writeFile.write("\n\nisProxy()",)
    writeFile.write(str(thisPage.isProxy()))
    writeFile.write("\n\nisRichText()",)
    writeFile.write(str(thisPage.isRichText()))
    writeFile.write("\n\nisText()",)
    writeFile.write(str(thisPage.isText()))
    writeFile.write("\n\nisURL()",)
    writeFile.write(str(thisPage.isURL()))
    writeFile.write("\n\nkey()",)
    writeFile.write(str(thisPage.key().encode('UTF-8')))
    writeFile.write("\n\nlastEditingComputerName()",)
    writeFile.write(str(thisPage.lastEditingComputerName()))
    writeFile.write("\n\nlastEditingUserName()",)
    writeFile.write(str(thisPage.lastEditingUserName()))
    writeFile.write("\n\nmainThreadProxy()",)
    writeFile.write(str(thisPage.mainThreadProxy()))
    writeFile.write("\n\nmainThreadProxyNoWait()",)
    writeFile.write(str(thisPage.mainThreadProxyNoWait()))
    writeFile.write("\n\nmetaValues()",)
    writeFile.write(str(thisPage.metaValues()))
    writeFile.write("\n\nmodifiedDate()",)
    writeFile.write(str(thisPage.modifiedDate()))

    writeFile.write("\n\nmy_compactDescription()",)
    writeFile.write(str(thisPage.my_compactDescription().encode('UTF-8')))
    writeFile.write("\n\nname()",)
    writeFile.write(str(thisPage.name().encode('UTF-8')))
    writeFile.write("\n\nnewXPC()",)
    writeFile.write(str(thisPage.newXPC()))
    writeFile.write("\n\nnoExport()",)
    writeFile.write(str(thisPage.noExport()))
    writeFile.write("\n\nobjectContainer()",)
    writeFile.write(str(thisPage.objectContainer()))
    # writeFile.write("\n\nobjectSpecifier()",)
    # writeFile.write(str(thisPage.objectSpecifier().encode('UTF-8')))

    writeFile.write("\n\nobservationInfo()",)
    writeFile.write(str(thisPage.observationInfo()))
    writeFile.write("\n\nojbcClass()",)
    writeFile.write(str(thisPage.ojbcClass()))
    # writeFile.write("\n\nopenFileAlias()",)
    # writeFile.write(str(thisPage.openFileAlias()))

    # writeFile.write("\n\nopenURL()",)
    # writeFile.write(str(thisPage.openURL().encode('UTF-8')))
    writeFile.write("\n\nptext()",)
    writeFile.write(str(thisPage.ptext().encode('UTF-8')))

    writeFile.write("\n\nregisterForChangeNotifications()",)
    writeFile.write(str(thisPage.registerForChangeNotifications()))
    writeFile.write("\n\nrelease()",)
    writeFile.write(str(thisPage.release()))
    # writeFile.write("\n\nretain()",)
    # writeFile.write(str(thisPage.retain().encode('UTF-8')))

    writeFile.write("\n\nretainCount()",)
    writeFile.write(str(thisPage.retainCount()))
    writeFile.write("\n\nretainWeakReference()",)
    writeFile.write(str(thisPage.retainWeakReference()))
    writeFile.write("\n\nscriptingProperties()",)
    writeFile.write(str(thisPage.scriptingProperties()))
    # writeFile.write("\n\nself()",)
    # writeFile.write(str(thisPage.self().encode('UTF-8')))

    writeFile.write("\n\nshouldColorMatch()",)
    writeFile.write(str(thisPage.shouldColorMatch()))
    writeFile.write("\n\nshouldHighlightLinks()",)
    writeFile.write(str(thisPage.shouldHighlightLinks()))
    writeFile.write("\n\nskipOnExport()",)
    writeFile.write(str(thisPage.skipOnExport()))
    writeFile.write("\n\nstore()",)
    writeFile.write(str(thisPage.store()))
    writeFile.write("\n\nstoreAttributes()",)
    writeFile.write(str(thisPage.storeAttributes()))
    writeFile.write("\n\nstringData()",)
    writeFile.write(str(thisPage.stringData().encode('UTF-8')))
    writeFile.write("\n\nsuperclass()",)
    writeFile.write(str(thisPage.superclass()))
    writeFile.write("\n\nsupportedBufferPixelFormats()",)
    writeFile.write(str(thisPage.supportedBufferPixelFormats()))
    writeFile.write("\n\nsupportedRenderedTexturePixelFormats()",)
    writeFile.write(str(thisPage.supportedRenderedTexturePixelFormats()))
    writeFile.write("\n\ntagIds()",)
    writeFile.write(str(thisPage.tagIds()))
    writeFile.write("\n\ntagNames()",)
    writeFile.write(str(thisPage.tagNames()))
    # writeFile.write("\n\ntextStorage()",)
    # writeFile.write(str(thisPage.textStorage().encode('UTF-8')))

    writeFile.write("\n\ntitle()",)
    writeFile.write(str(thisPage.title().encode('UTF-8')))
    writeFile.write("\n\ntoManyRelationship()",)
    writeFile.write(str(thisPage.toManyRelationship()))
    writeFile.write("\n\ntoManyRelationshipKeys()",)
    writeFile.write(str(thisPage.toManyRelationshipKeys()))
    writeFile.write("\n\ntoOneRelationshipKeys()",)
    writeFile.write(str(thisPage.toOneRelationshipKeys()))
    writeFile.write("\n\ntype()",)
    writeFile.write(str(thisPage.type()))
    writeFile.write("\n\nurl()",)
    writeFile.write(str(thisPage.url()))
    writeFile.write("\n\nuserInterfaceItemIdentifier()",)
    writeFile.write(str(thisPage.userInterfaceItemIdentifier()))
    writeFile.write("\n\nuti()",)
    writeFile.write(str(thisPage.uti()))
    writeFile.write("\n\nuuid()",)
    writeFile.write(str(thisPage.uuid()))
    writeFile.write("\n\nversion()",)
    writeFile.write(str(thisPage.version()))
    writeFile.write("\n\nzone()",)
    writeFile.write(str(thisPage.zone()))

    writeFile.close()

    # fileName = "/Users/Dave/Library/Containers/com.flyingmeat.VoodooPad5/Data/Library/Application Support/VoodooPad/PlugIns/tmp.yaml"
    # stream = file(fileName, 'w')
    # yamlContent = documentDict
    # yaml.dump(yamlContent, stream, default_flow_style=False)
    # stream.close()
    return None


# use the tab-trigger below for new function
# x-def-with-logger
