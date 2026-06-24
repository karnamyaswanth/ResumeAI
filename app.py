import streamlit as st
import plotly.express as px

from utils.parser import extract_text
from utils.scorer import (
    extract_skills,
    calculate_score
)

from utils.matcher import (
    match_jobs,
    missing_skills
)

from utils.report import (
    generate_report
)

from utils.suggestions import (
    get_resume_suggestions
)


# ---------------- PAGE ----------------

st.set_page_config(
    page_title="ResumeAI",
    page_icon="📄",
    layout="wide"
)

st.title(
    "📄 ResumeAI – AI Resume Analyzer"
)


# ---------------- UPLOAD ----------------

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)


# ---------------- PROCESS ----------------

if uploaded:

    resume_text = extract_text(
        uploaded
    )

    skills = extract_skills(
        resume_text
    )

    score = calculate_score(
        skills
    )

    jobs = match_jobs(
        skills
    )

    missing = missing_skills(
        skills
    )

    suggestions = get_resume_suggestions(
        skills
    )

    report = generate_report(
        skills,
        score,
        jobs
    )

    # SUCCESS

    st.success(
        "Resume Uploaded Successfully!"
    )

    # RESUME

    st.subheader(
        "📄 Extracted Resume"
    )

    st.text_area(
        "",
        resume_text,
        height=250
    )

    # SCORE

    st.subheader(
        "🎯 Resume Score"
    )

    st.metric(
        "Score",
        f"{score}/100"
    )

    st.progress(
        score / 100
    )

    # ATS

    if score >= 85:

        st.success(
            "🟢 ATS Friendly Resume"
        )

    elif score >= 60:

        st.info(
            "🟡 Moderate ATS Match"
        )

    else:

        st.error(
            "🔴 Low ATS Compatibility"
        )

    # SKILLS

    st.subheader(
        "🧠 Detected Skills"
    )

    if skills:

        st.write(
            ", ".join(skills)
        )

        chart = px.bar(
            x=skills,
            y=[1] * len(skills)
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

    else:

        st.warning(
            "No skills detected"
        )

    # JOBS

    st.subheader(
        "💼 Recommended Roles"
    )

    for job, value in jobs.items():

        st.write(
            f"✅ {job}: {value}%"
        )

    job_chart = px.bar(
        x=list(jobs.keys()),
        y=list(jobs.values())
    )

    st.plotly_chart(
        job_chart,
        use_container_width=True
    )

    # MISSING

    st.subheader(
        "📌 Missing Skills"
    )

    if missing:

        for item in missing:

            st.write(
                f"❌ {item}"
            )

    else:

        st.success(
            "All important skills detected"
        )

    # AI

    st.subheader(
        "🧠 AI Resume Suggestions"
    )

    if suggestions:

        for tip in suggestions:

            st.info(
                tip
            )

    else:

        st.success(
            "Excellent profile improvements detected"
        )

    # REPORT

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="resume_report.txt"
    )