projects = [
    {
        "title": "SMP Performance Coach",
        "problem": "Manually tracking fitness data and writing coaching notes took 30+ minutes per day.",
        "solution": "Automated pipeline that trains a classifier on 28 days of data, predicts daily goal achievement, and generates a coaching message.",
        "tools": ["Python", "scikit-learn", "pandas", "FastAPI"],
        "result": "Prediction + coaching in under 2 seconds. Exports weekly JSON report.",
        "github": "github.com/rhoneyokeyo/smp-tracker",
        "type": "ML + API"
    },
    {
        "title": "Multi-Endpoint API Dashboard",
        "problem": "Three separate data sources with no unified view. Reporting was manual and inconsistent.",
        "solution": "Dashboard that fetches from three endpoints, processes each independently, and outputs a combined summary with protocol comparison.",
        "tools": ["Python", "requests", "pandas"],
        "result": "Single command produces a full multi-source report. Reduced prep time by 90%.",
        "github": "github.com/rhoneyokeyo/api-dashboard",
        "type": "Data Pipeline"
    },
    {
        "title": "Browser-Based AI Coach",
        "problem": "Clients needed a way to get coaching feedback without installing software.",
        "solution": "Client-side JavaScript tool. Prediction engine and coaching generator run entirely in the browser. No server required.",
        "tools": ["JavaScript", "DOM API", "Fetch API"],
        "result": "Zero setup for end users. Works on any device with a browser.",
        "github": "github.com/rhoneyokeyo/browser-coach",
        "type": "Web Tool"
    },
    {
        "title": "Data Analysis Report",
        "problem": "Clients needed a monthly breakdown fitness log with protocol comparison.",
        "solution": "28-day SMP Fitness Log Analysis. Weekly breakdown with protocol analysis.",
        "tools": ["Python", "Pandas", "NumPy"],
        "result": "Exports a weekly analysis report. Works on any browser enabled device.",
        "github": "github.com/rhoneyokeyo/data-analysis-report",
        "type": "ML + API"
    },
]

SEPARATOR = "=" * 64

print(SEPARATOR)
print(" DEVELOPER PORTFOLIO SUMMARY")
print(SEPARATOR)

for i, p in enumerate(projects, 1):
    print(f"\nProject {i}: {p['title']} [{p['type']}]")
    print(f" Problem: {p['problem']}")
    print(f" Solution: {p['solution']}")
    print(f" Tools: {','.join(p['tools'])}")
    print(f" Result: {p['result']}")
    print(f" Code: {p['github']}")

print()
print(SEPARATOR)
print(f" Total projects: {len(projects)}")

print(f" Tech stack: {(sorted(projects, key=lambda p: p["type"]))}")
print(SEPARATOR)
