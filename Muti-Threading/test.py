import threading
import tkinter as tk

def create_window(title, x, y):
    # Create a new thread-safe tkinter window
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{x}x{y}")

    # Create a label in the window
    label = tk.Label(window, text=f"This is {title} window")
    label.pack(padx=20, pady=20)

    # Run the tkinter main loop for this window
    window.mainloop()

def main():
    # Create two threads, each for creating a tkinter window
    thread1 = threading.Thread(target=create_window, args=("Window 1", 300, 200))
    thread2 = threading.Thread(target=create_window, args=("Window 2", 400, 300))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
