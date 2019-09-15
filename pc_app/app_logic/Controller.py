from app_logic.Model import Model
from app_logic.Enums import Key


class Controller:

    def __init__(self, model):
        self.model = model

    def add_key_combination_to_key(self, key, button_combination):
        meh = 0

    def add_program_path_to_key(self, key, path_to_program):
        meh = 0

    def remove_configuration_from_key(self, key):
        meh = 0

    def add_new_config(self, config_name):
        meh = 0

    def remove_config(self, config_id):
        meh = 0

    def execute_test_button_press(self, key):
        meh = 0

    def search_for_ports(self):
        self.model.get_available_comports()

    def connect_com_port(self, selected_port):
        self.model.connect_to_com_port(selected_port)
        meh = 0

    def set_color(self, color):
        meh = 0

    def trigger_debug_key(self, key):
        meh = 0

    def set_debug_mode(self):
        self.model.set_debug_mode()
