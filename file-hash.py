import hashlib

def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        print(f"SHA-256 Hash: {sha256.hexdigest()}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

file_path = input("Enter the file path to hash: ")
hash_file(file_path)
