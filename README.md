## 🔍 SimpleScan

**SimpleScan** is a lightweight Python tool that checks if a specific TCP port is open on a target host using sockets.
---

### 🚀 Features

* Checks if a specific port is open on a target host
* Uses **TCP (SOCK\_STREAM)** connection
* 1-second timeout for faster scanning
* Simple and beginner-friendly

---

### 🛠️ Installation (Linux)

```bash
# Clone the repo
git clone https://github.com/priyan37/simplescan.git
cd port-scanner

# Make sure Python 3 is installed
python3 --version

# Run the script
python3 scanner.py
```
---

## ⚙️ Usage

```bash
$ python3 simplescan.py
Enter target IP or hostname: 192.168.1.1
Enter port to scan: 22
Port 22 is OPEN
```

---

## 🧠 How It Works

* `socket.AF_INET` — Uses IPv4 addressing (e.g., 192.168.1.1)
* `socket.SOCK_STREAM` — Establishes a TCP connection (reliable like a phone call)
* `connect_ex()` — Attempts to connect

  * Returns `0` → Port is **OPEN**
  * Returns non-zero → Port is **CLOSED**
* `socket.setdefaulttimeout(1)` — Waits 1 second max before giving up
* Always use `s.close()` to clean up

---

## 📘 TCP vs UDP (Extra)

This scanner uses **TCP** for reliable results.
To experiment with **UDP**, use `socket.SOCK_DGRAM` instead — but be aware, UDP is connectionless and harder to interpret accurately.

---

## ⚡ Future Ideas

* Scan multiple ports or a range
* Add UDP scanning support
* Implement multithreading for faster scans
* Save results to a file
* Add colored output or banners

---

## ⚠️ Disclaimer

> Use SimpleScan only on systems and networks you own or have **explicit permission** to scan. Unauthorized scanning can be illegal.

---

## 🧑‍💻 Author

**Priyadharshan Vadivel**
Cybersecurity Student & Solo Builder
[LinkedIn](https://www.linkedin.com/in/priyan37/) 

---
