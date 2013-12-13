# -*- coding: utf-8 -*-
VPScriptMenuTitle = "List Page Names"
import AppKit


def main(windowController, *args, **kwargs):
    document = windowController.document()
    textView = windowController.textView()
    for key in document.keys():
        textView.insertText_(key)
        textView.insertText_("\n")
