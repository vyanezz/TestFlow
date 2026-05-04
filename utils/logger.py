from datetime import datetime
from utils.colors import COLORS

class Logger:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def log_api_call(self, endpoint, method=None, status="TRAFFIC"):
        if not self.enabled:
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        method_str = method.upper() if method else "ANY"
        color = COLORS.get(method_str, COLORS["ANY"])

        print(
            f"\033[90m[{timestamp}]\033[0m "
            f"\033[95m[{status}]\033[0m "
            f"{color}[{method_str}]{COLORS['RESET']} "
            f"{endpoint}"
        )

    def log_action(self, action_desc, action_type=None, status="ACTION"):
        if not self.enabled:
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        type_str = action_type.upper() if action_type else "ANY"
        color = COLORS.get(type_str, COLORS["ANY"])

        print(
            f"\033[90m[{timestamp}]\033[0m "
            f"\033[92m[{status}]\033[0m "
            f"{color}[{type_str}]{COLORS['RESET']} "
            f"{action_desc}"
        )

    def log_wait(self, message, action_type="WAIT"):
        if not self.enabled:
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        type_str = action_type.upper()
        color = COLORS.get(type_str, COLORS["ANY"])

        print(
            f"\033[90m[{timestamp}]\033[0m "
            f"\033[93m[WAIT]\033[0m "
            f"{color}[{type_str}]{COLORS['RESET']} "
            f"{message}"
        )
