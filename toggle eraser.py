from krita import *

class BrushToggler:
    def __init__(self):
        self.previous_brush = None
        self.eraser_preset_name = "a) Eraser Circle"
        self.load_previous_brush()

    def load_previous_brush(self):
        try:
            with open("previous_brush.txt", "r") as f:
                self.previous_brush = f.read().strip()
        except FileNotFoundError:
            pass

    def save_previous_brush(self):
        with open("previous_brush.txt", "w") as f:
            f.write(str(self.previous_brush.name()))

    def toggle_brush(self):
        window = Krita.instance().activeWindow()
        view = window.activeView()
        if not view:
            return

        doc = Krita.instance().activeDocument()
        if not doc:
            return

        current_brush_preset = view.currentBrushPreset()
        all_presets = Krita.instance().resources('preset')

        if current_brush_preset.name() == self.eraser_preset_name:
            if self.previous_brush:
                view.setCurrentBrushPreset(all_presets[self.previous_brush])
        else:
            self.previous_brush = current_brush_preset
            self.save_previous_brush()
            print(self.previous_brush.name())
            eraser_brush = "a) Eraser Circle"
            if eraser_brush:
                view.setCurrentBrushPreset(all_presets[eraser_brush])

# Create an instance of the BrushToggler class
brush_toggler = BrushToggler()
brush_toggler.toggle_brush()
