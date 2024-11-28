import os
from datetime import datetime

# Define the courses and their details with additional metadata
courses = [
    {
        "code": "MTL102", 
        "name": "Differential Equations", 
        "professor": "Professor V. V. K. Srinivas Kumar", 
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonO2EtcDgOS6vP9l0osfXORs",
        "description": "Explore the fundamental techniques of solving differential equations, crucial for understanding complex mathematical and engineering problems.",
        "difficulty": "Intermediate",
        "tags": ["Mathematics", "Engineering", "Calculus"]
    },
    {
        "code": "CLP301", 
        "name": "Chemical Engineering Laboratory-I", 
        "professor": "Unknown", 
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonNvDId2qHiT2Mto2tIcVG-U",
        "description": "Hands-on experiments and practical techniques in chemical engineering processes.",
        "difficulty": "Advanced",
        "tags": ["Chemical Engineering", "Lab Work", "Practical Skills"]
    },
    {
        "code": "HUL261", 
        "name": "Introduction to Psychology", 
        "professor": "Yashpal Jogdand and Sumitava Mukherjee", 
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonPSY1su7N2vhLwRYylaWprU",
        "description": "An introduction to the scientific study of the mind and behavior.",
        "difficulty": "Beginner",
        "tags": ["Psychology", "Human Behavior", "Social Sciences"]
    },
    {
        "code": "MSL405", 
        "name": "Financial Management and Compliance for Startups", 
        "professor": "Shveta Singh", 
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonOXuhUjxSzR9gt-WnMS2pb1",
        "description": "Learn financial strategies and compliance essentials to build and manage startups effectively.",
        "difficulty": "Intermediate",
        "tags": ["Startups", "Finance", "Management"]
    },
    {
        "code": "PYL101",
        "name": "Physics-I",
        "professor": "Professor B. Satpati",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonN8JpDPQReNlUskDWomvpba",
        "description": "An in-depth study of mechanics, thermodynamics, and introductory physics concepts.",
        "difficulty": "Intermediate",
        "tags": ["Physics", "Mechanics", "Thermodynamics"]
    },
    {
        "code": "BEL101",
        "name": "Biochemistry",
        "professor": "Professor Yogendra Singh",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonNeSWDLytX7Gaed15E54-wJ",
        "description": "Explore the chemical processes within and relating to living organisms.",
        "difficulty": "Intermediate",
        "tags": ["Biology", "Biochemistry", "Life Sciences"]
    },
    {
        "code": "CEL201",
        "name": "Environmental Engineering",
        "professor": "Professor S. Asolekar",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonPKsVzkINpjROdR6rRvcnNp",
        "description": "Understand the principles and practices of environmental engineering, focusing on sustainability.",
        "difficulty": "Intermediate",
        "tags": ["Environmental Science", "Engineering", "Sustainability"]
    },
    {
        "code": "HUL201",
        "name": "Humanities and Social Sciences Elective",
        "professor": "Various Instructors",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonPVrdNiYg7oxHgUlYr6f8KP",
        "description": "An elective course designed to provide insights into social sciences and humanities.",
        "difficulty": "Beginner",
        "tags": ["Social Sciences", "Humanities", "Electives"]
    },
    {
        "code": "CSL101",
        "name": "Introduction to Computing",
        "professor": "Professor Subhashis Banerjee",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonNdA_5cxek32bfRxhsjXKVL",
        "description": "Learn the basics of programming and computational thinking.",
        "difficulty": "Beginner",
        "tags": ["Computer Science", "Programming", "Algorithms"]
    },
    {
        "code": "MEL123",
        "name": "Engineering Drawing",
        "professor": "Professor A. Kumar",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonNzSWcd_gXWt-tC3TyI6riH",
        "description": "Master the fundamentals of engineering graphics and CAD tools.",
        "difficulty": "Beginner",
        "tags": ["Engineering", "Graphics", "Design"]
    },
    {
        "code": "EEL101",
        "name": "Basic Electrical Engineering",
        "professor": "Professor R. Sharma",
        "playlist_url": "https://www.youtube.com/playlist?list=PLSIUNf-YNonP-VIt3rfFzH2HQNhboYM7B",
        "description": "An introduction to the fundamental concepts of electrical engineering.",
        "difficulty": "Intermediate",
        "tags": ["Electrical Engineering", "Circuits", "Electronics"]
    }
]


# HTML template for course pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course_code} - {course_name} | IIT Delhi Courses</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script src="script.js" defer></script>
    <meta name="description" content="Course page for {course_code} - {course_name} at IIT Delhi">
    <meta name="keywords" content="{tags}">
</head>
<body>
    <div class="page-container">
        <header class="header">
            <div class="header-content">
                <div class="course-badge">
                    <span class="course-code">{course_code}</span>
                </div>
                <div class="header-text">
                    <h1>{course_name}</h1>
                    <p class="professor">
                        <i class="fas fa-chalkboard-teacher"></i> {professor}
                    </p>
                </div>
            </div>
        </header>

        <main class="content">
            <div class="course-details">
                <section class="course-intro">
                    <h2>Course Overview</h2>
                    <div class="course-meta">
                        <span class="difficulty">{difficulty}</span>
                        <div class="tags">
                            {tag_html}
                        </div>
                    </div>
                    <p>{description}</p>
                </section>

                <section class="course-playlist">
                    <h2>Course Playlist</h2>
                    <div class="playlist-container">
                        <div class="playlist-overlay">
                            <button class="play-btn" data-url="{playlist_url}">
                                <i class="fas fa-play"></i> Start Learning
                            </button>
                        </div>
                        <iframe 
                            width="100%" 
                            height="450" 
                            src="{playlist_url}" 
                            title="{course_name} Playlist" 
                            frameborder="0" 
                            allow="autoplay; encrypted-media" 
                            allowfullscreen
                            class="responsive-iframe"
                        ></iframe>
                    </div>
                </section>
            </div>
        </main>

        <footer class="footer">
            <div class="footer-content">
                <p>&copy; {current_year} <a href="https://rtnesharma.in">rtnesharma.in</a>. All Rights Reserved.</p>
                <div class="social-links">
                    <a href="https://github.com/rksiitd1" target="_blank"><i class="fab fa-github"></i></a>
                    <a href="https://www.linkedin.com/in/ratnesh-sharma" target="_blank"><i class="fab fa-linkedin"></i></a>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>"""

# Directory where HTML files are stored
output_dir = "C:/Users/RATNESH/OneDrive/Documents/GitHub/rksiitd1.github.io/infinity/c"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through courses and create/update HTML files
for course in courses:
    # Generate tag HTML
    tag_html = ' '.join([f'<span class="tag">{tag}</span>' for tag in course.get('tags', [])])
    
    # Create HTML content
    html_content = template.format(
        course_code=course['code'],
        course_name=course['name'],
        professor=course['professor'] or "Instructor: Not Specified",
        playlist_url=course['playlist_url'],
        description=course.get('description', 'No description available.'),
        difficulty=course.get('difficulty', 'Not Specified'),
        tag_html=tag_html,
        current_year=datetime.now().year
    )
    
    # Write HTML file
    file_path = os.path.join(output_dir, f"{course['code']}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

print("All HTML files updated successfully!")
