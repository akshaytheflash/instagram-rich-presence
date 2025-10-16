from instagrapi import Client
import win32gui
import win32process
import psutil
import time

cl = Client()

sessionid = "enter session id here"  # Replace with your actual session ID
cl.login_by_sessionid(sessionid)

while(True):
    activeWindowHandle = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(activeWindowHandle)
    threadid, processid = win32process.GetWindowThreadProcessId(activeWindowHandle)

    try:
        process = psutil.Process(processid)
        processName = process.name()
    
    except psutil.NoSuchProcess:
        processName = "Unknown"

    if processName.casefold() == "spotify.exe":
        noteText = f"Listening to {window_title}"

    elif processName.casefold() == "code.exe":
        file_name = window_title.split()[0] if window_title else "unknown file"
        noteText = f"Editing code in file: {file_name}"

    elif processName.casefold() in ["chrome.exe", "firefox.exe", "msedge.exe"]:
        if " - youtube" in window_title.lower():  
            parts = window_title.rsplit(" - YouTube", 1)
            video_title = parts[0] if parts else window_title
            noteText = f"Watching: {video_title}"
        else:
            tab_title = window_title.split(" - ")[0] if window_title else "unknown tab"
            noteText = f"Browsing: {tab_title}"


    elif processName.casefold() == "word.exe":
        noteText = f"Writing document: {window_title}"

    else:
        noteText = f"Using {processName} window: {window_title}"

    note = cl.create_note(noteText, 0)
    
    print("Note posted successfully!")

    time.sleep(15)




