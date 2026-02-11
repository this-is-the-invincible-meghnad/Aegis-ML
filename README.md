# 🛡️ Aegis-ML: AI-Powered Network Vulnerability Scanner

> *"Traditional scanners just list ports. Aegis-ML understands them."*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-RandomForest-orange?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Ethical%20Hacking-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📖 Overview
**Aegis-ML** is an intelligent security tool that bridges the gap between **Network Scanning** and **Machine Learning**. 

Unlike standard scanners that simply report open ports, Aegis-ML uses a trained **Random Forest Classifier** to analyze port patterns. It predicts the **probability** of a system being vulnerable and assigns a confidence score.

## 🚀 Key Features
* **Smart Integration:** Automates `Nmap` for high-speed port discovery and service versioning (`-sV`).
* **AI Brain:** Uses a trained `Random Forest Classifier` to analyze port signatures and predict threat levels.
* **CEH Compliance:** Fully supports Module 3 requirements including **OS Fingerprinting** (`-O`) and **NSE Scripting** (`-sC`).
* **Risk Scoring:** Provides a real-time confidence percentage (e.g., "86.00% Safe") to prioritize security actions.
* **Cyberpunk UI:** Professional, color-coded CLI interface for clear threat visualization.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Scanning Engine:** Nmap (Network Mapper)
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Data Processing:** Pandas
* **Model Serialization:** Joblib

---

## ⚖️ Legal Disclaimer & Terms of Use

**⚠️ READ BEFORE USE**

**Aegis-ML** is a security research tool designed for **educational purposes**, **authorized penetration testing**, and **network defense analysis**.

1. **Authorized Use Only:** You are strictly prohibited from using this tool on government servers, corporate networks, or any device you do not own without explicit written permission.
2. **Liability:** The developer (**Abhinandan Pandey**) is **not responsible** for any damage, data loss, or legal consequences caused by the use or misuse of this software.
3. **Compliance:** Unauthorized scanning is a crime under the **Information Technology Act, 2000 (Section 43 & 66)** in India.

**USE AT YOUR OWN RISK.**

---

## ⚡ Installation & Usage

### Prerequisites
1. Install [Nmap](https://nmap.org/download.html) (Ensure it is in your System PATH).
2. Python 3.x installed.

### Setup
```bash
# 1. Clone the repository
git clone [https://github.com/this-is-the-invincible-meghnad/Aegis-ML.git](https://github.com/this-is-the-invincible-meghnad/Aegis-ML.git)
cd Aegis-ML

# 2. Install dependencies
pip install -r requirements.txt