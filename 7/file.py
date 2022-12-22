
from filesystem_item import FilesystemItem

class File(FilesystemItem):
    def __init__(self, name, size) -> None:
        super().__init__(name)
        self.size = size
