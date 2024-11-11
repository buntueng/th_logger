from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from ui_app import Ui_MainWindow
import sys

import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import QTimer
from lineChart import LineChart
import datetime

import sqlite3
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Constructor for the main window.

        Initializes the UI, creates line chart instances,
        initializes data and sets up a timer to update the graphs
        every 1000ms (1 second).

        """
        super().__init__()
        self.setupUi(self)
        
        # if database does not exist, create it
        # if run in script mode, the current path is the path of the script
        # if run in interactive mode, the current path is the path of the interpreter
        # so we need to get the path of the script
        current_path = ''
        if hasattr(sys, 'frozen'):
            current_path = os.path.dirname(sys.executable)
        else:
            current_path = os.path.dirname(os.path.realpath(__file__))
            
        self.database_path = os.path.join(current_path, 'data.db')
            
        if not os.path.exists(self.database_path):
            conn = sqlite3.connect(self.database_path)
            c = conn.cursor()
            # create table th_sensor if not exists
            # datetime, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, sensor1_status, sensor2_status, sensor3_status, sensor4_status, sensor5_status, sensor6_status
            # temperature is decimals, humidity is integers, status is integers
            c.execute('''CREATE TABLE th_sensor (datetime text, temperature1 real, temperature2 real, temperature3 real, temperature4 real, temperature5 real, temperature6 real, humidity1 int, humidity2 int, humidity3 int, humidity4 int, humidity5 int, humidity6 int, sensor1_status int, sensor2_status int, sensor3_status int, sensor4_status int, sensor5_status int, sensor6_status int)''')
            conn.commit()
            conn.close()

        # Create line chart instances
        self.temperature_chart1 = LineChart(self.TCH1_widget,max_points=50,time_resolution=10)  # Assuming 'graph_widget_1' from Designer
        layout1 = QVBoxLayout(self.TCH1_widget) 
        layout1.addWidget(self.temperature_chart1)

        self.temperature_chart2 = LineChart(self.TCH2_widget,max_points=50,time_resolution=10)  # Assuming 'graph_widget_2' from Designer
        layout2 = QVBoxLayout(self.TCH2_widget)
        layout2.addWidget(self.temperature_chart2)
        
        self.temperature_chart3 = LineChart(self.TCH3_widget,max_points=50)  # Assuming 'graph_widget_3' from Designer
        layout3 = QVBoxLayout(self.TCH3_widget)
        layout3.addWidget(self.temperature_chart3)
        
        self.temperature_chart4 = LineChart(self.TCH4_widget,max_points=10)  # Assuming 'graph_widget_4' from Designer
        layout4 = QVBoxLayout(self.TCH4_widget)
        layout4.addWidget(self.temperature_chart4)
        
        self.temperature_chart5 = LineChart(self.TCH5_widget,max_points=10)  # Assuming 'graph_widget_5' from Designer
        layout5 = QVBoxLayout(self.TCH5_widget)
        layout5.addWidget(self.temperature_chart5)
        
        self.temperature_chart6 = LineChart(self.TCH6_widget,max_points=10)  # Assuming 'graph_widget_6' from Designer
        layout6 = QVBoxLayout(self.TCH6_widget)
        layout6.addWidget(self.temperature_chart6)
        
        # humidity charts
        self.humidity_chart1 = LineChart(self.HCH1_widget,max_points=50,time_resolution=10)
        layout7 = QVBoxLayout(self.HCH1_widget)
        layout7.addWidget(self.humidity_chart1)
        
        self.humidity_chart2 = LineChart(self.HCH2_widget,max_points=50,time_resolution=10)
        layout8 = QVBoxLayout(self.HCH2_widget)
        layout8.addWidget(self.humidity_chart2)
        
        self.humidity_chart3 = LineChart(self.HCH3_widget,max_points=50)
        layout9 = QVBoxLayout(self.HCH3_widget)
        layout9.addWidget(self.humidity_chart3)
        
        self.humidity_chart4 = LineChart(self.HCH4_widget,max_points=10)
        layout10 = QVBoxLayout(self.HCH4_widget)
        layout10.addWidget(self.humidity_chart4)
        
        self.humidity_chart5 = LineChart(self.HCH5_widget,max_points=10)
        layout11 = QVBoxLayout(self.HCH5_widget)
        layout11.addWidget(self.humidity_chart5)
        
        self.humidity_chart6 = LineChart(self.HCH6_widget,max_points=10)
        layout12 = QVBoxLayout(self.HCH6_widget)
        layout12.addWidget(self.humidity_chart6)
        

        # Set up timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graphs)
        self.timer.start(10000)  # Update every 1000ms (1 second)

    def update_graphs(self):
        
        x_data = datetime.datetime.now()  # Add timestamp

        # Generate random data
        t_data1 = random.randint(0, 50)
        t_data2 = random.randint(0, 50)
        t_data3 = random.randint(0, 50)
        t_data4 = random.randint(0, 50)
        t_data5 = random.randint(0, 50)
        t_data6 = random.randint(0, 50)

        h_data1 = random.randint(0, 100)
        h_data2 = random.randint(0, 100)
        h_data3 = random.randint(0, 100)
        h_data4 = random.randint(0, 100)
        h_data5 = random.randint(0, 100)
        h_data6 = random.randint(0, 100)

        # sensor status
        sensor1_status = 1
        sensor2_status = 0
        sensor3_status = 1
        sensor4_status = 0
        sensor5_status = 1
        sensor6_status = 0

        # Update the charts
        self.temperature_chart1.update_graph(x_data, t_data1)
        self.temperature_chart2.update_graph(x_data, t_data2)
        self.temperature_chart3.update_graph(x_data, t_data3)
        self.temperature_chart4.update_graph(x_data, t_data4)
        self.temperature_chart5.update_graph(x_data, t_data5)
        self.temperature_chart6.update_graph(x_data, t_data6)
        # ... (For other graphs)
        
        self.humidity_chart1.update_graph(x_data, h_data1)
        self.humidity_chart2.update_graph(x_data, h_data2)
        self.humidity_chart3.update_graph(x_data, h_data3)
        self.humidity_chart4.update_graph(x_data, h_data4)
        self.humidity_chart5.update_graph(x_data, h_data5)
        self.humidity_chart6.update_graph(x_data, h_data6)

        # Insert data into the database
        conn = sqlite3.connect(self.database_path)
        c = conn.cursor()
        c.execute('''INSERT INTO th_sensor (datetime, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, sensor1_status, sensor2_status, sensor3_status, sensor4_status, sensor5_status, sensor6_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                  (x_data, t_data1, t_data2, t_data3, t_data4, t_data5, t_data6, h_data1, h_data2, h_data3, h_data4, h_data5, h_data6, sensor1_status, sensor2_status, sensor3_status, sensor4_status, sensor5_status, sensor6_status))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())