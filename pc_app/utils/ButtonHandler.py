# class for the initialization of the buttons and other action stuff to unbloat the view
from app_logic.Enums import Key

class ButtonHandler:

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def init_debug_buttons(self):
        self.model.ui.btn_debug_f1.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F1))
        self.model.ui.btn_debug_f2.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F2))
        self.model.ui.btn_debug_f3.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F3))
        self.model.ui.btn_debug_f4.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F4))
        self.model.ui.btn_debug_f5.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F5))
        self.model.ui.btn_debug_f6.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F6))
        self.model.ui.btn_debug_f7.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F7))
        self.model.ui.btn_debug_f8.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F8))
        self.model.ui.btn_debug_f9.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F9))
        self.model.ui.btn_debug_f10.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F10))
        self.model.ui.btn_debug_f11.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F11))
        self.model.ui.btn_debug_f12.clicked.connect(lambda: self.controller.trigger_debug_key(Key.F12))

    def init_all_buttons(self):

        self.model.ui.btn_connect.clicked.connect(lambda: self.model.connect_com_port())
        self.model.ui.btn_search_ports.clicked.connect(lambda: self.controller.search_for_ports())
        self.model.ui.btn_setcolor.clicked.connect(lambda: self.model.open_color_dialog())

        self.model.ui.actionEnable_debug.triggered.connect(self.controller.set_debug_mode)

        self.model.ui.btn_f1_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F1))
        self.model.ui.btn_f2_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F2))
        self.model.ui.btn_f3_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F3))
        self.model.ui.btn_f4_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F4))
        self.model.ui.btn_f5_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F5))
        self.model.ui.btn_f6_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F6))
        self.model.ui.btn_f7_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F7))
        self.model.ui.btn_f8_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F8))
        self.model.ui.btn_f9_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F9))
        self.model.ui.btn_f10_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F10))
        self.model.ui.btn_f11_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F11))
        self.model.ui.btn_f12_delete.clicked.connect(lambda: self.controller.remove_configuration_from_key(Key.F12))

        self.model.ui.btn_f1_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F1))
        self.model.ui.btn_f2_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F2))
        self.model.ui.btn_f3_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F3))
        self.model.ui.btn_f4_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F4))
        self.model.ui.btn_f5_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F5))
        self.model.ui.btn_f6_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F6))
        self.model.ui.btn_f7_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F7))
        self.model.ui.btn_f8_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F8))
        self.model.ui.btn_f9_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F9))
        self.model.ui.btn_f10_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F10))
        self.model.ui.btn_f11_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F11))
        self.model.ui.btn_f12_set.clicked.connect(lambda: self.model.open_connect_dialog_for_key(Key.F12))

    def show_debug_buttons(self):
        self.model.ui.btn_debug_f1.setVisible(True)
        self.model.ui.btn_debug_f2.setVisible(True)
        self.model.ui.btn_debug_f3.setVisible(True)
        self.model.ui.btn_debug_f4.setVisible(True)
        self.model.ui.btn_debug_f5.setVisible(True)
        self.model.ui.btn_debug_f6.setVisible(True)
        self.model.ui.btn_debug_f7.setVisible(True)
        self.model.ui.btn_debug_f8.setVisible(True)
        self.model.ui.btn_debug_f9.setVisible(True)
        self.model.ui.btn_debug_f10.setVisible(True)
        self.model.ui.btn_debug_f11.setVisible(True)
        self.model.ui.btn_debug_f12.setVisible(True)

    def hide_debug_buttons(self):
        self.model.ui.btn_debug_f1.setVisible(False)
        self.model.ui.btn_debug_f2.setVisible(False)
        self.model.ui.btn_debug_f3.setVisible(False)
        self.model.ui.btn_debug_f4.setVisible(False)
        self.model.ui.btn_debug_f5.setVisible(False)
        self.model.ui.btn_debug_f6.setVisible(False)
        self.model.ui.btn_debug_f7.setVisible(False)
        self.model.ui.btn_debug_f8.setVisible(False)
        self.model.ui.btn_debug_f9.setVisible(False)
        self.model.ui.btn_debug_f10.setVisible(False)
        self.model.ui.btn_debug_f11.setVisible(False)
        self.model.ui.btn_debug_f12.setVisible(False)