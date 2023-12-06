#!/usr/bin/python3
"""Module reads stdin line by line and computes metrics

Attributes:
    stat_dict: dictionary that holds the code status, and the size

    Example:
        stat_dict = {'200': 1, '404': 2, '500': 3, 'size': 10}
"""

from sys import stdin


if __name__ == '__main__':
    stat_dict = {'size': 0}

    try:
        j = 0
        for i, line in enumerate(stdin):
            j = i
            stat = line.split()
            # 2nd to last token is the status code
            # last token is the `size` to accumulate
            code = stat[-2]
            size = stat[-1]

            if size.isnumeric():
                stat_dict['size'] += int(size)
            if code not in \
                    ('200', '301', '400', '401', '403', '404', '405', '500'):
                continue
            if code not in stat_dict:
                stat_dict[code] = 0

            stat_dict[code] += 1

            if not (i + 1) % 10:
                print('File size: {}'.format(stat_dict['size']))
                for k, v in sorted(stat_dict.items()):
                    if k != 'size':
                        print('{}: {}'.format(k, v))
        if (j + 1) % 10:
            print('File size: {}'.format(stat_dict['size']))
            for k, v in sorted(stat_dict.items()):
                if k != 'size':
                    print('{}: {}'.format(k, v))
    except KeyboardInterrupt:
        print('File size: {}'.format(stat_dict['size']))
        for k, v in sorted(stat_dict.items()):
            if k != 'size':
                print('{}: {}'.format(k, v))
