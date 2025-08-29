import yaml

def load(path: str):
	try:
		with open(path, 'r') as file:
			data = yaml.safe_load(file)

		return data
	except (FileNotFoundError):
		print(f"ERROR: No file founded in {path}.")
	except (PermissionError):
		print(f"ERROR: Permission error while accessing {path}.")

def dump(path: str, data: dict):
	try:
		with open(path, 'w') as file:
			yaml.safe_dump(data, file)
	except (FileNotFoundError):
		print(f"ERROR: No file founded in {path}.")
	except (PermissionError):
		print(f"ERROR: Permission error while accessing {path}.")