import os
class DatFileLister:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    def list_dat_files(self):
        # List all files in the folder
        files = os.listdir(self.folder_path)
        # Filter out only the .dat files
        dat_files = [file[:-4] for file in files if file.endswith('.dat')]
        return dat_files
    
    def read_dat_file(self, file_name):
        # take filename as input add .dat and open it
        file_path = os.path.join(self.folder_path, f"{file_name}.dat")
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                content = file.read()
                # Remove the first line
                lines = content.split('\n')
                if lines:
                    lines = lines[1:]
                # Convert to (x, y) list
                points = [(float(line.split()[0]), float(line.split()[1])) for line in lines]
            return points
        except FileNotFoundError:
            return f"File {file_name}.dat not found."
