def generate_report(skills, score, jobs):

    report = ""

    report += "RESUME ANALYSIS REPORT\n\n"

    report += f"Resume Score: {score}/100\n\n"

    report += "Detected Skills:\n"

    for skill in skills:
        report += f"• {skill}\n"

    report += "\nJob Matches:\n"

    for job, value in jobs.items():
        report += f"{job}: {value}%\n"

    return report