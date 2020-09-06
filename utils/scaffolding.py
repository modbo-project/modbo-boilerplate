def get_folders_path(development):
    if development:
        modules_folder = "dev_modules"
        content_folder = "dev_content"
    else:
        modules_folder = "modules"
        content_folder = "content"

    return modules_folder, content_folder