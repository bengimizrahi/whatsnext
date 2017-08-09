import Tkinter as tk

LINE_HEIGHT = 50
INDENTATION_WIDTH = 70
CHECKBOX_SIZE = 17

class Row():
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.canvas = tk.Canvas(self.frame, bg="white", height=LINE_HEIGHT)
        self.canvas.create_line(INDENTATION_WIDTH, 0, INDENTATION_WIDTH,
                                LINE_HEIGHT, fill="pink", width=2)
        self.canvas.create_rectangle(INDENTATION_WIDTH/2 - CHECKBOX_SIZE/2,
                                     LINE_HEIGHT/2 - CHECKBOX_SIZE/2,
                                     INDENTATION_WIDTH/2 + CHECKBOX_SIZE/2,
                                     LINE_HEIGHT/2 + CHECKBOX_SIZE/2)
        self.canvas.bind("<Button-1>", self.on_button_1)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release_1)
        self.canvas.bind("<B1-Motion>", self.on_b1_motion)
        self.button = tk.Button(self.frame, text="M")
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.button.pack(side=tk.LEFT, fill=tk.Y)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.line = []
        self.current_line_canvas_id = None
        self.lines = []

    def __append_point__(self, evt):
        if len(self.line):
            last_point = self.line[-1]
            if last_point == (evt.x, evt.y):
                return
        self.line.append((evt.x, evt.y))

    def __draw_current_line__(self):
        if len(self.line) == 0:
            return
        elif len(self.line) == 1:
            p = self.line[0]
            if self.current_line_canvas_id:
                self.canvas.delete(self.current_line_canvas_id)
            self.current_line_canvas_id = self.canvas.create_line(p[0], p[1], p[0], p[1], width=1)
        else:
            def l(arr, p): arr.extend(p); return arr
            coords = reduce(l, self.line, [])
            self.current_line_canvas_id = self.canvas.create_line(*coords, width=2)

    def on_button_1(self, evt):
        self.__append_point__(evt)

    def on_button_release_1(self, evt):
        self.__draw_current_line__()
        self.lines.append(self.line)
        self.line = []

    def on_b1_motion(self, evt):
        self.__append_point__(evt)
        self.__draw_current_line__()

class Gui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("What's Next?")
        self.rows = [Row(self.root) for _ in range(10)]

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()