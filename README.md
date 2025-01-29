## **📌 Project Overview**
This is an **UI Test Automation Framework** built using **Selenium WebDriver, Python, and Pytest**.  
It automates the **end-to-end testing** of a web-based application, ensuring functionality across login, cart management, and checkout processes.  

The framework supports **test execution with Allure Reports**, providing **detailed and interactive reports** for easy analysis.

## **✅ Implemented Test Cases**

### **1️⃣ Login Tests **
- ✅ **Test valid login** → Logs in successfully with correct credentials.
- ✅ **Test invalid login** → Verifies error message for wrong credentials.
- ✅ **Test empty login** → Ensures error message is shown for empty fields.

### **2️⃣ Cart Management Tests **
- ✅ **Test add to cart** → Adds an item and verifies it appears in the cart.
- ✅ **Test remove from cart** → Removes an item from the cart successfully.

### **3️⃣ Checkout Flow Tests **
- ✅ **Test checkout process** → Completes a successful order transaction.

---

## **📊 Test Execution & Allure Reports**
All test execution results are stored in **Allure Reports**, providing a **detailed, graphical representation of test cases**.

### **Run Tests & Generate Allure Reports**
1️⃣ Run all test cases and store results:  pytest tests/ --alluredir=reports/

