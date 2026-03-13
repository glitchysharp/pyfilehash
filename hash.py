#!/usr/bin/env python3
from hash_common import run_hash_cli


def main() -> None:
	run_hash_cli("md5",    "    MD5")
	run_hash_cli("sha1",   "  SHA-1")
	run_hash_cli("sha256", "SHA-256")
	run_hash_cli("sha384", "SHA-384")
	run_hash_cli("sha512", "SHA-512")


if __name__ == "__main__":
	main()