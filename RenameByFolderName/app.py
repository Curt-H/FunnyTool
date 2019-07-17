import os


def add_to_3_digit(num):
    n = num
    if n < 100:
        return '-00' + str(n)
    else:
        return '-' + str(n)


if __name__ == '__main__':
    path = input('File location:\n')
    result = os.walk(path)
    for folder, j, files in result:
        print(folder)
        for index, file in enumerate(files):
            print(index, file)

            filetype = os.path.splitext(file)[-1]
            new_fname_main = folder.split('\\')[-1]
            new_fname = new_fname_main + add_to_3_digit(index) + filetype
            new_folder = os.path.join(*folder.split('\\')[:-1])
            print(new_fname)

            old_path = os.path.join(folder, file)
            new_path = os.path.join(new_folder, new_fname)
            print(old_path)
            print(new_path)
            os.rename(old_path, new_path)

            print('*' * 20)
