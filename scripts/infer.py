import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from keyword_detector import check_all_competencies  # твой регулярный детектор
from evaluate import evaluate_candidate  # функция оценки из evaluate.py

# === Параметры ===
MODEL_PATH = "~/Desktop/CourseWork3Kurs/data/models/rubert-competency"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(DEVICE)
model.eval()

competencies = [
    "Определения, история развития и главные тренды ИИ",
    "Процесс, стадии и методологии разработки решений на основе ИИ (Docker, Linux/Bash, Git)",
    "Статистические методы и первичный анализ данных",
    "Оценка качества работы методов ИИ",
    "Языки программирования и библиотеки (Python, C++)",
    "SQL базы данных (GreenPLum, Postgres, Oracle)",
    "NoSQL базы данных (Cassandra, MongoDB, ElasticSearch, Neo4J, Hbase)",
    "Hadoop, SPARK, Hive",
    "Качество и предобработка данных, подходы и инструменты",
    "Работа с распределенной кластерной системой",
    "Методы машинного обучения",
    "Рекомендательные системы",
    "Методы оптимизации",
    "Основы глубокого обучения",
    "Анализ изображений и видео",
    "Машинное обучение на больших данных",
    "Глубокое обучение для анализа естественного языка",
    "Обучение с подкреплением и глубокое обучение с подкреплением",
    "Глубокое обучение для анализа и генерации изображений, видео",
    "Анализ естественного языка",
    "Информационный поиск",
    "Массово параллельные вычисления для ускорения машинного обучения (GPU)",
    "Потоковая обработка данных (data streaming, event processing)",
    "Массово параллельная обработка и анализ данных"
]

from profession_matrix import professions_dict

def predict_competency_levels(resume_text: str) -> dict:
    keyword_matches = check_all_competencies(resume_text)
    results = {}

    for competency in competencies:
        if not keyword_matches.get(competency, False):
            results[competency] = 0
            continue

        input_text = f"{competency}. {resume_text}"
        tokens = tokenizer.encode(input_text, add_special_tokens=True)
        block_size = 512
        blocks = [tokens[i:i+block_size] for i in range(0, len(tokens), block_size)]

        predicted_levels = []

        for block in blocks:
            block_tensor = torch.tensor([block]).to(DEVICE)

            with torch.no_grad():
                outputs = model(block_tensor)
                logits = outputs.logits
                predicted_level = torch.argmax(logits, dim=-1).item()
                predicted_levels.append(predicted_level)

        results[competency] = max(predicted_levels)

    return results

if __name__ == "__main__":
    resume_text = """ 
    
Разрабатывал и обучал модели машинного обучения с использованием Python, Scikit-learn и Pandas, развёртывая решения в Docker-среде и применяя Git для контроля версий.

    """

    candidate_levels = predict_competency_levels(resume_text)

    # Например, для профессии "Data Scientist"
    profession_name = "Data Scientist"

    evaluation_result = evaluate_candidate(candidate_levels, profession_name, professions_dict)

    print(f"Профессия: {profession_name}")
    print(f"Процент соответствия: {evaluation_result['match_percent']:.2f}%")
    found_skills = {k: v for k, v in candidate_levels.items() if v > 0}
    print(f"Найденные компетенции:")
    for skill, level in found_skills.items():
        print(f" - {skill}: уровень {level}")
    print("Недостающие компетенции:")
    for skill in evaluation_result["missing_skills"]:
        print(f" - {skill['name']}: требуется уровень {skill['required_level']}, найден уровень {skill['candidate_level']}")

