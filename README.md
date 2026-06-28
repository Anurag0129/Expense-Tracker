# Expense Tracker

A simple command-line expense tracker built in Python as a beginner project.

## Features
- Add new expenses with category, amount, date, and note
- View all expenses in a formatted table
- Delete expenses by row number
- View total spending and category-wise breakdown
- Input validation (no empty categories, no negative/zero amounts)
- Data persists between runs using a local JSON file (`expenses.json`)

## How to run

1. Clone this repository
    
    git clone https://github.com/Anurag0129/expense-tracker.git

    cd expense-tracker

2. (Optional) Create and activate a virtual environment
    
    python -m venv venv

    venv\Scripts\activate

3. Run the program

    python expense_tracker.py


## Menu options

| Option | Action |
|--------|--------|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | Delete Expense |
| 4 | Show Summary |
| 5 | Exit |

## Tech used
- Python 3
- Built-in `json` module for data persistence
- Built-in `datetime` module for automatic date stamping

## Status
✅ Core features complete — built step by step while learning Python.

## Possible future improvements
- Edit existing expenses
- Filter expenses by date range or category
- Monthly spending reports
- Export to CSV