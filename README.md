# 🛡️ Aegis-ML: AI-Powered Network Vulnerability Scanner

> *"Traditional scanners just list ports. Aegis-ML understands them."*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-RandomForest-orange?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Ethical%20Hacking-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📖 Overview
**Aegis-ML** is an intelligent security tool that bridges the gap between **Network Scanning** and **Machine Learning**. 

Unlike standard scanners (like Nmap) that simply report open ports, Aegis-ML uses a trained **Random Forest Classifier** to analyze port patterns and service banners. It predicts the **probability** of a system being vulnerable to exploitation (e.g., EternalBlue, RDP attacks) and assigns a confidence score.

## 🚀 Key Features
* **Smart Integration:** Automates `Nmap` for high-speed port discovery and service versioning (`-sV`).
* **AI Brain:** Uses `Scikit-Learn` to classify targets as **SAFE** or **CRITICAL** based on port signatures.
* **Risk Scoring:** Provides a confidence percentage (e.g., "72.50% Critical") to help pentesters prioritize targets.
* **Zero-Noise:** Filters out standard traffic to focus on high-risk vectors (SMB, Telnet, RDP).
* **Cyberpunk UI:** Professional CLI with color-coded threat detection.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Scanning Engine:** Nmap (Network Mapper)
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Data Processing:** Pandas
* **Model Serialization:** Joblib

# ⚖️ Legal Disclaimer & Terms of Use

## 1. Authorized Use Only
**Aegis-ML** is a security research tool designed for **educational purposes**, **authorized penetration testing**, and **network defense analysis**.

You are **strictly prohibited** from using this tool on:
* Government servers or networks.
* Corporate networks without written permission (Authorization Letter).
* Any device or IP address you do not own or have explicit consent to test.

## 2. Liability
The developer (**Invincible Meghnad**) and contributors of this repository are **not responsible** for any damage, data loss, or legal consequences caused by the use or misuse of this software. 

By downloading, installing, or using this software, you agree that:
1. You will use it solely for legal and ethical purposes.
2. You acknowledge that unauthorized scanning is a crime under the **Information Technology Act, 2000 (Section 43 & 66)** in India, the **Computer Fraud and Abuse Act (CFAA)** in the USA, and similar laws globally.

## 3. Educational Intent
This project demonstrates how Machine Learning can be applied to Cybersecurity for **defensive** purposes (Vulnerability Assessment). It is not designed to aid in malicious activities.

---
**USE AT YOUR OWN RISK.**

## ⚡ Installation & Usage

### Prerequisites
1. Install [Nmap](https://nmap.org/download.html) (Ensure it is in your System PATH).
2. Python 3.x installed.

### Setup
```bash
# 1. Clone the repository
git clone [https://github.com/this-is-the-invincible-meghnad/Aegis-ML.git](https://github.com/this-is-the-invincible-meghnad/Aegis-ML.git)
cd Aegis-ML

# 2. Install Python dependencies
pip install -r requirements.txt