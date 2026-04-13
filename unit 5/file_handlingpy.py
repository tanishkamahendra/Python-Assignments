def read_file():
    filename=input("Enter the filename:")
    try:
        with open(filename,'r') as file:
            content = file.read()
            print("file content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist")
    except PermissionError:
        print("Error: you do no have permission to read the file.")
    except Exception as e:
        print(f"an unexpected error occured:{e}")
        
if __name__=="__main__":
    read_file()