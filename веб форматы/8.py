import shutil
from os import path, makedirs
from datetime import datetime


def make_reserve_arc(source: str, dest: str) -> None:
    if not path.exists(dest):
        makedirs(dest)
    now: datetime = datetime.now()
    archname = f'{path.basename(source)}-{now.day}-{now.month}-{now.year}-{now.hour}-{now.minute}-{now.second}'
    shutil.make_archive(
        path.join(dest, archname), "zip", source)
