<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>get-meta-pdf
</h1>
<h3>◦ Unlock PDF magic with meta power!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/Gael-Pitras/get-meta-pdf.git?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/Gael-Pitras/get-meta-pdf.git?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/Gael-Pitras/get-meta-pdf.git?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/Gael-Pitras/get-meta-pdf.git?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running get-meta-pdf](#-running-get-meta-pdf)
    - [🧪 Tests](#-tests)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The core functionality of this project is to allow users to select a PDF file and retrieve its properties and metadata. The purpose of the project is to provide a convenient way for users to access and display important information about PDF files. This value proposition is achieved by leveraging the PyPDF2 library for PDF processing and integrating it with the PyQt5 framework for creating a user-friendly graphical interface.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a simple architecture leveraging PyPDF2 and PyQt5 libraries. It consists of a single file, `app.py`, which handles PDF file selection, metadata extraction, and GUI rendering. The code is organized using functions and classes, providing a modular structure. Overall, the architecture is straightforward and easy to understand. |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. While there is a brief description of the file `app.py`, the code within functions and methods is not well-documented. Proper documentation would improve code maintainability and help others understand the implementation details. Documentation should be added for the methods and classes explaining their purpose and functionality. |
| 🔗 | **Dependencies**   | The codebase relies on external dependencies, PyPDF2 and PyQt5, for PDF processing and GUI respectively. These libraries are popular and well-maintained, ensuring reliable functionality. Ensure that the version of these dependencies is compatible with the codebase. |
| 🧩 | **Modularity**     | The codebase demonstrates modularity by organizing functionality into separate functions and classes. This allows for better code organization and reusability. Further improvement could be achieved by separating concerns into distinct modules and applying a more structured approach, like using separate modules for GUI and PDF processing functionalities. |
| 🧪 | **Testing**        | The codebase lacks any tests, making it difficult to ensure its correctness and reliability. Implementing unit tests using a suitable testing framework like pytest would help detect and prevent bugs, improve code quality, and support future changes. |
| ⚡️ | **Performance**    | As performance largely depends on the capabilities of the underlying libraries, PyPDF2 and PyQt5, the codebase should inherit their respective performance characteristics. However, in terms of file selection and metadata extraction, the current implementation should handle reasonable-sized PDFs efficiently. Performance optimizations could be added for large files or batch processing scenarios. Additionally, profiling tools can help identify any bottlenecks. |
| 🔐 | **Security**       | The codebase does not incorporate any specific security measures. It's essential to validate input file formats rigorously and handle exceptions gracefully. Additionally, sensitive data should be handled securely, considering aspects like encryption and access control. |
| 🔀 | **Version Control**| Git is appropriately utilized for version control, with the codebase stored in a public GitHub repository. Key Git features such as version history, branches, and merge requests can be utilized effectively to track changes, collaborate, and maintain code quality. Employing proper branching strategies and utilizing Git hooks for pre-commit and pre-push checks would be beneficial. |
| 🔌 | **Integrations**   | The codebase interacts solely with the user through GUI elements for file selection and displaying metadata. No external integrations with other systems or services are visible in the current codebase. However, as an added functionality, the codebase could support integrations with cloud storage services for file upload/download and an API for remote metadata extraction. |
| 📶

---


## 📂 Repository Structure

```sh
└── get-meta-pdf/
    ├── README.md
    └── app.py
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                       | Summary                                                                                                                                                                                                      |
| ---                                                                        | ---                                                                                                                                                                                                          |
| [app.py](https://github.com/Gael-Pitras/get-meta-pdf.git/blob/main/app.py) | This code allows the user to select a PDF file, retrieve its properties and metadata, and display them in a table. It uses the PyPDF2 library for PDF processing and PyQt5 for the graphical user interface. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the get-meta-pdf repository:
```sh
git clone https://github.com/Gael-Pitras/get-meta-pdf.git
```

2. Change to the project directory:
```sh
cd get-meta-pdf
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running get-meta-pdf

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```




---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  LICENSE-TYPE` License. See the [LICENSE-Type](LICENSE) file for additional info.

---

## 👏 Acknowledgments

`- ℹ️ List any resources, contributors, inspiration, etc.`

---
