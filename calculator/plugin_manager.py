import importlib
from pathlib import Path
from typing import List, Callable, Optional

class PluginManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.commands: List[str] = []
            cls._instance.operations: dict[str, Callable] = {}
        return cls._instance

    def load_plugins(self) -> None:
        plugins_dir = Path(__file__).parent.parent / "plugins"
        for file in plugins_dir.glob("*.py"):
            if file.name != "__init__.py":
                module_name = f"plugins.{file.stem}"
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "register"):
                        module.register(self)
                except ImportError as e:
                    print(f"Error loading plugin {module_name}: {e}")

    def register_command(self, command: str) -> None:
        self.commands.append(command)

    def get_operation(self, command: str) -> Optional[Callable]:
        return self.operations.get(command)
