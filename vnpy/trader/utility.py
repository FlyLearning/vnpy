"""
General utility functions.
"""

import shelve
from pathlib import Path

from .constant import (STATUS_NOTTRADED, STATUS_PARTTRADED, STATUS_SUBMITTING)


class Singleton(type):
    """
    Singleton metaclass, 
    
    class A:
        __metaclass__ = Singleton
        
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """"""
        if cls not in cls._instances:
            cls._instances[cls] = super(VtSingleton,
                                        cls).__call__(*args,
                                                      **kwargs)

        return cls._instances[cls]


def get_temp_path(filename: str):
    """
    Get path for temp file with filename.
    """
    home_path = Path.home()
    temp_path = home_path.joinpath('.vntrader')

    if not temp_path.exists():
        temp_path.mkdir()

    return temp_path.joinpath(filename)


def get_icon_path(file_path: str, ico_name: str):
    """
    Get path for icon file with ico name.
    """
    ui_path = Path(file_path).parent
    icon_path = ui_path.joinpath("ico", ico_name)
    return str(icon_path)


def load_setting(file_name: str):
    """
    Load setting from shelve file in temp path.
    """
    file_path = get_temp_path(file_name)
    f = shelve.open(str(file_path))
    setting = dict(f)
    f.close()
    return setting


def save_setting(file_name: str, setting: dict):
    """
    Save setting into shelve file in temp path.
    """
    file_path = get_temp_path(file_name)
    f = shelve.open(str(file_path))
    for k, v in setting.items():
        f[k] = v
    f.close()