# -*- coding: utf-8 -*-
from omg.utils.dget import dget


def _col_attacher(res):
    return dget(res, ["res", "spec", "attacher"], "")

def _col_pv(res):
    source = dget(res, ["res", "spec", "source"], "")
    if source:
       return source["persistentVolumeName"]

def _col_node(res):
    return dget(res, ["res", "spec", "nodeName"], "")

def _col_attached(res):
    return dget(res, ["res", "status", "attached"], "")
# Default columns (without -o wide)
# NAME and AGE cols, if present, with None value,
# will be handled by build_table function that will
# fill them with the common name/age column functions
DEFAULT_COLUMNS = {
    "NAME": None,
    "ATTACHER": _col_attacher,
    "PV": _col_pv,
    "NODE": _col_node,
    "ATTACHED": _col_attached,
    "AGE": None,
}

# Wide columns (with -o wide)
# In addition to the default columns
WIDE_COLUMNS = {
}
