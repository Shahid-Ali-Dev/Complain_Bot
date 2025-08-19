# 🐦 Auto Twitter Complain Bot  

This is a simple automation bot built with **Python + Selenium** that automatically complains to your internet provider on **Twitter (X.com)** when your internet speed is below the promised limit.  

---

## 📌 Features  
- Measures internet **download and upload speed** using `speedtest`.  
- Compares actual speeds with your **promised plan speeds**.  
- If the speed is lower, it **logs in to Twitter (X)** and tweets a complaint automatically.  
- Uses **Chrome profile storage** to keep you logged in (no need to log in every run).  

---

## ⚡ Requirements  
- Python 3.9+  
- Google Chrome installed  
- ChromeDriver (compatible with your Chrome version)  
- Python libraries:  
  ```bash
  pip install selenium speedtest-cli
