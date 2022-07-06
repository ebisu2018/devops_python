'''

实战：模拟 ls -lah 命令解析
当对目录进行iterdir的时候，由于文件数量可能非常多，因此使用yield是好的

'''

import argparse
from pathlib import Path
import datetime

parse = argparse.ArgumentParser('ls', add_help=False)
parse.add_argument('path', nargs='?', default='.', help='dir path')
parse.add_argument('-l', dest='detail', action='store_true')
parse.add_argument('-a', '--all', action='store_true')
parse.add_argument('-h', dest='human', action='store_true')
args = parse.parse_args(['-ah'])
# Namespace(path='.', detail=False, all=True, human=True)
print(args)


def _gethuman(size):
    units = ' KMGTP'
    depth = 0
    while size > 1000 and depth < len(units) - 1:
        size //= 1000
        depth += 1
    return '{}{}'.format(size, units[depth] if depth else '')


def list_dir(path='.', all=False, detail=False, human=False):
    p = Path(path)
    for f in p.iterdir():
        if not all and f.name.startswith('.'):
            continue
        if not detail:
            yield f.name
        else:
            st = f.stat()
            import stat
            mode = stat.filemode(st.st_mode)
            size =_gethuman(st.st_size) if human else st.st_size
            mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y%M%D-%H%M%S')
            yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, mtime, f.name)


print(*list_dir(args.path, args.all, args.detail, args.human), sep='\n')

print(_gethuman(1030000))
