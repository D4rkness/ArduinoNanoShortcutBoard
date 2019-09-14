class KeyCommand:

    def __init__(self, key, command_type, execution_parameter):
        self.key = key
        self.command_type = command_type
        self.execution_parameter = execution_parameter

    def get_key(self):
        return self.key

    def get_command_type(self):
        return self.command_type

    def get_execution_parameter(self):
        return self.command_type
