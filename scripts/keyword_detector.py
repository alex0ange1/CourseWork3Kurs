import re

keyword_patterns = {
    "Определения, история развития и главные тренды ИИ": [
        r"\bискусственный интеллект\b", r"\bИИ\b", r"\bhistory of AI\b", r"\bтренды ИИ\b",
        r"\bопределения ИИ\b", r"\bразвитие ИИ\b", r"\bAI trends\b"
    ],
    "Процесс, стадии и методологии разработки решений на основе ИИ (Docker, Linux/Bash, Git)": [
        r"\bdocker\b", r"\blinux\b", r"\bbash\b", r"\bgit\b", r"\bметодология разработки\b",
        r"\bpipeline\b", r"\bCI/CD\b", r"\bdeployment\b", r"\bstages of development\b"
    ],
    "Статистические методы и первичный анализ данных": [
        r"\bстатистический анализ\b", r"\bстатистика\b", r"\bEDA\b", r"\bпервичный анализ данных\b",
        r"\bexploratory data analysis\b"
    ],
    "Оценка качества работы методов ИИ": [
        r"\bметрики качества\b", r"\baccuracy\b", r"\bprecision\b", r"\brecall\b",
        r"\bf1-score\b", r"\bvalidation\b", r"\bоценка модели\b"
    ],
    "Языки программирования и библиотеки (Python, C++)": [
        r"\bpython\b", r"\bc\+\+\b", r"\bnumpy\b", r"\bpandas\b", r"\btensorflow\b",
        r"\bpytorch\b", r"\bscikit-learn\b", r"\bбиблиотеки python\b", r"\bпрограммирование\b"
    ],
    "SQL базы данных (GreenPLum, Postgres, Oracle)": [
        r"\bsql\b", r"\bpostgresql\b", r"\bpostgres\b", r"\bgreenplum\b", r"\boracle\b",
        r"\bбазы данных sql\b", r"\bзапросы sql\b"
    ],
    "NoSQL базы данных (Cassandra, MongoDB, ElasticSearch, Neo4J, Hbase)": [
        r"\bnosql\b", r"\bcassandra\b", r"\bmongodb\b", r"\belasticsearch\b",
        r"\bneo4j\b", r"\bhbase\b", r"\bdocument db\b", r"\bgraph db\b"
    ],
    "Hadoop, SPARK, Hive": [
        r"\bhadoop\b", r"\bspark\b", r"\bhive\b", r"\bmapreduce\b", r"\bbig data\b",
        r"\bраспределенная обработка\b"
    ],
    "Качество и предобработка данных, подходы и инструменты": [
        r"\bпредобработка данных\b", r"\bdata cleaning\b", r"\bmissing values\b",
        r"\bnormalization\b", r"\bfeature engineering\b"
    ],
    "Работа с распределенной кластерной системой": [
        r"\bкластер\b", r"\bdistributed system\b", r"\bраспределенная система\b",
        r"\bkubernetes\b", r"\bcluster management\b"
    ],
    "Методы машинного обучения": [
        r"\bмашинное обучение\b", r"\bmachine learning\b", r"\bsupervised\b", r"\bunsupervised\b",
        r"\bregression\b", r"\bclassification\b"
    ],
    "Рекомендательные системы": [
        r"\bрекомендательные системы\b", r"\brecommendation system\b",
        r"\bcollaborative filtering\b", r"\bcontent-based filtering\b"
    ],
    "Методы оптимизации": [
        r"\bоптимизация\b", r"\bgradient descent\b", r"\bstochastic optimization\b",
        r"\bconvex optimization\b"
    ],
    "Основы глубокого обучения": [
        r"\bглубокое обучение\b", r"\bdeep learning\b", r"\bнейронные сети\b",
        r"\bneural networks\b", r"\bbackpropagation\b"
    ],
    "Анализ изображений и видео": [
        r"\bанализ изображений\b", r"\bcomputer vision\b", r"\bimage processing\b",
        r"\bvideo analysis\b", r"\bopencv\b"
    ],
    "Машинное обучение на больших данных": [
        r"\bbig data\b", r"\bdistributed ml\b", r"\bmachine learning at scale\b", r"\bspark ml\b"
    ],
    "Глубокое обучение для анализа естественного языка": [
        r"\bnlp\b", r"\bnatural language processing\b", r"\bbert\b", r"\btransformers\b",
        r"\blanguage models\b"
    ],
    "Обучение с подкреплением и глубокое обучение с подкреплением": [
        r"\breinforcement learning\b", r"\bобучение с подкреплением\b", r"\bdeep reinforcement learning\b",
        r"\bdqn\b", r"\bpolicy gradient\b"
    ],
    "Глубокое обучение для анализа и генерации изображений, видео": [
        r"\bgan\b", r"\bgenerative adversarial networks\b", r"\bimage generation\b",
        r"\bvideo generation\b", r"\bvae\b"
    ],
    "Анализ естественного языка": [
        r"\bnlp\b", r"\btext analysis\b", r"\bsentiment analysis\b", r"\btokenization\b",
        r"\bnamed entity recognition\b"
    ],
    "Информационный поиск": [
        r"\binformation retrieval\b", r"\bsearch engines\b", r"\btf-idf\b", r"\bbm25\b",
        r"\bпоисковые системы\b"
    ],
    "Массово параллельные вычисления для ускорения машинного обучения (GPU)": [
        r"\bgpu computing\b", r"\bcuda\b", r"\bparallel computing\b", r"\bmassively parallel\b",
        r"\btensor cores\b"
    ],
    "Потоковая обработка данных (data streaming, event processing)": [
        r"\bstreaming\b", r"\bdata streaming\b", r"\bkafka\b", r"\bevent processing\b",
        r"\bflink\b", r"\bspark streaming\b"
    ],
    "Массово параллельная обработка и анализ данных": [
        r"\bmassively parallel processing\b", r"\bmpp\b", r"\bdistributed computing\b",
        r"\bbig data analytics\b"
    ]
}

def check_competency_regex(text: str, competency: str) -> bool:
    patterns = keyword_patterns.get(competency, [])
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def check_all_competencies(text: str) -> dict:
    """
    Возвращает словарь {компетенция: True/False}, где True — компетенция найдена.
    """
    result = {}
    for comp in keyword_patterns.keys():
        result[comp] = check_competency_regex(text, comp)
    return result