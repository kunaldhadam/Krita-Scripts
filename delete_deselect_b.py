from krita import *

# Get the current document
doc = Krita.instance().activeDocument()
if doc is not None:
    # Get the current selection
    selection = doc.selection()

    # If there is a selection
    if selection is not None:
        # Delete the selected area (cut action)
        action = Krita.instance().action('edit_cut')
        if action is not None:
            action.trigger()

        # Deselect
        doc.setSelection(None)

    # Switch to the brush tool
    brush_action = Krita.instance().action('KritaShape/KisToolBrush')
    if brush_action is not None:
        brush_action.trigger()
