# 🎪 AFUZZ: Async URL Fuzzer 🎮  

Welcome to **AFUZZ**, a lightweight and efficient URL fuzzing tool designed to test web applications for vulnerabilities or hidden endpoints. Whether you're a penetration tester, bug bounty hunter, or just someone who loves exploring the unknown, AFUZZ is here to make your fuzzing experience both fun and powerful! 🎉

---

## 🎯 Features  

- 🌐 **Supports Synchronous and Asynchronous Modes**  
  Choose between synchronous (blocking) or asynchronous (non-blocking) fuzzing for optimal performance.  

- ⚡ **Fast and Efficient**  
  Leverages `aiohttp` for blazing-fast asynchronous requests.  

- 🛠️ **Customizable Payloads**  
  Use your own wordlists to replace placeholders in the base URL.  

- ✅ **Logs Only Successful Responses (200)**  
  Outputs only URLs with `200 OK` responses, keeping your results clean and focused.  

- 🖍️ **Color-Coded Output**  
  Highlights successful URLs in green for better visibility.  

- 💾 **Output Results to File**  
  Saves results to a specified file for later analysis.  

---

## 🕹️ How It Works  

AFUZZ replaces the `@` placeholder in the base URL with payloads from a wordlist and sends HTTP requests to test each variation. You can choose between synchronous or asynchronous modes based on your needs.  

---

## 🎪 Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/afuzz.git
   cd AFUZZ
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. You're ready to fuzz! 🎉  

---

## 🎮 Usage  

Run the script with the following options:  

```bash
python afuzz.py -u <base_url> -w <wordlist> -o <output_file> -m <mode>
```

### Options:  
| Option        | Description                                                                                 |
|---------------|---------------------------------------------------------------------------------------------|
| `-u`, `--url` | Base URL with `@` as a placeholder (e.g., `https://example.com/@`).                         |
| `-w`, `--wordlist` | Path to your wordlist file containing payloads (one per line).                           |
| `-o`, `--output` | Path to the output file where results will be saved (e.g., `results.txt`).                |
| `-m`, `--mode` | Fuzzing mode: `sync` (synchronous) or `async` (asynchronous). Default is `sync`.            |

---

## 🎢 Examples  

### Example 1: Synchronous Fuzzing  
```bash
python afuzz.py -u "https://example.com/@" -w wordlist.txt -o results.txt -m sync
```

### Example 2: Asynchronous Fuzzing  
```bash
python afuzz.py -u "https://example.com/@" -w wordlist.txt -o results.txt -m async
```

### Example Output:  
#### Console Output:  
```plaintext
https://response1.com
https://response2.com

Successful responses (200): 2
```

#### Output File (`results.txt`):  
```plaintext
https://response1.com
https://response2.com
```

---

## 🎭 How It Works Under the Hood  

### 🧩 Core Functions:

1. **URL Validation**  
   Ensures the base URL is valid and contains the placeholder (`@`).  

2. **Synchronous Fuzzing (`sync_fuzz`)**  
   Replaces the placeholder with each payload, sends HTTP requests using `requests`, and logs only successful responses (`200 OK`).  

3. **Asynchronous Fuzzing (`async_fuzz`)**  
   Uses `aiohttp` to perform non-blocking HTTP requests, allowing multiple URLs to be tested simultaneously for faster results.  

4. **Output Handling**  
   Logs only successful URLs (`200 OK`) to both the console and an output file for clarity and simplicity.  

---

## 🛠️ Code Overview  

Here's a brief overview of how AFUZZ works:

### Main Components:
1. **Input Validation:**  
   Ensures the base URL, wordlist, and other inputs are valid before proceeding.

2. **Synchronous Mode:**  
   Uses Python's `requests` library to send HTTP requests one at a time.

3. **Asynchronous Mode:**  
   Leverages Python's `asyncio` and `aiohttp` libraries for concurrent requests.

4. **Output Results:**  
   Logs only URLs with a status code of 200 (`OK`) to both the console and output file.

---

## 🛡️ Error Handling  

AFUZZ handles common errors gracefully:
- Invalid URLs are flagged during validation.
- Errors during HTTP requests are logged but do not interrupt execution.
- If an output file already exists, you'll be prompted before overwriting it.

---
    
## 🎈 License  

This project is licensed under [MIT License](LICENSE). Feel free to use it in your projects! 😊  

---

Happy fuzzing! 🚀

---
