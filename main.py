import os
from modules.core import clean_text, jaccard_similarities, get_common_words, containment_score
from modules.extractor import extracted_text
from modules.web_extractor import extract_web_text

Documents="documents"

def main():
    print("="*55)
    print("\t *Advanced PLAGARISM CHECKER\n\t JACCARD SIMILARITIES")
    print("\t Local Files • Wikipedia • Any Web URL")
    print("="*55)
    print()
    print("Choose mode:")
    print("1. Compare two local files")
    print("2. Compare local file with Wikipedia")
    print("3. Compare local file with Web URL")
    choice = input("Enter 1 | 2 | 3 : ").strip()

    if choice == '1':
        valid_extension = (".txt", ".pdf", ".docx")
        try:
            all_files = [f for f in os.listdir(Documents) if f.lower().endswith(valid_extension)]
            if not all_files:
                print("No supported files found in 'documents' folder!")
                return
        except FileNotFoundError:
            print("Folder 'documents' not found! Create it and put files inside.")
            return
        print("Avaliable local files in 'documents' folder")
        print()
        for i, file in enumerate(all_files, 1):
            print(f"\t{i}. {file}")
        print()
        while True:
            file1 = input("Enter first file name (with .txt): ").strip()
            if file1 in all_files:
                break
            print("File not found! Choose from the list above.")
        while True:
            file2 = input("Enter second file name (with .txt): ").strip()
            if file2 in all_files and file2!=file1:
                break
            print("File not found or same as first! Try again.")
        path1 = os.path.join(Documents, file1)
        path2 = os.path.join(Documents, file2)
        print("\nReading local files...")
        text1 = extracted_text(path1)
        text2 = extracted_text(path2)
        source_name1 = file1
        source_name2 = file2

    elif choice in ['2', '3']:
        valid_extension = (".txt", ".pdf", ".docx")
        try:
            all_files = [f for f in os.listdir(Documents) if f.lower().endswith(valid_extension)]
            if not all_files:
                print("No supported files found in 'documents' folder!")
                return
        except FileNotFoundError:
            print("No supported file found in 'documents' folder!")
            return
        print("Avaliable local files in 'documents' folder:")
        for i, file in enumerate(all_files, 1):
            print(f"\t{i}. {file}")
        print()
        while True:
            file1 = input("Enter first file name (with .txt): ").strip()
            if file1 in all_files:
                break
            print("File not found! Choose from the list above.")
        path1 = os.path.join(Documents, file1)
        print("\nReading local files...\n")
        text1 = extracted_text(path1)
        if choice == "2":
            web_source = input("Enter Wikipedia topic (e.g., 'Plagiarism'): ")
        else:
            web_source = input ("Enter full Web URL (e.g., https://github.com/p-varun): ")
        print(f"\nFetching web content from: {web_source}\n")
        text2 = extract_web_text(web_source)
        source_name1 = file1
        source_name2 = "Web: " + web_source[:50] + "..." if len(web_source) > 50 else web_source

    else:
        print("Invalid choice! Run again.")
        return
    
    if not text1 or not text2:
        print("One or both sources are empty or could not be read.")
        return
    set1 = clean_text(text1)
    set2 = clean_text(text2)

    if choice == 1:
        score = jaccard_similarities(set1, set2)
    else:
        containment = containment_score(set1, set2)
        reverse_containment = containment_score(set2, set1)
        score = max(containment, reverse_containment)

    common_words = get_common_words(set1, set2)
    print("\n" + "="*55)
    print(f"RESULT: {source_name1} vs {source_name2}")
    print("="*55)
    if choice == 1:
        print(f"\t-----Plagiarism Score: {score}%-----")
    else:
        print(f"\tPlagiarism from WEB: {score}")
        print("\t(Percentage of your text found in the source)")
    print()

    if score > 80:
        print("\tEXTREME SIMILARITY DETECTED!")
    elif score > 60:
        print("\tHIGH SIMILARITY - Possible plagiarism")
    elif score > 40:
        print("\tModerate similarity")
    else:
        print("\tlow similarity - Probably original work")
    print(f"\nCommon words found: {len(common_words)}")
    
    if common_words:
        print("First 20 common words:", ", ".join(common_words[:20]))
        if len(common_words) > 20:
            print("   ... and more")
    print("\n=====================Done!====================\n")
    print("HINT: IF WHILE USING WIKIPEDIA DOES GIVE YOU AN ERROR THEN PLACE THE WIKIPEDIA URL(with https://) AS SECOND SOURCE.\n")
if __name__ == "__main__":
    main()