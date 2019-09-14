from app_logic.Enums import Key
from PySide2.QtWidgets import QApplication, QMainWindow, QAction
from app_logic.Controller import Controller  # Remove later needed for development


class View:

    def __init__(self, controller, ui):
        self.controller = controller
        self.ui = ui
        self.init_buttons()

    # noinspection DuplicatedCode
    def init_buttons(self):

        # self.ui.btn_debug_f1.clicked.connect(lambda: self.fuck(2))

        self.ui.btn_connect.clicked.connect(lambda: self.controller.search_for_ports())
        self.ui.btn_setcolor.clicked.connect(lambda: self.open_color_dialog())

        self.ui.actionEnable_debug.triggered.connect(self.controller.set_debug_mode)

        self.ui.btn_f1_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F1))
        self.ui.btn_f2_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F2))
        self.ui.btn_f3_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F3))
        self.ui.btn_f4_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F4))
        self.ui.btn_f5_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F5))
        self.ui.btn_f6_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F6))
        self.ui.btn_f7_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F7))
        self.ui.btn_f8_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F8))
        self.ui.btn_f9_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F9))
        self.ui.btn_f10_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F10))
        self.ui.btn_f11_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F11))
        self.ui.btn_f12_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F12))

        self.ui.btn_f1_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F1))
        self.ui.btn_f2_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F2))
        self.ui.btn_f3_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F3))
        self.ui.btn_f4_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F4))
        self.ui.btn_f5_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F5))
        self.ui.btn_f6_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F6))
        self.ui.btn_f7_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F7))
        self.ui.btn_f8_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F8))
        self.ui.btn_f9_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F9))
        self.ui.btn_f10_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F10))
        self.ui.btn_f11_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F11))
        self.ui.btn_f12_set.clicked.connect(lambda: self.open_connect_dialog_for_key(Key.F12))

    def init_debug_buttons(self):
        self.ui.btn_debug_f1.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F1))
        self.ui.btn_debug_f2.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F2))
        self.ui.btn_debug_f3.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F3))
        self.ui.btn_debug_f4.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F4))
        self.ui.btn_debug_f5.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F5))
        self.ui.btn_debug_f6.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F6))
        self.ui.btn_debug_f7.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F7))
        self.ui.btn_debug_f8.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F8))
        self.ui.btn_debug_f9.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F9))
        self.ui.btn_debug_f10.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F10))
        self.ui.btn_debug_f11.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F11))
        self.ui.btn_debug_f12.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F12))

    def open_connect_dialog_for_key(self, key):
        meh = 0

    def open_color_dialog(self):
        meh = 0

    def add_entrys_to_spinner_bar_ports(self, port_names):
        self.ui.combobox_comport.clear()
        for port_name in port_names:
            self.ui.combobox_comport.addItem(port_name)

    def add_debug_buttons(self):
        self.ui.btn_debug_f1.setVisible(True)
        self.ui.btn_debug_f2.setVisible(True)
        self.ui.btn_debug_f3.setVisible(True)
        self.ui.btn_debug_f4.setVisible(True)
        self.ui.btn_debug_f5.setVisible(True)
        self.ui.btn_debug_f6.setVisible(True)
        self.ui.btn_debug_f7.setVisible(True)
        self.ui.btn_debug_f8.setVisible(True)
        self.ui.btn_debug_f9.setVisible(True)
        self.ui.btn_debug_f10.setVisible(True)
        self.ui.btn_debug_f11.setVisible(True)
        self.ui.btn_debug_f12.setVisible(True)

    def remove_debug_buttons(self):
        self.ui.btn_debug_f1.setVisible(False)
        self.ui.btn_debug_f2.setVisible(False)
        self.ui.btn_debug_f3.setVisible(False)
        self.ui.btn_debug_f4.setVisible(False)
        self.ui.btn_debug_f5.setVisible(False)
        self.ui.btn_debug_f6.setVisible(False)
        self.ui.btn_debug_f7.setVisible(False)
        self.ui.btn_debug_f8.setVisible(False)
        self.ui.btn_debug_f9.setVisible(False)
        self.ui.btn_debug_f10.setVisible(False)
        self.ui.btn_debug_f11.setVisible(False)
        self.ui.btn_debug_f12.setVisible(False)

    def update_debug_state(self, debug_mode):
        string_prefix = 'debug: '
        if debug_mode:
            self.ui.actionEnable_debug.setText(string_prefix + 'true')
            self.add_debug_buttons()
        else:
            self.ui.actionEnable_debug.setText(string_prefix + 'false')
            self.remove_debug_buttons()
