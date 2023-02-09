import argparse


def format_text_block(frame_height: int, frame_width: int, ﬁle_name: str) -> str:
    try:
        result = []
        file = open(file_name, 'rt')
        current_line = ''
        kill_next = False
        while True:
            sym = file.read(1)
            if sym == '\n':
                if not kill_next:
                    result.append(current_line)
                    current_line = ''
            else:
                current_line += sym
            kill_next = False
            if len(current_line) == frame_width:
                result.append(current_line)
                kill_next = True
                current_line = ''
            if len(result) == frame_height:
                break
        ans = '\n'.join(result)
        file.close()
        del file
        return ans
    except Exception:
        return f"[Errno 2] No such file or directory: '{file_name}'"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.filename))


if __name__ == '__main__':
    main()
