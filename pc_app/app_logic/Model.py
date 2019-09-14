

class Model:

    def __init__(self):
        self.view = None
        self.debug_mode = False
        self.color = 0
        self.connected = False
        self.com_port = 0

    def add_view(self, view):
        self.view = view

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

    def set_active_com_port(self, key):
        meh = 0

    def set_color(self, color):
        meh = 0

    def set_debug_mode(self):
        self.debug_mode = not self.debug_mode
        if self.view is not None:
            self.view.update_debug_state(self.debug_mode)
