"""
Import Helper - Because sometimes files are shy.
Handles the tricky business of importing our enterprise components.
"""

import importlib.util
import os


def import_special_file(filepath, variable_name):
	"""For when regular imports aren't dramatic enough."""
	try:
		if not os.path.exists(filepath):
			return " [The space wasn't found... the file wasn't found either? Did you not download the space file? 💀] "
		
		spec = importlib.util.spec_from_file_location("special_module", filepath)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		return getattr(module, variable_name)
	except Exception:
		return " [The space wasn't found... But the file was... you just have to look beyond the visible.] "

# What are you doing here? 🤔
