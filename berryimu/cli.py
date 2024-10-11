"""Example usage of the BerryIMU library."""

import argparse
import logging

from berryimu import IMU, KalmanFilter

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--bus", type=int, default=1)
    parser.add_argument("--step", action="store_true")
    args = parser.parse_args()

    imu = IMU(args.bus)
    filter = KalmanFilter(imu)

    while True:
        try:
            if args.step:
                line = input("Press 'r' to reset the filter: ").strip()
                if line == "r":
                    filter.reset()
                    imu.reset()
                    logger.info("IMU and filter reset")

            angles = filter.step()
            logger.info("Angles: %s", angles)
        except Exception as e:
            logger.error("Error: %s", e)


if __name__ == "__main__":
    # python -m berryimu.cli
    main()
