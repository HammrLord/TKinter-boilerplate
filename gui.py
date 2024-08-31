# for classes based on tkinter gui components

class SampleGUIComponent(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.master = master

        # Declare your GUI components here