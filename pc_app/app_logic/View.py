from app_logic.Enums import Key
from app_logic.Controller import Controller  # Remove later needed for development

class View:

    def __init__(self, controller, ui):
        self.controller = controller
        self.ui = ui
        self.init_buttons()

    # noinspection DuplicatedCode
    def init_buttons(self):
        self.ui.btn_connect.addAction(self.controller.connect_com_port())
        self.ui.actionEnable_debug.activate(self.controller.set_debug_mode())
        self.ui.btn_setcolor.addAction(self.open_color_dialog)

        self.ui.btn_f1_delete.addAction(self.controller.remove_configuration_from_key(Key.F1))
        self.ui.btn_f2_delete.addAction(self.controller.remove_configuration_from_key(Key.F2))
        self.ui.btn_f3_delete.addAction(self.controller.remove_configuration_from_key(Key.F3))
        self.ui.btn_f4_delete.addAction(self.controller.remove_configuration_from_key(Key.F4))
        self.ui.btn_f5_delete.addAction(self.controller.remove_configuration_from_key(Key.F5))
        self.ui.btn_f6_delete.addAction(self.controller.remove_configuration_from_key(Key.F6))
        self.ui.btn_f7_delete.addAction(self.controller.remove_configuration_from_key(Key.F7))
        self.ui.btn_f8_delete.addAction(self.controller.remove_configuration_from_key(Key.F8))
        self.ui.btn_f9_delete.addAction(self.controller.remove_configuration_from_key(Key.F9))
        self.ui.btn_f10_delete.addAction(self.controller.remove_configuration_from_key(Key.F10))
        self.ui.btn_f11_delete.addAction(self.controller.remove_configuration_from_key(Key.F11))
        self.ui.btn_f12_delete.addAction(self.controller.remove_configuration_from_key(Key.F12))

        self.ui.btn_f1_set.addAction(self.open_connect_dialog_for_key(Key.F1))
        self.ui.btn_f2_set.addAction(self.open_connect_dialog_for_key(Key.F2))
        self.ui.btn_f3_set.addAction(self.open_connect_dialog_for_key(Key.F3))
        self.ui.btn_f4_set.addAction(self.open_connect_dialog_for_key(Key.F4))
        self.ui.btn_f5_set.addAction(self.open_connect_dialog_for_key(Key.F5))
        self.ui.btn_f6_set.addAction(self.open_connect_dialog_for_key(Key.F6))
        self.ui.btn_f7_set.addAction(self.open_connect_dialog_for_key(Key.F7))
        self.ui.btn_f8_set.addAction(self.open_connect_dialog_for_key(Key.F8))
        self.ui.btn_f9_set.addAction(self.open_connect_dialog_for_key(Key.F9))
        self.ui.btn_f10_set.addAction(self.open_connect_dialog_for_key(Key.F10))
        self.ui.btn_f11_set.addAction(self.open_connect_dialog_for_key(Key.F11))
        self.ui.btn_f12_set.addAction(self.open_connect_dialog_for_key(Key.F12))

    def open_connect_dialog_for_key(self, key):
        meh = 0

    def open_color_dialog(self):
        meh = 0
