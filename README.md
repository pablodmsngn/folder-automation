# Folder Automator Tool

## Overview

This project implements an **automated file organization tool in Python**.
The tool is designed to scan a target directory, analyze the file types within it, and automatically move them into specific subfolders.

In this implementation, the **sorting rules are dynamically loaded** from a single, customizable `config.json` file, keeping the code clean and strictly separated from user preferences.

---

## Features

* **Deep Analysis**: Scans and counts all file extensions within a directory and its subdirectories.
* **Automated Organization**: Moves files into categorized subfolders based on a JSON map.
* **Collision Protection**: Prevents data loss by handling duplicate filenames (e.g., `image_1.jpg`).
* **Smart Cleanup**: Optionally deletes empty folders after files have been moved.
* **Modular Architecture**: Uses a separated structure (`src/` folder) for better maintenance.

---

## Project Structure

```text
.
├── src/
│   ├── analyzer.py
│   ├── cleaner.py
│   ├── loader.py
│   └── manager.py
├── config.json           <-- Main Configuration File
├── main.py
└── README.md

```

### `src/analyzer.py`

Contains the logic to scan the directory and extract statistics efficiently using `collections.Counter`:

* `folder_analyzer(folder_path)`
* `extensions_extraction(folder_path)`
* `data_extraction(counter)`

### `src/cleaner.py`

Handles the bottom-up directory traversal to safely delete empty folders:

* `remove_empty_folders(folder_path: str) -> bool`

### `src/loader.py`

Handles the safe parsing of the configuration files with error handling for missing or malformed JSON:

* `load_config(config_file: str) -> dict`

### `src/manager.py`

The core engine that determines file destinations and executes the move:

* `organize_files(folder_path: str, config: dict) -> bool`
* `resolve_duplicate(target_folder: str, filename: str) -> str`
* `get_target_path(extension: str, destinations: dict) -> str`

### `config.json`

The central dictionary defining sorting rules for your assets (images, icons, css, templates, js, and documents).

---

## How It Works

1. The user provides a **folder path**.
2. The program analyzes the directory and displays a breakdown of all **file extensions** found.
3. Sorting rules are loaded from `config.json`.
4. Files are moved to their new specific destinations:
* **Images**: `assets/images/gallery`
* **Icons**: `assets/icons`
* **Styles**: `assets/css`
* **Scripts**: `assets/module/js`


5. Any unrecognized extensions are moved to a default folder: `escritorio2/others`.
6. The user is prompted to clean up empty folders.

---

## Requirements

* **Python 3.x**
* Built-in libraries only: `os`, `shutil`, `json`, `collections`.

---

## How to Run

1. Open a terminal in the project folder.
2. Ensure `config.json` is in the root directory.
3. Run the application:
```bash
python main.py

```


4. Enter the path of the folder you wish to organize.

---

## License

This project is intended for **educational use**.

---
