import matplotlib
matplotlib.use('QtAgg')  # Use Qt backend for matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.dates  as mdates

class LineChart(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=7, height=3, dpi=100, max_points=100, time_resolution=30):
        """
        Constructor for LineChart.
        
        Parameters
        ----------
        parent : QWidget
            The parent widget for the figure canvas.
        width : float, optional
            The width of the figure in inches. Defaults to 5.
        height : float, optional
            The height of the figure in inches. Defaults to 1.
        dpi : int, optional
            The DPI of the figure. Defaults to 100.
        
        Notes
        -----
        The figure is created with the specified width and height, and the
        axes is created as a single subplot. The top and right spines are
        removed to create a clean look. The bottom margin is adjusted to
        make room for a watermark.
        """
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111) 
        super().__init__(self.fig)
        self.setParent(parent)  # Important for embedding
        
        # Set the maximum number of points to display
        self.max_points = max_points
        
        # Set the time resolution for the x-axis
        self.time_resolution = time_resolution
        
        # Initialize data
        self.x_data = []
        self.y_data = []
        
        # Remove the top and right spines (borders)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)

        self.last_point_text = None

        # Adjust the bottom margin
        self.fig.subplots_adjust(bottom=0.3)  # Example: 20% of figure height as bottom margin
        self.fig.subplots_adjust(top=0.8)  # Example: 20% of figure height as top margin
        self.fig.subplots_adjust(left=0.07)  # Example: 10% of figure width as left margin
        self.fig.subplots_adjust(right=0.97)  # Example: 10% of figure width as right margin


    def update_graph(self, x_data, y_data):
        # if x_data is list, then read the first element
        if isinstance(x_data, list):
            x_data = x_data[0]
        if isinstance(y_data, list):
            y_data = y_data[0]
        
        
        self.axes.clear()
        if len(self.x_data) > self.max_points:
            self.x_data.pop(0)
            self.y_data.pop(0)
        self.x_data.append(x_data)
        self.y_data.append(y_data)
        
        self.last_point_text = None
        self.axes.plot(self.x_data, self.y_data)

        self.axes.tick_params(axis='x', direction='in')
        self.axes.tick_params(axis='y', direction='in')

        if x_data and y_data:
            last_x = x_data
            last_y = y_data

            if self.last_point_text:
                self.last_point_text.set_position((last_x, last_y))
                self.last_point_text.set_text(f"{last_y}")
            else:
                self.last_point_text = self.axes.annotate(
                    f"{last_y}",
                    xy=(last_x, last_y),
                    xytext=(5, 5),
                    textcoords="offset points",
                )

        # set the x-axis to show every 30 seconds
        self.axes.xaxis.set_major_locator(mdates.SecondLocator(interval=self.time_resolution))
        self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        self.axes.set_xlim(auto=True)
        self.draw()