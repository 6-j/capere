import argparse
import time

import requests

from capere.utils import (
    format_batch_results,
    read_usernames_from_file,
    write_results_to_file,
    validate_username,
    show_progress,
)


def scrape_usernames(usernames):
    results = {}
    total_usernames = len(usernames)
    for index, username in enumerate(usernames, start=1):
        if not validate_username(username):
            print(f"Skipping invalid username: {username}")
            continue
        url = f"https://github.com/{username}"
        response = requests.get(url)
        if response.status_code == 404:
            results[username] = True
        elif response.status_code == 200:
            results[username] = False
        else:
            raise Exception(f"Unexpected status code for {username}: {response.status_code}")
        show_progress(index, total_usernames)
        time.sleep(1)
    return results


def main():
    parser = argparse.ArgumentParser(description="Check the availability of GitHub usernames.")
    parser.add_argument(
        "usernames",
        nargs="*",
        help="One or more GitHub usernames to check.",
    )
    parser.add_argument(
        "--file",
        "-f",
        help="Path to a file containing a list of usernames (one per line).",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to a file where results will be saved.",
    )
    parser.add_argument(
        "--color",
        "-c",
        action="store_true",
        help="Enable colored output.",
    )
    args = parser.parse_args()

    if args.file:
        usernames = read_usernames_from_file(args.file)
    else:
        usernames = args.usernames

    if not usernames:
        print("No usernames provided. Use --file or provide usernames directly.")
        return

    try:
        results = scrape_usernames(usernames)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    formatted_results = format_batch_results(results, args.color)

    print("\nResults:")
    print(formatted_results)

    if args.output:
        write_results_to_file(args.output, results)
        print(f"\nResults saved to {args.output}")
