def get_action_plan(career):
    plans = {
        "Data Scientist": [
            "✅ Learn Python, Statistics, and SQL",
            "📚 Take a Data Science certification (Coursera, Udemy, etc.)",
            "📊 Build projects: prediction models, analysis dashboards",
            "🏆 Create a Kaggle profile and participate in competitions"
        ],
        "Software Engineer": [
            "💻 Master Data Structures and Algorithms",
            "🌐 Learn web or mobile development frameworks",
            "🛠️ Build 2–3 real-world apps or open-source contributions",
            "🔍 Apply for internships at startups or tech firms"
        ],
        "Product Manager": [
            "🗣️ Develop strong communication and leadership skills",
            "📦 Understand product lifecycle and agile methodology",
            "🧰 Use tools like Jira, Notion, Figma",
            "👥 Learn basic tech concepts to collaborate with developers"
        ],
        "Teacher": [
            "📘 Gain expertise in your chosen subject",
            "🎓 Complete a B.Ed. or equivalent qualification",
            "📹 Build online teaching experience (YouTube, Udemy)",
            "🏫 Apply for private/public school positions"
        ],
        "Doctor": [
            "🎓 Complete MBBS or equivalent medical degree",
            "📄 Clear NEET/Medical entrance exams",
            "🏥 Do clinical internships",
            "🧪 Choose specialization and pursue MD or diploma"
        ]
    }
    return plans.get(career, [
        "🔍 Explore online resources about the career",
        "🤝 Talk to professionals or mentors in the field",
        "🧪 Start a small project or internship in this area"
    ])
