import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox
import csv

def setup_ui(root):
    file_path_var = tk.StringVar()
    stop_flag = [False]
    file_format_var = tk.StringVar(value="txt")  # Default format
    is_paused = [False]  # Flag to track pause/resume

    # Title
    title_label = tk.Label(root, text="🌐 Website Checker Tool", font=("Arial Rounded MT Bold", 24), fg="#004aad", bg="#f0f0f5")
    title_label.pack(pady=10)

    # File Frame
    top_frame = tk.Frame(root, bg="#f0f0f5")
    top_frame.pack(pady=5)

    browse_btn = tk.Button(top_frame, text="📂 Select TXT File", font=("Arial", 12), width=20, bg="#4CAF50", fg="white")
    browse_btn.grid(row=0, column=0, padx=5)

    file_entry = tk.Entry(top_frame, textvariable=file_path_var, width=60, font=("Arial", 12))
    file_entry.grid(row=0, column=1, padx=5)

    # Control Frame
    control_frame = tk.Frame(root, bg="#f0f0f5")
    control_frame.pack(pady=10)

    start_btn = tk.Button(control_frame, text="▶️ Start Checking", font=("Arial", 12), width=20, bg="#2196F3", fg="white")
    start_btn.grid(row=0, column=0, padx=10)

    stop_btn = tk.Button(control_frame, text="⛔ Stop", font=("Arial", 12), width=20, bg="#f44336", fg="white", state="disabled")
    stop_btn.grid(row=0, column=1, padx=10)

    # Pause/Resume Button
    def toggle_pause_resume():
        if is_paused[0]:
            # Resume the checking process
            is_paused[0] = False
            pause_resume_btn.config(text="⏸️ Pause")
        else:
            # Pause the checking process
            is_paused[0] = True
            pause_resume_btn.config(text="▶️ Resume")

    pause_resume_btn = tk.Button(control_frame, text="⏸️ Pause", font=("Arial", 12), width=20, bg="#FFC107", fg="white", command=toggle_pause_resume)
    pause_resume_btn.grid(row=0, column=2, padx=10)

    reset_btn = tk.Button(control_frame, text="🔄 Reset Terminal", font=("Arial", 12), width=20, bg="#FF5722", fg="white", command=lambda: reset_terminal())
    reset_btn.grid(row=0, column=3, padx=10)

    # Save Format Selection
    save_format_frame = tk.Frame(root, bg="#f0f0f5")
    save_format_frame.pack(pady=10)

    save_format_label = tk.Label(save_format_frame, text="Save as:", font=("Arial", 12), bg="#f0f0f5")
    save_format_label.grid(row=0, column=0, padx=10)

    # Dropdown (ttk.Combobox)
    save_format_dropdown = ttk.Combobox(save_format_frame, textvariable=file_format_var, values=["txt", "csv", "excel"], state="readonly", font=("Arial", 12), width=10)
    save_format_dropdown.grid(row=0, column=1, padx=10)

    save_btn = tk.Button(save_format_frame, text="💾 Save Results", font=("Arial", 12), width=20, bg="#FF9800", fg="white", state="disabled")
    save_btn.grid(row=0, column=2, padx=10)

    # Progress bar
    progress_bar = ttk.Progressbar(root, length=750)
    progress_bar.pack(pady=10)

    # Status Label
    status_label = tk.Label(root, text="Status: Waiting to start...", font=("Arial", 12), bg="#f0f0f5")
    status_label.pack()

    # Text Area for Logs
    text_area = scrolledtext.ScrolledText(root, width=100, height=20, font=("Consolas", 10))
    text_area.pack(padx=10, pady=10)

    # Footer / Logo
    footer_label = tk.Label(root, text="✨ by Dipen Rana", font=("Segoe Script", 14, "italic"), fg="gray", bg="#f0f0f5")
    footer_label.pack(pady=10)

    # Function to reset the terminal (clear text area)
    def reset_terminal():
        text_area.delete(1.0, 'end')  # Clear the entire text area

    return {
        'file_path_var': file_path_var,
        'browse_btn': browse_btn,
        'start_btn': start_btn,
        'stop_btn': stop_btn,
        'pause_resume_btn': pause_resume_btn,  # Added Pause/Resume button
        'reset_btn': reset_btn,
        'save_btn': save_btn,
        'progress_bar': progress_bar,
        'status_label': status_label,
        'text_area': text_area,
        'messagebox': messagebox,
        'stop_flag': stop_flag,
        'file_format_var': file_format_var,
        'save_format_dropdown': save_format_dropdown,  # Added the dropdown
        'output': [],  # Placeholder for website results
        'is_paused': is_paused,  # Flag to track pause/resume
    }
