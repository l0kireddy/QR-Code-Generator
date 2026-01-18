# 📟 QR_Terminal_Master

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Web-orange.svg)
![Privacy](https://img.shields.io/badge/privacy-Client--Side%20Only-green.svg)

A high-definition, cyberpunk-styled QR Code generator capable of producing professional, brand-ready designs. Built with a strict **Terminal / Glassmorphism UI**, this tool runs entirely in the browser with **zero backend dependencies**.

![Screenshot of the Application](screenshot.png)
*(Note: Upload a screenshot of your interface here)*

## ✨ Key Features

### 🖥️ The Interface
* **Terminal Aesthetic:** Dark mode, monospace typography, and sharp edges.
* **Glassmorphism:** UI elements float on a "frosted glass" layer with light blur effects.
* **Toggle System:** Cleanly switch between "Standard" and "Custom" modes to keep the UI minimal.

### 🎨 Design Capabilities
* **3 Matrix Styles:** Standard (Square), Dotted (Circles), and Fluid (Rounded/Liquid).
* **Gradient Engine:** Create Linear (45°) or Radial gradients with unlimited color stops.
* **Corner Customization:** Style corner markers (squares vs. dots) independently from the main data pattern.
* **Brand Integration:** Upload and center your **Logo** automatically.
* **Backdrop Support:** Place custom images behind the QR code for transparent/artistic designs.

### ⚡ Performance & Privacy
* **100% Client-Side:** No API calls. No servers. No data leaves your device.
* **Offline Capable:** Works without an internet connection (if the library is cached/downloaded).
* **High-Res Export:** Generates **1000x1000px** PNGs suitable for print.

## 🚀 How to Run

Since this is a standalone frontend application, no installation (`npm`, `pip`, etc.) is required.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/qr-terminal-master.git](https://github.com/yourusername/qr-terminal-master.git)
    ```
2.  **Open the file:**
    Simply double-click `index.html` to open it in your web browser.

## 🛠️ Tech Stack

* **Core:** HTML5, CSS3 (Backdrop-filter, Flexbox)
* **Logic:** Vanilla JavaScript (ES6+)
* **Library:** [qr-code-styling](https://github.com/kozakdenys/qr-code-styling) (for rendering the canvas)

## 📂 Project Structure

``` text
/
├── index.html        # The entire application (Logic + UI)
├── README.md         # Documentation
└── screenshot.png    # (Optional) Preview image
```

## 🌐 Deployment

Since this is a static HTML/JS project, you can deploy it instantly for free.

### Option 1: GitHub Pages (Recommended)
1.  Push this code to a GitHub repository.
2.  Go to **Settings** > **Pages** in your repository menu.
3.  Under **Source**, select `Deploy from a branch`.
4.  Select `main` (or `master`) and click **Save**.
5.  Your site will be live at `https://your-username.github.io/repo-name/`.

### Option 2: Netlify (Drag & Drop)
1.  Log in to [Netlify](https://www.netlify.com/).
2.  Go to the "Sites" tab.
3.  Drag your project folder directly onto the browser window.
4.  Netlify will deploy it instantly and give you a live URL.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new matrix shapes or terminal themes, feel free to fork the repo.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

> **Note:** This tool uses `qr-code-styling` under the hood. All rendering happens locally in the browser.
>
> *Built with 🟢 and ☕ by [Your Name]*
