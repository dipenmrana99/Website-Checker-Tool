import requests
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from file_saver import save_results
from utils import clean_website_list

def check_website(site):
    try:
        response = requests.get(site, timeout=8)
        if response.status_code == 200:
            return (site, 'Alive')
        else:
            return (site, f'Error {response.status_code}')
    except Exception:
        return (site, 'Dead or Error')

def start_checking(filepath, elements):
    stop_flag = elements['stop_flag']
    websites = clean_website_list(filepath)
    output = []
    total = len(websites)
    count = 0

    elements['progress_bar']['maximum'] = total
    elements['progress_bar']['value'] = 0
    elements['status_label'].config(text=f"Status: 0/{total}")

    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_site = {executor.submit(check_website, site): site for site in websites}
        for future in as_completed(future_to_site):
            if stop_flag[0]:
                break

            result = future.result()
            output.append(result)
            count += 1

            elements['text_area'].insert('end', f"✔️ {count}/{total} {result[0]} -> {result[1]}\n")
            elements['text_area'].see('end')
            elements['progress_bar']['value'] = count
            elements['status_label'].config(text=f"Status: {count}/{total}")

    elements['output'] = output  # Pass the result to the save button

    if output and not stop_flag[0]:
        elements['save_btn'].config(state="normal")

    elements['start_btn'].config(state="normal")
    elements['stop_btn'].config(state="disabled")

    if stop_flag[0]:
        elements['messagebox'].showwarning("Stopped", "⛔ Checking was manually stopped!")
    else:
        elements['messagebox'].showinfo("Done", "✅ Finished checking websites!")
