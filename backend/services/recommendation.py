def calculate_match(job, candidate):
    score = 0

    job_skills = [
        s.strip().lower()
        for s in (job.skills or "").split(",")
        if s.strip()
    ]

    candidate_skills = [
        s.strip().lower()
        for s in (candidate.skills or "").split(",")
        if s.strip()
    ]

    for skill in job_skills:
        if skill in candidate_skills:
            score += 20

    return score