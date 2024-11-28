import os

# Data for the courses
courses = [
    ("MTL102", "Differential Equations", "Professor V. V. K. Srinivas Kumar", "https://www.youtube.com/playlist?list=PLSIUNf-YNonO2EtcDgOS6vP9l0osfXORs"),
    ("CLP301", "Chemical Engineering Laboratory-I", "Unknown", "https://www.youtube.com/playlist?list=PLSIUNf-YNonNvDId2qHiT2Mto2tIcVG-U"),
    ("HUL261", "Introduction to Psychology", "Yashpal Jogdand and Sumitava Mukherjee", "https://www.youtube.com/playlist?list=PLSIUNf-YNonPSY1su7N2vhLwRYylaWprU"),
    ("MSL405", "Financial Management and Compliance for Startups", "Shveta Singh", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOXuhUjxSzR9gt-WnMS2pb1"),
    ("MLL100", "Introduction to Materials Science and Engineering", "Rajesh Prasad", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMY41hwJA8xsX4y0odNJwTH"),
    ("BBL133", "Mass and Energy Balances in Biochemical Engineering", "Sunil Nath", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOcjwegnuFA68-iNEzrayhL"),
    ("CLL261", "Process Dynamics and Control", "Hariprasad Kodamana", "https://www.youtube.com/playlist?list=PLSIUNf-YNonP3rCuBCj0h3pxf4Q_emVWK"),
    ("CVL100", "Environmental Science", "Gazala Habib", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMK57aaDC7zD6VWCLVb2YIT"),
    ("CLL251", "Heat Transfer", "Manojkumar Charandas Remteke", "https://www.youtube.com/playlist?list=PLSIUNf-YNonNqG2O2LWp0N1bfRda4LMLn"),
    ("HUL256", "Critical Thinking", "Arudra Burra", "https://www.youtube.com/playlist?list=PLSIUNf-YNonODx1wr1hy-FkahpO98zSHK"),
    ("SBL704", "Virology", "Vivekanandan Perumal", "https://www.youtube.com/playlist?list=PLSIUNf-YNonPuU4taAKKJUioY3Ijupypw"),
    ("SBL702", "System Biology", "James Gomes", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMOVbWhGglTtMHINWg5uyBK"),
    ("BBL131P", "Labs in Biochemistry", "Prashant Mishra", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMf5i97x8iqGzh2eH_mLvqq"),
    ("BBL433B", "Labs on Enzyme Science and Engineering", "Dr. K. J. Mukherjee", "https://www.youtube.com/playlist?list=PLSIUNf-YNonNX14-DKk9GPNt_XQOuOvc7"),
    ("CLL252", "Mass Transfer", "Ashok N Bhaskarwar", "https://www.youtube.com/playlist?list=PLSIUNf-YNonNibPXcfzsC4iJQI71Qmj0u"),
    ("BBL434", "Bioinformatics", "Ishaan Gupta", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOX_BUfGYTN4dwWiglljyf0"),
    ("BBL432", "Fluid Solid Systems", "Sunil Nath", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMZCLnzBjhBpUo0XUVv9f36"),
    ("BBL733", "Recombinant DNA Technology", "Ritu Kulshreshtha", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMxoPGbahliCAvhA10qwcEg"),
    ("BBL341", "Environmental Biotechnology", "Saroj Mishra", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOo3EVuACaIEsdOj_SMbNUn"),
    ("BBL433", "Enzyme Science and Engineering", "Dr. Krishna Jyoti Mukherjee", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMze2MPl5E7wok1626JTMfA"),
    ("BBL131", "Biochemistry", "Prashant Mishra", "https://www.youtube.com/playlist?list=PLSIUNf-YNonPcGRZiABiZHWO4PlwpnhOm"),
    ("BBL132", "General Microbiology", "Shilpi Sharma", "https://www.youtube.com/playlist?list=PLSIUNf-YNonNi3sxMi31_7AkJc4sNNtyD"),
    ("BBL431", "Bioprocess Technology", "Shaikh Ziauddin Ahammad", "https://www.youtube.com/playlist?list=PLSIUNf-YNonPjZsgnGNV_sWr0RPdNkOuz"),
    ("SBL726", "Molecular Motors", "Anita Roy", "https://www.youtube.com/playlist?list=PLSIUNf-YNonMNkFpMq75BMgNny4kQdZgf"),
    ("BBL331", "Bioprocess Engineering", "Atul Narang", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOXRguTR8o39VBMbOcX7uWU"),
    ("MSL802", "Intellectual Property Rights Management", "S.K. Jain", "https://www.youtube.com/playlist?list=PLSIUNf-YNonOo853OuJ5t9xmFtspORxO"),
    ("BBL231", "Molecular Biology and Genetics", "Dr. Preeti Srivastava", "https://www.youtube.com/playlist?list=PLSIUNf-YNonME8BsCeC7BISUyv5ExzxfK")
]

# Ensure the output directory exists
os.makedirs("c01", exist_ok=True)

# Generate HTML files
for course in courses:
    course_code, course_name, instructor, playlist_link = course
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course_code} - {course_name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #FF6B9E;
            --secondary-color: #7158E2;
            --background-color: #FFF2F8;
            --text-color: #333;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-15px); }}
            100% {{ transform: translateY(0px); }}
        }}

        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}

        @keyframes subtle-background {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        @keyframes slide-in {{
            from {{ 
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{ 
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        body {{
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(
                -45deg, 
                #FF6B9E, 
                #7158E2, 
                #FFC2D1, 
                #A0E7E5
            );
            background-size: 400% 400%;
            animation: subtle-background 15s ease infinite;
            color: var(--text-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }}

        .course-card {{
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(113, 88, 226, 0.2);
            padding: 40px;
            max-width: 500px;
            width: 100%;
            text-align: center;
            position: relative;
            overflow: hidden;
            animation: float 5s ease-in-out infinite, slide-in 1s ease-out;
            transform-style: preserve-3d;
        }}

        .course-card::before {{
            content: '✨';
            position: absolute;
            top: -30px;
            left: -30px;
            font-size: 50px;
            opacity: 0.3;
            transform: rotate(-15deg);
        }}

        .course-card::after {{
            content: '🌟';
            position: absolute;
            bottom: -30px;
            right: -30px;
            font-size: 50px;
            opacity: 0.3;
            transform: rotate(15deg);
        }}

        .course-header {{
            margin-bottom: 20px;
            opacity: 0;
            animation: slide-in 0.8s ease-out forwards;
            animation-delay: 0.2s;
        }}

        .course-code {{
            color: var(--secondary-color);
            font-size: 1.2rem;
            margin-bottom: 10px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        .course-title {{
            font-size: 2rem;
            font-weight: 600;
            color: var(--primary-color);
            margin-bottom: 15px;
            animation: pulse 2s ease-in-out infinite;
        }}

        .instructor-info {{
            background-color: var(--background-color);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 20px;
            opacity: 0;
            animation: slide-in 0.8s ease-out forwards;
            animation-delay: 0.4s;
        }}

        .playlist-link {{
            display: inline-block;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            color: white;
            text-decoration: none;
            padding: 12px 25px;
            border-radius: 30px;
            transition: all 0.3s ease;
            font-weight: 600;
            position: relative;
            overflow: hidden;
            opacity: 0;
            animation: slide-in 0.8s ease-out forwards;
            animation-delay: 0.6s;
        }}

        .playlist-link::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                120deg, 
                transparent, 
                rgba(255,255,255,0.3), 
                transparent
            );
            transition: all 0.5s ease;
        }}

        .playlist-link:hover::before {{
            left: 100%;
        }}

        .playlist-link:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(113, 88, 226, 0.3);
        }}

        @media (max-width: 600px) {{
            .course-card {{
                padding: 20px;
                margin: 20px 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="course-card">
        <div class="course-header">
            <div class="course-code">{course_code}</div>
            <h1 class="course-title">{course_name}</h1>
        </div>
        <div class="instructor-info">
            <strong>Instructor:</strong> {instructor}
        </div>
        <a href="{playlist_link}" class="playlist-link" target="_blank">Watch Playlist</a>
    </div>
</body>
</html>"""
    
    with open(f"c01/{course_code}.html", "w", encoding="utf-8") as file:
        file.write(html_content)

print("HTML files created successfully in the 'c01' folder!")