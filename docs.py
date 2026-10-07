from pathlib import Path


documents = {
    "cricket.txt": """
Cricket is a popular sport played between two teams.
Fast bowlers are important because they can generate high speed.
Bowlers try to take wickets while batsmen try to score runs.
""",

    "python.txt": """
Python is a popular programming language.
Python is used for automation, web development, data science,
machine learning, artificial intelligence, and scripting.
""",

    "machine_learning.txt": """
Machine learning allows computers to learn patterns from data.
Supervised learning uses labeled data.
Classification and regression are common machine learning tasks.
""",

    "artificial_intelligence.txt": """
Artificial intelligence allows machines to perform tasks
that normally require human intelligence.
AI includes machine learning, deep learning, and natural language processing.
""",

    "football.txt": """
Football is a team sport played around the world.
Players try to score goals by moving the ball toward the opponent goal.
""",

    "basketball.txt": """
Basketball is a fast team sport.
Players score points by throwing the ball through the basket.
""",

    "tennis.txt": """
Tennis is played between two players or two teams.
Players use a racket to hit a ball over the net.
""",

    "programming.txt": """
Programming is the process of creating instructions for computers.
Programming languages include Python, Java, C++, and JavaScript.
""",

    "databases.txt": """
Databases store and organize information.
Database systems allow applications to create, read, update, and delete data.
""",

    "sql.txt": """
SQL is used to work with relational databases.
SQL allows developers to query, insert, update, and delete records.
""",

    "web_development.txt": """
Web development involves building websites and web applications.
HTML, CSS, JavaScript, and backend technologies are commonly used.
""",

    "cloud_computing.txt": """
Cloud computing provides computing resources over the internet.
Cloud services include storage, databases, networking, and virtual machines.
""",

    "cybersecurity.txt": """
Cybersecurity protects computers, networks, applications, and data.
Security includes authentication, encryption, monitoring, and access control.
""",

    "data_science.txt": """
Data science combines statistics, programming, mathematics, and domain knowledge.
Data scientists analyze data to discover useful patterns.
""",

    "pandas.txt": """
Pandas is a Python library used for data analysis.
DataFrames allow developers to store, clean, transform, and analyze structured data.
""",

    "numpy.txt": """
NumPy is a Python library for numerical computing.
NumPy provides arrays and mathematical operations for scientific computing.
""",

    "git.txt": """
Git is a version control system.
Developers use Git to track changes in source code and collaborate on projects.
""",

    "github.txt": """
GitHub is a platform for hosting Git repositories.
Developers use GitHub for collaboration, pull requests, issues, and project management.
""",

    "api.txt": """
An API allows different software systems to communicate.
APIs commonly exchange data using formats such as JSON.
""",

    "rest_api.txt": """
REST APIs use HTTP methods such as GET, POST, PUT, PATCH, and DELETE.
REST services commonly return JSON responses.
""",

    "neural_networks.txt": """
Neural networks are machine learning models inspired by biological neurons.
They are widely used for classification, prediction, and pattern recognition.
""",

    "deep_learning.txt": """
Deep learning uses neural networks with multiple layers.
Deep learning is widely used for computer vision, speech recognition, and language tasks.
""",

    "natural_language_processing.txt": """
Natural language processing allows computers to work with human language.
NLP is used for translation, sentiment analysis, search, and chatbots.
""",

    "transformers.txt": """
Transformers are neural network architectures used extensively in natural language processing.
They use attention mechanisms to understand relationships between words.
""",

    "rag.txt": """
Retrieval augmented generation combines document retrieval with language models.
RAG retrieves relevant information before generating an answer.
""",
}


docs_path = Path("docs")
docs_path.mkdir(exist_ok=True)


for filename, content in documents.items():
    file_path = docs_path / filename

    file_path.write_text(
        content.strip(),
        encoding="utf-8",
    )


print(f"Created {len(documents)} documents.")