# An object which controls the environment seen in a with statement
# by defining __enter__() and __exit__() methods.

def main():
    with open('books.txt', 'w') as my_file:
        my_file.write("If Tomorrow Comes")

if __name__ == "__main__":
    main()

# since the open() function is paired with a with statement 
# the function will create a context manager


# Class Based Context Manager
import sqlite3
class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"an error occurred: {exc_val}")

        self.connection.close()

# Generator Based Context Manager
from contextlib import contextmanager

@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f"an error occured: {e}")
    finally:
        connection.close()