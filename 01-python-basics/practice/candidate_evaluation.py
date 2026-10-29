def evaluate_candidate(name, experience, country, *skills, **details):
    name = name.strip().title()
    print(f"Evaluating candidate: {name}")

    country = country.strip().title()
    print(f"Country:   {country}")
    print(f"Experience: {experience} years")

    for key, value in details.items():
        print(f" Additional details {key}: {value}")

    for skill in skills:
        skill = skill.strip().lower()
        print(f"Skills: {skill}")

    if experience >= 5 and country == "Canada":
        skills = [skill.strip().lower() for skill in skills]
        if "python" in skills:
            print(f"{name} pass the initial screening.")
        else:
            print(f"{name} does not meet the criteria.")
