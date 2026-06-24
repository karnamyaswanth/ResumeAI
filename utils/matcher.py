JOB_SKILLS = {

    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "Excel"
    ],

    "Python Developer": [
        "Python",
        "Streamlit",
        "SQL"
    ],

    "ML Engineer": [
        "Python",
        "Machine Learning",
        "Scikit-Learn"
    ]

}


def match_jobs(skills):

    results = {}

    for job in JOB_SKILLS:

        required = JOB_SKILLS[job]

        matched = 0

        for skill in skills:

            if skill in required:
                matched += 1

        results[job] = round(
            matched /
            len(required)
            * 100
        )

    return results


def missing_skills(skills):

    required = [
        "Python",
        "SQL",
        "Machine Learning",
        "Streamlit",
        "Pandas"
    ]

    missing = []

    for skill in required:

        if skill not in skills:
            missing.append(skill)

    return missing