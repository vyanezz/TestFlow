# 🚀 TestFlow

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**TestFlow** is an experimental Python end-to-end (E2E) testing framework that combines browser automation with HTTP traffic validation in a single workflow.

Built on top of **Selenium** and **mitmproxy**, it allows you to validate not only UI behavior but also the exact network requests and responses generated during user interactions.

This makes it possible to test full application flows the way they actually work: from `click` → `API request` → `backend response` → `UI result`.

---

## 💡 The Problem it Solves (Why TestFlow?)

Modern web applications are API-driven. However, most UI automation tools only validate what happens in the browser's DOM. This means **a visual test can pass while the backend is actually broken or sending incorrect data.**

For example:
1. The UI redirects to a dashboard after a login attempt.
2. But the login API actually returned incomplete data, or the wrong endpoint was called entirely.

Instead of guessing what happened behind a button click or splitting your tests into separate "UI Tests" and "API Tests", **TestFlow merges both layers into one execution flow.**

### Traditional Approach vs. TestFlow

* **Traditional:** UI test (checks page behavior) + API test (checks backend separately) + Manual correlation between both.
* **TestFlow:** A single test validates UI behavior, request correctness, backend response, and the real integration between both layers.

---

## ⚙️ Installation

Currently, TestFlow is in active development and is not yet available as a package. The only way to install and run it is by installing the required dependencies locally in your project:

```bash
pip install -r requirements.txt
```

> **Note:** TestFlow currently uses **Google Chrome** by default. Ensure you have Chrome installed on your system. Selenium will automatically handle the ChromeDriver management.

---

## 🛠️ Usage Example: Login Flow

This example shows a complete login validation. It verifies the UI interaction, the endpoint used, the HTTP method, the sent payload, the backend response, and the final UI state.

```python
from test_flow import TestFlow

test = TestFlow(
    enable_logger=True,
    headless=True
)

test.navigate("[https://myapp.com/login](https://myapp.com/login)")

# Intercept and validate the network request triggered by the click.
with test.expect_request(
    endpoint="[https://api.myapp.com/auth/login](https://api.myapp.com/auth/login)",
    method="POST",
    json_body={
        "email": "john@test.com",
        "password": "secret123"
    },
    timeout=10 
) as flow:
    
    # UI actions inside the context
    test.send_keys("id", "email", "john@test.com")
    test.send_keys("id", "password", "secret123")
    test.click("id", "login-button")

# Backend response validations
flow.assert_status(200)
flow.assert_json({
    "success": True
})

# Final UI state validation
test.assert_url("/dashboard")

test.stop_test()
```

*To run your tests, simply execute the Python file directly:* `python my_test.py`

---

## 🧠 Core Concepts

### Browser Automation
Simple Selenium-based API for user actions:
```python
test.navigate(url)
test.send_keys("id", "username", "john")
test.click("id", "submit")
```

### Request Validation
Define the expected network behavior triggered by UI actions:
```python
with test.expect_request(endpoint="/api/users", method="POST"):
    test.click("id", "save-button")
```

### Traffic Synchronization
Wait for specific requests to occur before continuing execution (ideal for SPAs or async calls):
```python
# Pause execution until the request occurs (with optional timeout)
test.wait_for_request("[https://api.example.com/users](https://api.example.com/users)", "GET", timeout=5)
```

---

## 🏗️ Architecture

```text
┌──────────────────────────────┐
│          Test Case (Script)  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          TestFlow            │
│         Public API           │
└───────┬───────────┬──────────┘
        │           │
        ▼           ▼
┌─────────────┐ ┌─────────────┐
│ Selenium    │ │ HTTP Layer  │
│ (Chrome)    │ │ Validation  │
└──────┬──────┘ └──────┬──────┘
       │               │
       └───────┬───────┘
               ▼
┌──────────────────────────────┐
│      Embedded mitmproxy      │
│     Traffic Interception     │
└──────────────────────────────┘
```
> *Note on HTTPS:* By using `mitmproxy` to intercept local traffic, HTTPS requests are internally analyzed by the TestFlow engine. If you experience SSL certificate issues in the test browser, check your local proxy configuration settings.

---

## 🚧 Project Status (Roadmap)
TestFlow is an evolving project. It currently features:
* **Browser:** Exclusive support for Google Chrome.
* **Execution:** Runs as standalone `.py` scripts (not yet integrated with test runners like `pytest` or `unittest`).
* **License:** MIT (Feel free to use, modify, and contribute!).
