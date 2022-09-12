# -*- coding: utf-8 -*-
from omg.utils.dget import dget


def _col_phase(res):
    return dget(res, ["res", "status", "phase"], "")

def _col_progress(res):
    return dget(res, ["res", "status", "progress"], "")

def _col_restarts(res):
    return dget(res, ["res", "status", "restartCount"], "")
# Default columns (without -o wide)
# NAME and AGE cols, if present, with None value,
# will be handled by build_table function that will
# fill them with the common name/age column functions
DEFAULT_COLUMNS = {
    "NAME": None,
    "PHASE": _col_phase,
    "PROGRESS": _col_progress,
    "RESTARTS": _col_restarts,
    "AGE": None,
}

# Wide columns (with -o wide)
# In addition to the default columns
WIDE_COLUMNS = {
}
