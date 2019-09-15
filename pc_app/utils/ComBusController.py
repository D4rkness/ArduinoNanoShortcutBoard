import serial.tools.list_ports

class ComBusController:

    instance = None

    def __init__(self):
        self.baudrate = 115200
        self.ports = list()
        self.serial_connection = None

    def is_connected(self):
        if self.serial_connection is None:
            return False

        return self.serial_connection.isOpen()

    def get_all_comports(self):
        self.ports = list()
        for port in serial.tools.list_ports.comports():
            self.ports.append(port)
        return self.ports

    def translate_selection_to_port(self, selection):

        if selection >= self.ports.__sizeof__():
            return None

        return self.ports.__getitem__(selection).device

    def connect_to_port(self, port):
        self.serial_connection = serial.Serial(port, self.baudrate)

    def start_port_reading(self):
        meh = 0

    def stop_port_reading(self):
        meh = 0

    def close_connection(self):
        self.serial_connection.close()


def get_instance():
    if ComBusController.instance is None:
        ComBusController.instance = ComBusController()
    return ComBusController.instance

