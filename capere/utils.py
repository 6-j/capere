from colorama import Fore, Style


def format_username_availability(username, is_available):
    if is_available:
        return f"The username '{username}' is available!"
    else:
        return f"The username '{username}' is taken."


def format_username_availability_color(username, is_available):
    if is_available:
        return f"{Fore.GREEN}The username '{username}' is available!{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}The username '{username}' is taken.{Style.RESET_ALL}"


def format_batch_results(results, should_color):
    formatted_results = []
    for username, is_available in results.items():
        if should_color:
            formatted_results.append(format_username_availability_color(username, is_available))
        else:
            formatted_results.append(format_username_availability(username, is_available))
    return "\n".join(formatted_results)


def show_progress(current, total):
    print(f"Processing {current}/{total}...")


def validate_username(username):
    if not username:
        return False
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
    return all(char in allowed_characters for char in username)


def read_usernames_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def write_results_to_file(filename, results):
    with open(filename, "w") as file:
        for username, is_available in results.items():
            file.write(f"{username}: {'Available' if is_available else 'Taken'}\n")
