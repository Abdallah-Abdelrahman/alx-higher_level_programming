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
        for i, line in enumerate(stdin):
            stat = line.split()
            _len = len(stat)

            if not stat[_len - 2] in stat_dict:
                # 2nd to last token is the status code
                stat_dict[stat[_len - 2]] = 0

            stat_dict[stat[_len - 2]] += 1
            stat_dict['size'] += int(stat[_len - 1])

            if not (i + 1) % 10:
                print('File size: {}'.format(stat_dict['size']))
                for k, v in sorted(stat_dict.items()):
                    if k == 'size':
                        continue
                    elif v:
                        print('{}: {}'.format(k, v))
#                    for k in stat_dict:
#                        if k != 'size':
#                            stat_dict[k] = 0
    except KeyboardInterrupt:
        print('File size: {}'.format(stat_dict['size']))
        for k, v in sorted(stat_dict.items()):
            if k == 'size':
                continue
            elif v:
                print('{}: {}'.format(k, v))
#                for k in stat_dict:
#                    if k != 'size':
#                        stat_dict[k] = 0
