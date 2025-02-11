import asyncio
import aiohttp
import requests
from termcolor import colored
from urllib.parse import urlparse
import os
import sys

# Function to validate URL format
def is_valid_url(url):
    """
    Validate the format of a given URL.
    Returns True if valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Synchronous fuzzing function
def sync_fuzz(base_url, payloads, output_file):
    """
    Perform synchronous fuzzing by replacing '@' in the base URL with payloads.
    Logs only successful (200) responses to the output file and prints them.
    """
    success_count = 0

    with open(output_file, 'w') as log_file:
        for payload in payloads:
            url = base_url.replace('@', payload.strip())
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    success_count += 1
                    print(colored(url, 'green'))
                    log_file.write(f"{url}\n")
            except Exception as e:
                pass  # Ignore errors for this task

    print(f"\nSuccessful responses (200): {success_count}")

# Asynchronous fuzzing function
async def async_fuzz(base_url, payloads, output_file):
    """
    Perform asynchronous fuzzing by replacing '@' in the base URL with payloads.
    Logs only successful (200) responses to the output file and prints them.
    """
    success_count = 0

    async with aiohttp.ClientSession() as session:
        with open(output_file, 'w') as log_file:
            tasks = []
            for payload in payloads:
                url = base_url.replace('@', payload.strip())
                tasks.append(fetch_url(session, url))

            results = await asyncio.gather(*tasks, return_exceptions=True)
            for i, result in enumerate(results):
                if isinstance(result, dict) and result['status'] == 200:
                    success_count += 1
                    print(colored(result['url'], 'green'))
                    log_file.write(f"{result['url']}\n")

    print(f"\nSuccessful responses (200): {success_count}")

# Coroutine to fetch a single URL asynchronously
async def fetch_url(session, url):
    """
    Fetch a single URL asynchronously using aiohttp.
    Returns a dictionary with the URL and status code if successful,
    or an exception object if an error occurs.
    """
    try:
        async with session.get(url, timeout=10) as response:
            return {'url': url, 'status': response.status}
    except Exception as e:
        return e

# Main function to handle argument parsing and execution
def main():
    """
    Main entry point for the script. Parses arguments,
    validates inputs, and runs the appropriate fuzzing mode (sync/async).
    """
    import argparse

    parser = argparse.ArgumentParser(description="AFUZZ - ** Async URL Fuzzer **Perform synchronous fuzzing by replacing '@' in the base URL with payloads.
    Logs only successful (200) responses to the output file and prints them.")
    parser.add_argument('-u', '--url', required=True, help='Base URL with @ as placeholder')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to wordlist file')
    parser.add_argument('-o', '--output', required=True, help='Output file for results')
    parser.add_argument('-m', '--mode', choices=['sync', 'async'], default='sync', help='Fuzzing mode (sync/async)')
    
    args = parser.parse_args()

    # Validate inputs
    if not is_valid_url(args.url):
        print("[!] Invalid base URL format.")
        sys.exit(1)

    if '@' not in args.url:
        print("[!] Base URL must contain a placeholder '@'.")
        sys.exit(1)

    if not os.path.isfile(args.wordlist):
        print(f"[!] Wordlist file '{args.wordlist}' not found.")
        sys.exit(1)

    if os.path.exists(args.output):
        overwrite = input(f"[?] Output file '{args.output}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("[!] Operation aborted.")
            sys.exit(1)

    # Read payloads from wordlist
    try:
        with open(args.wordlist, 'r') as f:
            payloads = f.readlines()
    except Exception as e:
        print(f"[!] Error reading wordlist: {e}")
        sys.exit(1)

    # Perform fuzzing based on mode
    if args.mode == 'sync':
        sync_fuzz(args.url, payloads, args.output)
    elif args.mode == 'async':
        asyncio.run(async_fuzz(args.url, payloads, args.output))

if __name__ == "__main__":
    main()
                                       
