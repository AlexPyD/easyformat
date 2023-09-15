import subprocess

def format_disk(disk_number, file_system="NTFS", label="MyVolume"):
    try:
        # Construct the diskpart script
        script = f"""
        select disk {disk_number}
        clean
        create partition primary
        format fs={file_system} quick
        assign
        label={label}
        """
        
        # Run the diskpart utility with the script
        subprocess.run(["diskpart"], input=script, text=True, check=True)
        print(f"Disk {disk_number} has been formatted with {file_system} file system and labeled as '{label}'.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error formatting disk {disk_number}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def list_disks():
    try:
        # Run the diskpart utility to list disks
        result = subprocess.run(["diskpart", "/s", "list_disks_script.txt"], text=True, capture_output=True, check=True)
        print(result.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Error listing disks: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        command = input("Enter a command (type '.help' for a list of commands): ").strip()

        if command == ".help":
            print(".format <disk_number> [<file_system> [<label>]] - Format a disk.")
            print(".list_disks - List all connected disks.")
            print(".exit - Exit the program.")
        elif command.startswith(".format"):
            parts = command.split()
            if len(parts) >= 2:
                disk_number = parts[1]
                file_system = parts[2] if len(parts) >= 3 else "NTFS"
                label = parts[3] if len(parts) >= 4 else "MyVolume"
                format_disk(disk_number, file_system, label)
            else:
                print("Usage: .format <disk_number> [<file_system> [<label>]]")
        elif command == ".list_disks":
            list_disks()
        elif command == ".exit":
            break
        else:
            print("Command not recognized. Type '.help' for a list of commands.")
