import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib in PySide6")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.figures = []
        self.canvases = []
        self.axes = []
        self.data = []
        self.timers = []

        # Create three matplotlib figures and canvases
        for i in range(3):
            figure = Figure(figsize=(5, 3))  # Adjust figure size as needed
            canvas = FigureCanvas(figure)
            self.layout.addWidget(canvas)
            self.figures.append(figure)
            self.canvases.append(canvas)
            self.axes.append(figure.add_subplot(111))  # Create a single subplot
            self.data.append([])

            # Initialize timers for each plot
            timer = QTimer()
            timer.timeout.connect(lambda i=i: self.update_plot(i))
            timer.start(1000)
            self.timers.append(timer)
            
        # Initialize data with 20 initial points
        for i in range(3):
            self.data[i] = [0] * 20  # Initialize with 20 zeros

            # Set initial x-axis limits for 20 points
            self.axes[i].set_xlim(0, 19)

    def update_plot(self, index):
        y = random.randint(0, 100)
        self.data[index].append(y)

        # Keep only the last 20 values
        if len(self.data[index]) > 20:
            self.data[index] = self.data[index][-20:]

        ax = self.axes[index]
        ax.clear()
        ax.plot(self.data[index], 'o-', color='blue')  # Plot with blue line and markers
        ax.set_ylim(0, 100)  # Set y-axis limits
        ax.set_xticks([])  # Remove x-axis ticks
        ax.text(len(self.data[index]) - 1, self.data[index][-1], f"{self.data[index][-1]}", 
                ha='center', va='bottom')  # Show current value

        self.canvases[index].draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())