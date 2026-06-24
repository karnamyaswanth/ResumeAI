def get_resume_suggestions(skills):

    suggestions = []

    required = {

        "python": "Add Python projects and examples",

        "sql": "Learn SQL joins and analytics",

        "machine learning": "Build ML portfolio projects",

        "streamlit": "Create dashboard applications",

        "pandas": "Practice data analysis workflows"

    }

    lower_skills = [
        s.lower()
        for s in skills
    ]

    for skill in required:

        if skill not in lower_skills:

            suggestions.append(
                required[skill]
            )

    return suggestions