import re
import sys

import TeliaChallenge

from utils import LOG


def init(path: list) -> list:
    optimized_path = TeliaChallenge.pathReduc(path)
    if optimized_path is None:
        LOG.error("Optimized Path is None. Please check input arguments!")
        return
    return TeliaChallenge.pathReduc(path)


# Data cleansing
def cleanse() -> list:
    return [x for x in re.sub(r'[\[\]]', '', re.sub(r"\s+", "", ' '.join(sys.argv[1:]))).split(",") if x.strip()]


if __name__ == '__main__':
    cleansed_data = cleanse()
    final_path = init(cleansed_data)
    if final_path is not None:
        print(final_path)
