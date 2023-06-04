# Port_Scanner

A Simple Multithreaded Port Scanner in Python enables simultaneous scanning of multiple network ports for efficient identification of open ports.

# Features

- Scans multiple network ports simultaneously using multithreading to enhance performance and reduce scanning time.
- Utilizes a thread-safe queue to manage the distribution of port scanning tasks among multiple threads.
- Implements a lock mechanism to ensure proper access to shared resources when multiple threads are involved.
- Provides real-time feedback during the scanning process, allowing you to monitor the progress and status of each port being scanned.
- Handles user interruptions gracefully, allowing you to stop the scanning process at any time.
- Supports command-line usage with argument parsing, providing flexibility and ease of use.

# Usage 

1. Clone the Repository in your terminal using command :      
   
       git clone https://github.com/Cyber-Aakash/Port_Scanner
    
2. Run the following command to see the available options :      
   
       python port_scanner.py --help
 
3. Use the following command format to scan a target host for open ports :  
   
       python port_scanner.py targetname -p 1-1000
  
   - `-p`, `--port_range`: The range of ports to scan (e.g., "1-100" or "80,443,8080").

# Example

To scan the ports 1 to 1000 on the target host example.com, use the following command :   

    python port_scanner.py example.com -p 1-1000


This will initiate the port scanning process, and the scanner will display the status of each scanned port.
