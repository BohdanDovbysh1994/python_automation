from os import scandir, DirEntry


def folder_walk(folder_name: str, counter: int = 1) -> str:
    folder_items = scandir(folder_name)
    folder_symbol = '/'
    extend_folder_symbol = '∟'
    folder_not_empty_symbol = '̚'
    file_symbol = '+'
    name = folder_name.split('/')
    result = f"{name[-1] if len(name) > 1 else folder_name}{folder_symbol}"

    # if folder_items:
    #     result += folder_not_empty_symbol

    for item in folder_items:

        item: DirEntry = item
        tabulation = "\t" * counter

        if item.is_dir():
            result += folder_not_empty_symbol
            counter += 1
            result += f"\n{tabulation}{extend_folder_symbol}"
            result += folder_walk(f"{folder_name}/{item.name}", counter)
            counter -= 1

        if item.is_file():
            counter += 1
            result += f"\n{tabulation}{file_symbol}{item.name}"
            counter -= 1
    return result


print(folder_walk("../../lesson_7"))
