

button_style = ttk.Style()
button_style.configure(
    "Custom1.TButton",
    font=("Calibri", 8, "normal"),
    foreground="black" if self.os_is_windows else "white",
    background="#278ef0",
    width="11",
)
button_style.map(
    "Custom1.TButton",
    foreground=[("active", "!disabled", "black")],
    background=[("active", "!disabled", "#a9d3fa")],
)