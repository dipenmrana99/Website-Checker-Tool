import csv
import pandas as pd
from tkinter import messagebox

def save_results(output, file_format):
    if file_format == 'csv':
        with open('website_check_results.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Website', 'Status'])
            writer.writerows(output)
        messagebox.showinfo("Saved", "Results saved as 'website_check_results.csv'")

    elif file_format == 'txt':
        with open('website_check_results.txt', 'w', encoding='utf-8') as f:
            for website, status in output:
                f.write(f"{website} -> {status}\n")
        messagebox.showinfo("Saved", "Results saved as 'website_check_results.txt'")

    elif file_format == 'excel':
        df = pd.DataFrame(output, columns=['Website', 'Status'])
        df.to_excel('website_check_results.xlsx', index=False)
        messagebox.showinfo("Saved", "Results saved as 'website_check_results.xlsx'")

    else:
        messagebox.showerror("Error", "Unknown format! Please type: csv, txt, or excel.")
