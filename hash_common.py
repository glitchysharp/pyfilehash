#!/usr/bin/env python3
import argparse
import hashlib
from pathlib import Path


def hash_file(path: Path, algorithm: str) -> str:
	h = hashlib.new(algorithm)
	with path.open("rb") as f:
		for chunk in iter(lambda: f.read(8192), b""):
			h.update(chunk)
	return h.hexdigest()


def run_hash_cli(algorithm: str, display_name: str) -> None:
	parser = argparse.ArgumentParser(
		description=f"Compute a file's {display_name} hash."
	)
	parser.add_argument("file", type=Path, help="Path to the file to hash")
	args = parser.parse_args()

	file_path = args.file
	if not file_path.is_file():
		parser.error(f"file not found: {file_path}")

	print(display_name + ": ", hash_file(file_path, algorithm))