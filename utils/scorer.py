def extract_skills(text):

    skill_db = [

        "python",
        "sql",
        "machine learning",
        "streamlit",
        "pandas",
        "numpy",
        "power bi",
        "excel",
        "data analysis",
        "deep learning",
        "scikit-learn"
    ]

    found = []

    text = text.lower()

    for skill in skill_db:

        if skill in text:
            found.append(skill)

    return found


def calculate_score(skills):

    total = 10

    score = min(
        (len(skills) / total) * 100,
        100
    )

    return round(score)