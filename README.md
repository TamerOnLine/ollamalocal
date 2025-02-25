# ollamalocal

## 🚀 Overview
`ollamalocal` is a lightweight and automated environment setup script designed to streamline the process of creating and activating a virtual environment across different operating systems (**Windows, Linux, and macOS**). This project ensures that Python dependencies are properly managed and integrated with your development workflow. It also includes **LangChain Ollama** support to interact with AI models seamlessly.

## ✨ Features
- **Cross-Platform Support**: Works seamlessly on Windows (`.bat`, `.ps1`), Linux (`.sh`), and macOS (`.sh`).
- **Automated Virtual Environment Setup**: Detects Python installation, creates a virtual environment, and activates it.
- **Pip Package Management**: Ensures the latest version of pip and installs dependencies from `requirements.txt`.
- **Integrated with VS Code**: Provides a `.code-workspace` file for one-click environment activation in Visual Studio Code.
- **Supports LangChain Ollama**: Easily interact with the `mistral` model for AI-driven responses.

---

## 📥 Installation

### 🛠 Prerequisites
- **Python 3.6+** (Check installation using: `python --version`)
- **Git** (Optional) for cloning the project
- **VS Code** (Optional) for an enhanced development experience

### 🔧 Setup Instructions

#### **Windows**
1. **Using Command Prompt:**
   ```cmd
   cd path/to/ollamalocal
   activate_project.bat
   ```
2. **Using PowerShell:**
   ```powershell
   cd path/to/ollamalocal
   .\activate_project.ps1
   ```

#### **Linux/macOS**
1. Grant execution permission:
   ```bash
   cd path/to/ollamalocal
   chmod +x activate_project.sh
   ```
2. Run the script:
   ```bash
   ./activate_project.sh
   ```

---

## 📂 Project Structure
```
ollamalocal/
├── README.md                # Documentation
├── LICENSE                  # License file
├── activate_project.bat     # Windows CMD script
├── activate_project.ps1     # Windows PowerShell script
├── activate_project.sh      # Linux/macOS Bash script
├── requirements.txt         # List of dependencies
├── workspace.code-workspace # VS Code workspace configuration
├── src/
│   ├── __init__.py
│   └── main.py              # Main script for interacting with Ollama LLM
├── tests/
│   ├── __init__.py
│   └── test_example.py      # Basic test case
└── .github/
    └── workflows/
        └── main.yml         # CI/CD workflow for testing the virtual environment
```

---

## 🚀 Usage

### ✅ **Activate the Virtual Environment**
After running the setup script for your OS, the virtual environment will be activated automatically. You can confirm this by checking your terminal prompt:
```bash
(venv) user@machine:~/ollamalocal$
```

### 📦 **Install Dependencies**
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 📝 **Run LangChain Ollama Script**
```bash
python src/main.py
```
You will be prompted to enter a question, and the `mistral` model will provide a response.

### ❌ **Deactivate the Virtual Environment**
```bash
deactivate
```

---

## 🔄 **Troubleshooting**
| Issue | Solution |
|-------|---------|
| **Python Not Installed** | Ensure Python is installed and added to `PATH`. |
| **Virtual Environment Creation Failed** | Delete the `venv` folder and rerun the activation script. |
| **Permission Issues on macOS/Linux** | Run `chmod +x activate_project.sh` before executing the script. |

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit **Pull Requests** or open **Issues** on the [GitHub repository](https://github.com/TamerOnLine/ollamalocal).

---

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

### 🔗 **Useful Links**
- [GitHub Repository](https://github.com/TamerOnLine/ollamalocal)
- [LangChain Ollama](https://python.langchain.com/docs/integrations/llms/ollama)

---

If you need any modifications, let me know! 🚀