def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        valid_directory = os.path.isdir(directory)

        if not valid_directory:
            return f'Error: "{directory}" is not a directory'
        
        directory_content = os.listdir(directory)
        
        if directory == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")

        for content in directory_content:
            is_directory = os.path.isdir(content)
            file_size = os.path.getsize(content)
            
            print(f"  - {content}: file_size={file_size} bytes, is_dir={is_directory}")
    except SomeError:
        return f'Error: {SomeError}'


