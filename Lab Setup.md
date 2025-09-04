# Cybersecurity Lab Setup: Keylogger Exercise

## Overview

This document describes the setup of a simple cybersecurity lab environment used for low complexity offensive and defensive exercise involving keylogger scripts. The lab consists of two virtual machines (VMs): one acting as an attacker (Kali Linux) and the other as a target (Windows).

---

## Lab Topology

| Role        | OS           | vCPU | RAM    | Purpose                          |
|-------------|--------------|------|--------|----------------------------------|
| Attacker    | Kali Linux   | 2    | 8 GB   | Scripting, dev, command & control|
| Target      | Windows 10   | 2    | 4 GB   | Running and investigating scripts|

---

## Details

### 1. Kali Linux VM (Attacker)
- **OS:** Kali Linux 
- **vCPUs:** 2
- **RAM:** 8 GB
- **Installed Software:**
  - Python 3 (default on Kali)
  - PyCharm Professional (Student licence)
- **Usage:** Scripts development (in this lab keylogger and detector).

### 2. Windows VM (Target)
- **OS:** Windows 10 
- **vCPUs:** 2
- **RAM:** 4 GB
- **Installed Software:**
  - Python 3.17
    - Added to PATH for command-line execution
    - Pip for Python package installations
  - Scripts are copied and executed locally for simulation/testing

---

## Networking

- **Both VMs are on the same virtual network** (NAT for adapter 1 and Host-only for adapter 2).
- Can communicate with each other (ping, file transfer, etc.).
- No external exposure; isolated for safe experiments.

---

## Workflow

1. **Script Development**: Keylogger and detection scripts are made and edited on Kali using PyCharm.
2. **Deployment**: Scripts are transferred to the Windows VM for execution (via shared folder, SMB, or other means).
3. **Testing**: Keylogger is run on the Windows VM; detection script is used to identify and observe keylogger activity.

---

## Notes

- Only use this lab for ethical, educational, and authorized testing.
- Never run keyloggers outside of controlled, consented environment.
