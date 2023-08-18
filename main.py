import sys
import shutil
import json

def add_pair_to_store(src: str, dst: str) -> None:
    pair = {"src": src, "dst": dst}
    with open("file_pairs.json", "r+") as fjs:
        content = json.load(fjs)
        content["pairs"].append(pair)
        fjs.seek(0)
        json.dump(content, fjs, indent=4)

def find_changed() -> list:
    changed_pairs = []
    with open("file_pairs.json", "r+") as fjs:
        for pair in json.load(fjs)["pairs"]:
            import difflib

            with open(pair['src']) as src:
                src_cont = src.readlines()

            with open(pair['dst']) as dst:
                dst_cont = dst.readlines()

            if len(list(difflib.unified_diff(src_cont, dst_cont))) != 0:
                changed_pairs.append(pair)

    return changed_pairs

def refresh_pairs(pairs: list) -> None:
    for pair in pairs:
        shutil.copy(pair['src'], pair['dst'])

def main():
    argc = len(sys.argv)

    options = []
    first_file_idx = 1

    # loads options into option list
    for i in range(1, argc):
        if sys.argv[i][0] == "-":
            options.append(sys.argv[i])
            first_file_idx += 1
    
    if len(options):
        for opt in options:
            match opt:
                case "-add":
                    src = sys.argv[first_file_idx]
                    dst = sys.argv[first_file_idx + 1]
                    add_pair_to_store(src, dst)
                case "-refresh":
                    to_refresh = find_changed()
                    print("Pairs to be updated: ")
                    print(to_refresh)
                    yn = input("Do you want to refresh? y/n: ")

                    if yn.lower == "n":
                        return

                    refresh_pairs(to_refresh)

if __name__ == "__main__":
    main()
