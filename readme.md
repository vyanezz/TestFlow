# 🚀 TestFlow

A lightweight Python test automation framework that combines **Selenium-based UI testing** with **network traffic validation** using an embedded proxy.

It allows you to validate both **frontend behavior** and **backend responses** within the same test flow, providing a more complete end-to-end testing approach.

---

## ✨ Features

- Simplified and intuitive Selenium WebDriver wrapper  
- Built-in support for capturing HTTP requests  
- Response validation (status, headers, body)  
- Clean and readable test API  
- Optional logging for debugging  

---

## 🧱 Architecture

The framework is composed of:

- **WebDriver** → Simplified Selenium wrapper  
- **ApiValidator** → Handles request and response validation  
- **Embedded Proxy** → Captures network traffic during test execution  
- **TestFlow** → Main entry point for users  

---

## 🎯 Goal

Provide a simple, scalable, and easy-to-use framework for writing tests that validate both **UI interactions** and **network communication** in a unified way.

---

## 🚧 Status

Work in progress. The framework is actively evolving.
