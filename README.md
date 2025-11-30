# *Advanced Plagiarism Checker (Jaccard Similarity)

A simple yet powerful command-line plagiarism detection tool that compares a student document against:

Another local file
A Wikipedia article
Any public web page (URL)

It uses Jaccard similarity on cleaned word sets (stop-words removed) and provides a clear percentage score plus common-word analysis.

## ✨Features

Supports .txt, .pdf, and .docx files
Compare two local documents
Check against Wikipedia articles (by title)
Check against any public webpage (full URL scraping)
Stop-word removal & text normalization
Jaccard similarity for pairwise comparison
Containment score when checking against web sources (shows how much of your text appears in the source)
Color-coded plagiarism alerts (Extreme / High / Moderate / Low)
Displays first 20 common words

---

## How to Run

1. How to Clone this repo?
    * Make sure you have git, VS Code downloaded
    * Open VS code select any new folder
    * Select Terminal->New Terminal->pass
    ```
        git clone https://github.com/P-VARUN/PLAGIARISM-CHECKER
    ```
    that code in Terminal.
2. `pip install -r requirements.txt`

## How to Use

Create a folder named ```documents``` in the same directory as main.py
Place the files you want to check inside the documents folder
Run the program:

Choose one of the three modes:
1 → Compare two local files
2 → Compare local file vs Wikipedia article
3 → Compare local file vs any web URL

Follow the prompts. Results with similarity percentage and common words will be displayed instantly.

---

## Tips & Tricks

For Wikipedia: you can type just the title (Quantum Mechanics) or paste the full URL.
If Wikipedia gives a disambiguation error, try the exact page title or use the full URL in mode 3.
The tool ignores common stop-words (a, the, and, of, etc.) to focus on meaningful content.
Works completely offline for local file comparisons.


### Limitations

Does not detect paraphrased plagiarism perfectly (only exact/shared wording).
Web scraping may be blocked on some sites with heavy anti-bot protection.
No synonym replacement or semantic analysis (pure set-based Jaccard).

* This project is ```under active development```. Plagiarism scores may vary slightly.
* The system achieves 60-70% accuracy when checking against web results.
* Offline file comparison is robust, though minor inconsistencies may still occur.

Feel free to Contact me for new ideas you have in this project.


## License
MIT License - feel free to use, modify, and distribute.

Made espically for STUDENTS.

Made with ❤️ for academic integrity.

## 🔎Contact Info
Contact me if any errors faced, or doubts in the project: https://discord.gg/s4qsdWS5S2