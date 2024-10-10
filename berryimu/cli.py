"""Example usage of the BerryIMU library."""

import argparse
import logging
import time

from berryimu.imu.imu import IMU

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--bus", type=int, default=1)
    args = parser.parse_args()

    imu = IMU(args.bus)
    last = time.time()

    while True:
        current = time.time()
        dt = current - last
        print(imu.step(dt))
        last = current


if __name__ == "__main__":
    # python -m berryimu.cli
    main()
