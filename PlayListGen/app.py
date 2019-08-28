import os

mediatail = [
    '.mp4',
    '.mkv',
    '.ts',
    '.rmvb',
    '.avi',
    '.flv',
    '.mpg',
    '.mpeg',
    '.m4v',
]


def get_video_names(dir_path):
    medialist = list()
    for path, directories, files in os.walk(dir_path):
        for f in files:
            mediapath = os.path.join(path, f)
            # Check the tail if it is a media file
            tail = os.path.splitext(mediapath)[1].lower()
            if tail in mediatail:
                medialist.append(mediapath)
    # Convert abs path to relative path
    # Do not us dir_path, because "D:\\" in dir_path is "D:\"
    # so it will not work properly
    common_path = os.path.commonprefix(medialist)
    for i in range(len(medialist)):
        medialist[i] = medialist[i].replace(common_path, "")
    return medialist


def generate_content(names):
    ns = names
    counter = 0
    files = ""

    for n in ns:
        n = n.strip()
        if len(n) > 0:
            counter += 1
            files += f"File{counter}={n}\n"

            print(f"{counter} -- {n}")

    content = f"[playlist]\nNumberOfEntries={counter}\n" + files

    return content


def dump_pls(path, content):
    with open(f"{path}\\playlist.pls", mode="w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    while True:
        work_path = input("Please input the path:\n")
        media_name_list = get_video_names(work_path)
        contents = generate_content(media_name_list)
        dump_pls(work_path, contents)
        print("Generate pls successfully")

        quit_app = input("Do it again? input q to quit!\n")
        if quit_app == 'q' or quit_app == "Q":
            exit(0)
