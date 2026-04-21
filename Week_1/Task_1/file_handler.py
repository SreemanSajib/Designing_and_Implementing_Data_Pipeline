class FileHandler:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        return None

    def read(self) -> list[str]:
        # File line by line read
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != '':
                rows.append(row.rstrip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            # if file don't find
            return []
        return rows

    def write(self, data_rows: list[str]):
        # Data abr file  likhar jonno
        try:
            filehandle = open(self.filepath, 'w', encoding="UTF-8")
            for row in data_rows:
                filehandle.write(row + '\n')
            filehandle.close()
        except Exception as e:
            print(f"Error writing to file: {e}")