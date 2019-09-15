from app_logic.Enums import Key
from utils.ButtonHandler import ButtonHandler
import serial.tools.list_ports
from PySide2.QtWidgets import QApplication, QMainWindow, QAction
from app_logic.Controller import Controller  # Remove later needed for development


class View:

    def __init__(self, controller, ui):
        self.controller = controller
        self.ui = ui
        self.button_handler = ButtonHandler(self, controller)
        self.button_handler.init_all_buttons()

        self.button_handler.init_debug_buttons()
        self.button_handler.hide_debug_buttons()

    def connect_com_port(self):
        self.controller.connect_com_port(self.ui.combobox_comport.currentIndex())

    def is_connected_state(self, is_connected):
        if is_connected:
            self.ui.label_connected.setText("Connected")
            self.ui.btn_connect.setText("Disconnect")
        else:
            self.ui.label_connected.setText("Disconnected")
            self.ui.btn_connect.setText("Connect")

    def open_connect_dialog_for_key(self, key):
        meh = 0

    def open_color_dialog(self):
        meh = 0

    def add_entrys_to_spinner_bar_ports(self, port_infos):
        self.ui.combobox_comport.clear()
        for port_info in port_infos:
            self.ui.combobox_comport.addItem(port_info.device)



    def update_debug_state(self, debug_mode):
        string_prefix = 'debug: '
        if debug_mode:
            self.ui.actionEnable_debug.setText(string_prefix + 'true')
            self.button_handler.show_debug_buttons()
        else:
            self.ui.actionEnable_debug.setText(string_prefix + 'false')
            self.button_handler.hide_debug_buttons()
