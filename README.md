# capere
> Python CLI program to check username availability

A Python CLI tool that checks the availability of GitHub usernames by scraping profile pages. It can read usernames from a file or accept them directly as arguments.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/6-j/capere.git
   cd capere
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
Check the availability of one or more usernames:
   ```sh
   python -m capere username1 username2 username3
   ```

### Read Usernames from a File
Provide a file containing usernames (one per line):
   ```sh
   python -m capere --file usernames.txt
   ```

### Save Results to a File
Save the results to a file:
   ```sh
   python -m capere --file usernames.txt --output results.txt
   ```

### Enable Colored Output
Display results with colored output:
   ```sh
   python -m capere --file usernames.txt --color
   ```

## Features

- **Batch processing**: Check multiple usernames at once.
- **File support**: Read usernames from a file and save results to a file.
- **Colored output**: Highlight available and taken usernames in the terminal.
- **Progress indicator**: See the progress of batch processing.

## Example

1. Create a file called `usernames.txt` with the following content:
   ```txt
   username1
   username2
   username3
   ```

2. Run the program:
   ```sh
   python -m capere --file usernames.txt --color --output results.txt
   ```

3. View the results in the terminal:
   ```txt
   Results:
   The username 'username1' is available!
   The username 'username2' is taken.
   The username 'username3' is available!
   
   Results saved to results.txt
   ```

## Dependencies

- Python 3.8+
- requests>=2.25.1
- colorama~=0.4.6

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

