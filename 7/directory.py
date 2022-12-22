
from __future__ import annotations
from filesystem_item import FilesystemItem
from file import File

class Directory(FilesystemItem):
    def __init__(self, name: str, parent: Directory, items: list[FilesystemItem]) -> None:
        super().__init__(name)
        self.items = items
        self.parent = parent
    
    def print_items(self) -> None:
        for item in self.items:
            print(item)

    def find_size(self) -> int: # only call this on root
        self.size = 0
        for item in self.items:
            if isinstance(item, File):
                self.size += item.size
            elif isinstance(item, Directory):
                self.size += item.find_size()
        return self.size

    def find_dir_by_name(self, name) -> Directory:
        for item in self.items:
            if item.name == name and isinstance(item, Directory):
                return item
        print("COULD NOT FIND DIRECTORY")

    def tree(self, func, depth=0) -> None:
        for item in self.items:
            if isinstance(item, File):
                func(item, depth)
            elif isinstance(item, Directory):
                func(item, depth)
                item.tree(func, depth + 1)
    
    def list(self) -> list[Directory]:
        dir_list = [self.size]
        for item in self.items:
            if isinstance(item, Directory):
                dir_list += item.list()
        return dir_list
