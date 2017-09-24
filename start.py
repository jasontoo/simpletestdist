"""
Start simpletestdist
"""
import sys
import argparse
import pytest
from utils import distribute

def main():
    """
    Main function for simpletestdist
    """
    parser = argparse.ArgumentParser(description="Python Test Automation.")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False,
                        help="increase output verbosity")
    parser.add_argument("-d", "--dist", type=int, metavar="N", nargs="?", dest="distribute", default=False,
                        help="distribution mode")
    parser.add_argument("test_suite", type=str, nargs="?", default=False,
                        help="Name of Test Suite. You can execute a directory, file, \
                        or individual test case. Refer to the Pytest namving conventions \
                        for more info")
    pytest_args = []

    options = parser.parse_args()
    if options.verbose:
        pytest_args.extend(['-s', '-v'])
    if options.distribute:
        pytest_args.append('-d')
        distribute.create_docker_containers(options.distribute)
        pytest_args.extend(distribute.get_container_arguments())
    if options.test_suite:
        pytest_args.append(options.test_suite)

    res = pytest.main(pytest_args)
    if options.distribute:
        distribute.cleanup()
    sys.exit(res)

if __name__ == '__main__':
    main()
