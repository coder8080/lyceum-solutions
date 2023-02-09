from zipfile import Path
import json
from os import path


def recurse(zippath: Path):
    ans = 0
    if zippath.is_dir():
        for item in zippath.iterdir():
            ans += recurse(item)
    else:
        _, extension = path.splitext(zippath.filename)
        if extension == '.json':
            data = json.loads(zippath.read_text())
            if data['city'] == 'Москва':
                ans += 1
    return ans


print(recurse(Path('input.zip')))
