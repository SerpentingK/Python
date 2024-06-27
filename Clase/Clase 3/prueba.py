import tkinter as tk
import random

class Simulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Poblaciones")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.rabbit_population = 100
        self.fox_population = 20

        self.rabbit_birth_rate = 0.1
        self.fox_birth_rate = 0.05
        self.fox_death_rate = 0.1
        self.rabbit_growth_rate = 0.2

        self.rabbit_speed = 3
        self.fox_speed = 5

        self.draw_population()

    def draw_population(self):
        self.canvas.delete("all")

        # Reproducción de conejos
        new_rabbits = int(self.rabbit_population * self.rabbit_birth_rate)
        self.rabbit_population += new_rabbits

        # Alimentación y muerte de zorros
        rabbit_eaten = min(self.rabbit_population, self.fox_population) * 0.2
        self.rabbit_population -= rabbit_eaten
        fox_starved = int(self.fox_population * self.fox_death_rate)
        self.fox_population -= fox_starved

        # Reproducción de zorros
        if self.rabbit_population > 10:
            new_foxes = int(self.fox_population * self.fox_birth_rate)
            self.fox_population += new_foxes

        # Limitar poblaciones a valores positivos
        self.rabbit_population = max(self.rabbit_population, 0)
        self.fox_population = max(self.fox_population, 0)

        # Dibujar poblaciones
        rabbit_x = 50
        fox_x = 50
        for _ in range(int(self.rabbit_population)):
            self.canvas.create_rectangle(rabbit_x, 350, rabbit_x + 2, 400, fill="gray")
            rabbit_x += 3
        for _ in range(int(self.fox_population)):
            self.canvas.create_rectangle(fox_x, 250, fox_x + 2, 300, fill="red")
            fox_x += 3

        # Interacciones entre zorros y conejos
        for _ in range(int(self.rabbit_population)):
            rabbit_x = random.randint(0, 800)
            rabbit_y = random.randint(0, 400)
            for _ in range(int(self.fox_population)):
                fox_x = random.randint(0, 800)
                fox_y = random.randint(0, 400)
                if abs(rabbit_x - fox_x) < 10 and abs(rabbit_y - fox_y) < 10:
                    self.rabbit_population -= 1
                    self.fox_population += 1

        # Mostrar información
        self.canvas.create_text(400, 50, text=f"Población de Conejos: {int(self.rabbit_population)}", font=("Helvetica", 16))
        self.canvas.create_text(400, 100, text=f"Población de Zorros: {int(self.fox_population)}", font=("Helvetica", 16))

        # Programar siguiente actualización
        self.root.after(1000, self.draw_population)

if __name__ == "__main__":
    root = tk.Tk()
    app = Simulation(root)
    root.mainloop()
