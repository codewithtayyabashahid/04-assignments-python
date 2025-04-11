import tkinter as tk

class EraserCanvas:
    def __init__(self, root, rows=10, cols=10, cell_size=40):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        
        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()
        
        self.cells = []
        for r in range(rows):
            row = []
            for c in range(cols):
                x1, y1 = c * cell_size, r * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row.append(rect)
            self.cells.append(row)
        
        self.eraser = self.canvas.create_rectangle(0, 0, cell_size, cell_size, fill="gray", outline="black")
        self.canvas.bind("<B1-Motion>", self.erase)
    
    def erase(self, event):
        self.canvas.coords(self.eraser, event.x - self.cell_size // 2, event.y - self.cell_size // 2,
                           event.x + self.cell_size // 2, event.y + self.cell_size // 2)
        
        for row in self.cells:
            for rect in row:
                x1, y1, x2, y2 = self.canvas.coords(rect)
                eraser_x1, eraser_y1, eraser_x2, eraser_y2 = self.canvas.coords(self.eraser)
                
                if not (x2 < eraser_x1 or x1 > eraser_x2 or y2 < eraser_y1 or y1 > eraser_y2):
                    self.canvas.itemconfig(rect, fill="white")

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    EraserCanvas(root)
    root.mainloop()

if __name__ == '__main__':
    main()
