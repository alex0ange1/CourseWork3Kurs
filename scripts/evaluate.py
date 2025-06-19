def evaluate_candidate(candidate_levels: dict, profession: str, professions_dict: dict) -> dict:

    required_skills = professions_dict.get(profession)
    if not required_skills:
        raise ValueError(f"Профессия {profession} не найдена в словаре.")

    total_required = 0
    total_matched = 0
    missing_skills = []

    for skill_name, required_level in required_skills.items():
        candidate_level = candidate_levels.get(skill_name, 0)

        total_required += required_level
        total_matched += min(candidate_level, required_level)

        if candidate_level < required_level:
            missing_skills.append({
                "name": skill_name,
                "required_level": required_level,
                "candidate_level": candidate_level
            })

    match_percent = (total_matched / total_required * 100) if total_required > 0 else 0.0

    return {
        "match_percent": match_percent,
        "missing_skills": missing_skills
    }


if __name__ == "__main__":

    professions_dict_example = {
        "Data Scientist": {
            "Определения, история развития и главные тренды ИИ": 1,
            "Процесс, стадии и методологии разработки решений на основе ИИ (Docker, Linux/Bash, Git)": 2,
            "Статистические методы и первичный анализ данных": 2,
        }
    }

    candidate_example = {
        "Определения, история развития и главные тренды ИИ": 0,
        "Процесс, стадии и методологии разработки решений на основе ИИ (Docker, Linux/Bash, Git)": 1,
        "Статистические методы и первичный анализ данных": 0,
    }

    result = evaluate_candidate(candidate_example, "Data Scientist", professions_dict_example)
    print(f"Процент соответствия: {result['match_percent']:.2f}%")
    print("Недостающие навыки:")
    for skill in result["missing_skills"]:
        print(f"- {skill['name']}: требуется {skill['required_level']}, есть {skill['candidate_level']}")
