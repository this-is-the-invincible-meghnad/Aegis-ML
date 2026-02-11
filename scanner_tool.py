import nmap
import pandas as pd
import joblib
import sys
from colorama import init, Fore, Style

# Initialize Colors (Auto-reset helps keep it clean)
init(autoreset=True)

# ASCII ART LOGO
BANNER = Fore.CYAN + Style.BRIGHT + r"""
    _    ____ ____ ___ ____        __  __ _     
   / \  | ____/ ___|_ _/ ___|      |  \/  | |    
  / _ \ |  _|| |  _ | |\___ \ _____| |\/| | |    
 / ___ \| |__| |_| || | ___) |_____| |  | | |___ 
/_/   \_\_____\____|___|____/      |_|  |_|_____|
                                                 
    [ AI-POWERED VULNERABILITY SCANNER v1.0 ]
    [ Dev: Invincible Meghnad | System: ONLINE ]
"""

# Load the Brain
try:
    model = joblib.load('aegis_brain.pkl')
except:
    print(Fore.RED + "[!] ERROR: Brain not found! Run 'python train_model.py' first.")
    sys.exit()

# Configure Nmap (Adjust path if needed, but it worked last time!)
# We keep the path explicitly to be safe based on your previous success
nm = nmap.PortScanner(nmap_search_path=['C:\\Program Files (x86)\\Nmap\\nmap.exe', 'C:\\Program Files\\Nmap\\nmap.exe'])

def scan_target(ip):
    print(BANNER)
    print(Fore.YELLOW + f"[*] TARGET LOCKED: {ip}")
    print(Fore.YELLOW + "[*] INITIALIZING SCAN ENGINES (Please wait)...")
    
    # -sV means "Service Version" (Find out WHAT is running)
    # -T4 is Fast Timing
    nm.scan(ip, arguments='-sV -T4')
    
    if ip not in nm.all_hosts():
        print(Fore.RED + "[-] Host is DOWN or blocking our pings.")
        return

    # Get Open Ports
    try:
        open_ports = nm[ip]['tcp'].keys()
    except KeyError:
        print(Fore.RED + "[-] No open TCP ports found.")
        return

    print(Fore.GREEN + f"\n[+] HOST IS UP. FOUND {len(open_ports)} OPEN PORTS:")
    
    # Prepare Data for AI
    input_data = {'21': 0, '22': 0, '23': 0, '80': 0, '443': 0, '445': 0, '3389': 0}
    
    # Loop through ports to show details
    for port in open_ports:
        service = nm[ip]['tcp'][port]['product']
        version = nm[ip]['tcp'][port]['version']
        print(f"    > Port {port}: {Fore.CYAN}{service} {version}")
        
        # Feed data to AI
        if str(port) in input_data:
            input_data[str(port)] = 1

    # AI PREDICTION
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df).max() * 100

    print("\n" + "="*40)
    print(Fore.WHITE + Style.BRIGHT + "       AI INTELLIGENCE REPORT")
    print("="*40)
    
    if prediction == 'DANGEROUS':
        print(Fore.RED + Style.BRIGHT + f"[!] THREAT DETECTED: CRITICAL")
        print(Fore.RED + f"[!] CONFIDENCE: {probability:.2f}%")
        print(Fore.RED + "[!] ACTION: Manual Verification Required (Possible Exploit)")
    else:
        print(Fore.GREEN + Style.BRIGHT + f"[+] SYSTEM STATUS: SAFE")
        print(Fore.GREEN + f"[+] CONFIDENCE: {probability:.2f}%")
        print(Fore.WHITE + "[+] ACTION: Routine Monitoring")
    
    print("="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Usage: python scanner_tool.py <target_ip>")
    else:
        target_ip = sys.argv[1]
        scan_target(target_ip)