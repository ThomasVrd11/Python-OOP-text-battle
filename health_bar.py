import os

os.system("")

class HealthBar:

    symbol_remaining = "█"
    symbol_lost = "░"
    barrier: str = "│"
    colors: dict = {
        "red": "\33[91m",
        "green": "\33[92m",
        "yellow": "\33[93m",
        "blue": "\33[94m",
        "purple": "\33[95m",
        "cyan": "\33[96m",
        "white": "\33[97m",
        "default": "\33[0m"
    }

    def __init__(
            self,
            entity: int,
            length: int = 20,
            is_colored: bool = True,
            color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.hp_max
        self.current_value = entity.hp
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.hp

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH {self.entity.hp}/{self.entity.hp_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
