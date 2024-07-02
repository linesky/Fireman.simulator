import tkinter as tk
import time
import threading

class FiremanSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fireman Simulator")
        self.canvas_size = 640
        self.grid_size = 16
        self.cell_size = self.canvas_size // self.grid_size

        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.yellow_circle_radius = 30
        self.red_circle_radius = 20

        self.draw_grid()
        self.draw_circles()

        self.update_circles()

    def draw_grid(self):
        for i in range(self.grid_size + 1):
            x = i * self.cell_size
            y = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.canvas_size, fill="black")
            self.canvas.create_line(0, y, self.canvas_size, y, fill="black")

    def draw_circles(self):
        center_x = self.canvas_size // 2
        center_y = self.canvas_size // 2

        self.canvas.delete("circles")
        
        self.canvas.create_oval(
            center_x - self.yellow_circle_radius,
            center_y - self.yellow_circle_radius,
            center_x + self.yellow_circle_radius,
            center_y + self.yellow_circle_radius,
            outline="yellow", fill="yellow", tags="circles"
        )

        self.canvas.create_oval(
            center_x - self.red_circle_radius,
            center_y - self.red_circle_radius,
            center_x + self.red_circle_radius,
            center_y + self.red_circle_radius,
            outline="red", fill="red", tags="circles"
        )

    def update_circles(self):
        self.yellow_circle_radius += 5
        self.red_circle_radius += 5

        self.draw_circles()
        self.after(500, self.update_circles)

if __name__ == "__main__":
    app = FiremanSimulator()
    app.mainloop()

