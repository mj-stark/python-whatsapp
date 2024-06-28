import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit

# Function to send messages
def send_messages():
    phone_numbers = entry_numbers.get().split(',')
    message = entry_message.get("1.0", tk.END).strip()
    
    if not phone_numbers or not message:
        messagebox.showwarning("Input Error", "Please enter phone numbers and a message.")
        return

    for number in phone_numbers:
        number = number.strip()
        try:
            # Send the message instantl y
            kit.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True, close_time=5)
            print(f"Message sent to {number}")
            messagebox.showinfo("Success", f"Message sent to {number}")
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")
            messagebox.showerror("Error", f"Failed to send message to {number}: {e}")

# Set up the main application window
root = tk.Tk()
root.title("WhatsApp Message Sender")

# Phone numbers input
tk.Label(root, text="Phone Numbers (comma-separated):").pack(pady=5)
entry_numbers = tk.Entry(root, width=50)
entry_numbers.pack(pady=5)

# Message input
tk.Label(root, text="Message:").pack(pady=5)
entry_message = tk.Text(root, height=10, width=50)
entry_message.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send Messages", command=send_messages)
send_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
