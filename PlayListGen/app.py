def load_list():
    with open("list.txt", mode="r", encoding="utf-8") as f:
        names = f.readlines()
    return names


def generate_content(names):
    ns = names
    counter = 0
    files = ""

    for n in ns:
        n = n.strip()
        if len(n) > 0:
            counter += 1
            files += f"File{counter}={n}\n"

    content = f"[playlist]\nNumberOfEntries={counter}\n" + files

    return content


def dump_pls(content):
    with open("playlist.pls", mode="w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    names = load_list()
    content = generate_content(names)
    dump_pls(content)
