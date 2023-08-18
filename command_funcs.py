import shutil
import json
from typing import NewType

pair = NewType("pair", dict[str, str])

def add_pair_to_store(src: str, dst: str) -> None:
    pair = {"src": src, "dst": dst}
    with open("file_pairs.json", "r+") as fjs:
        content = json.load(fjs)
        content["pairs"].append(pair)
        fjs.seek(0)
        json.dump(content, fjs, indent=4)

def find_changed() -> list[pair]:
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

def refresh_pairs(pairs: list[pair]) -> None:
    for pair in pairs:
        shutil.copy(pair['src'], pair['dst'])
        
    
def clear_file_pairs_file() -> None:
    content = json.load(open("file_pairs.json"))
    for _ in content['pairs']:
        content['pairs'].pop()

    open("file_pairs.json", "w").write(json.dumps(content, indent=4))
