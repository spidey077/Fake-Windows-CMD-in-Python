# Fake Windows Command Prompt (Python)

## Overview

This project is a **fake but realistic Windows Command Prompt** built entirely in Python.  
It simulates how CMD works internally while staying completely safe.  
No real files, processes, or network actions are used. Everything happens in memory.

The goal of this project is learning — understanding how command-line shells handle input, manage state, and execute commands.

---

## What This Project Is

- A learning-focused CMD simulator
- Fully fake and sandboxed
- Inspired by real Windows CMD behavior
- Written using only Python’s standard library

This is **not** a hacking tool and **does not** interact with your actual system.

---

## Main Features

### Shell Behavior
- Realistic CMD-style prompt
- Continuous command loop
- Command history support
- Built-in help system

### Fake File System
- In-memory directories and files
- Supports:
  - `dir`
  - `cd`
  - `mkdir`
  - `rmdir`
  - `type`
  - `del`

### Simulated Network Commands
(All outputs are fake but realistic)

- `ipconfig`
- `ping`
- `tracert`
- `arp`
- `netstat`

### System & Utility Commands

- `ver`
- `whoami`
- `systeminfo`
- `tasklist`
- `taskkill`
- `date`
- `time`
- `cls`
- `color`
- `echo`
- `history`
- `help`
- `exit`

---

## Example Usage

```text
C:\Users\Imdadullah> dir
C:\Users\Imdadullah> cd Documents
C:\Users\Imdadullah> type project.txt
C:\Users\Imdadullah> ping google.com
C:\Users\Imdadullah> tasklist
C:\Users\Imdadullah> taskkill /pid 2211
C:\Users\Imdadullah> systeminfo
C:\Users\Imdadullah> history
C:\Users\Imdadullah> exit
