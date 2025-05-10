import tkinter as tk
import threading
from tkinter import filedialog
from ui_elements import setup_ui
from website_checker import start_checking
import csv  
import pandas as pd  

def main():
    # Setup main window
    root = tk.Tk()
    root.title("🌐 Website Checker Pro - by Dipen Rana")
    root.geometry("850x650")
    root.configure(bg="#f0f0f5")
    root.resizable(False, False)

    # Setup UI
    elements = setup_ui(root)

    # Browse function
    def browse_file():
        filepath = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if filepath:
            elements['file_path_var'].set(filepath)

    # Start Checking
    def start_button_clicked():
        filepath = elements['file_path_var'].get()
        if not filepath:
            elements['messagebox'].showerror("Error", "Please select a TXT file first!")
            return
        elements['start_btn'].config(state="disabled")
        elements['stop_btn'].config(state="normal")
        elements['save_btn'].config(state="disabled")
        threading.Thread(target=start_checking, args=(
            filepath, elements
        ), daemon=True).start()

    # Stop Checking
    def stop_button_clicked():
        elements['stop_flag'][0] = True

    # Save Results
    def save_results_button_clicked():
        file_format = elements['file_format_var'].get().lower()
        output = elements['output']  # The result from website checking

        if file_format == 'csv':
            with open('website_check_results.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Website', 'Status'])
                writer.writerows(output)
            elements['messagebox'].showinfo("Saved", "Results saved as 'website_check_results.csv'")

        elif file_format == 'txt':
            with open('website_check_results.txt', 'w', encoding='utf-8') as f:
                for website, status in output:
                    f.write(f"{website} -> {status}\n")
            elements['messagebox'].showinfo("Saved", "Results saved as 'website_check_results.txt'")

        elif file_format == 'excel':
            df = pd.DataFrame(output, columns=['Website', 'Status'])
            df.to_excel('website_check_results.xlsx', index=False)
            elements['messagebox'].showinfo("Saved", "Results saved as 'website_check_results.xlsx'")

        else:
            elements['messagebox'].showerror("Error", "Unknown format! Please type: csv, txt, or excel.")
    
    # Hook functions
    elements['browse_btn'].config(command=browse_file)
    elements['start_btn'].config(command=start_button_clicked)
    elements['stop_btn'].config(command=stop_button_clicked)
    elements['save_btn'].config(command=save_results_button_clicked)

    root.mainloop()

if __name__ == "__main__":
    main()
