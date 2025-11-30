import re

STOPWORDS = {
    "a","an","the","and","or","but","if","is","am","are","was","were","be","been",
    "being","this","that","these","those","to","of","for","in","on","with","as",
    "by","about","at","from","it","its","into","than","then","so","too","very",
    "can","could","should","would","may","might","will","shall","do","does","did",
    "not","no","yes","your","you","we","our","they","their","them","he","she",
    "his","her","him","i","me","my","mine","let","us"
}

def clean_text(text):
    text = text.lower()
    cleaned = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if not cleaned:
        return set()
    words = cleaned.split()
    filtered = [w for w in words if w not in STOPWORDS]
    return set(filtered)

def jaccard_similarities(set1, set2):
    if len(set1) == 0 and len(set2) == 0:
        return 0.0
    intersection = set1 & set2
    union = set1 | set2
    jaccard_score = len(intersection)/len(union)
    percentage = round(jaccard_score*100,1)
    return percentage

def get_common_words(set1, set2):
    common = set1 & set2
    common_list = sorted(common)
    return common_list

def containment_score(student_set, source_set):
    if len(student_set) == 0:
        return 0.0
    common = student_set & source_set
    return round((len(common) / len(student_set)) * 100, 1)