# Job Profiles Database
JOB_PROFILES = {
    "data_scientist": {
        "title": "Data Scientist",
        "required_skills": ["Python", "R", "Machine Learning", "Statistics", "SQL", "Pandas", "NumPy", "Scikit-learn"],
        "preferred_skills": ["TensorFlow", "PyTorch", "Jupyter", "Matplotlib", "Seaborn", "AWS", "GCP", "Azure", "Spark", "Hadoop"],
        "education": ["Computer Science", "Statistics", "Mathematics", "Data Science", "PhD", "Masters"],
        "experience_keywords": ["data analysis", "predictive modeling", "statistical analysis", "A/B testing", "data visualization"],
        "tools": ["Tableau", "Power BI", "Excel", "Git", "Docker", "Kubernetes"],
        "weight_distribution": {
            "technical_skills": 0.35,
            "ml_tools": 0.25, 
            "education": 0.15,
            "experience": 0.15,
            "soft_skills": 0.10
        }
    },
    "software_engineer": {
        "title": "Software Engineer", 
        "required_skills": ["Programming", "Python", "JavaScript", "Java", "C++", "Git", "APIs", "Databases"],
        "preferred_skills": ["React", "Node.js", "Django", "Flask", "FastAPI", "Docker", "Kubernetes", "AWS", "MongoDB", "PostgreSQL"],
        "education": ["Computer Science", "Software Engineering", "Engineering", "Bachelor", "Masters"],
        "experience_keywords": ["software development", "web applications", "REST API", "microservices", "agile", "testing"],
        "tools": ["IDE", "Jenkins", "CI/CD", "Linux", "Bash", "Shell"],
        "weight_distribution": {
            "technical_skills": 0.40,
            "frameworks": 0.25,
            "education": 0.15,
            "experience": 0.15,
            "soft_skills": 0.05
        }
    },
    "backend_developer": {
        "title": "Backend Developer",
        "required_skills": ["Python", "Java", "Node.js", "APIs", "Databases", "Server", "Backend", "REST"],
        "preferred_skills": ["FastAPI", "Django", "Flask", "Spring", "Express", "MongoDB", "PostgreSQL", "MySQL", "Redis"],
        "education": ["Computer Science", "Software Engineering", "Bachelor", "Masters"],
        "experience_keywords": ["backend development", "API development", "server-side", "database design", "microservices"],
        "tools": ["Postman", "Docker", "Kubernetes", "Git", "Linux", "AWS"],
        "weight_distribution": {
            "technical_skills": 0.40,
            "frameworks": 0.30,
            "experience": 0.15,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "fullstack_developer": {
        "title": "Full Stack Developer",
        "required_skills": ["JavaScript", "Python", "React", "Node.js", "HTML", "CSS", "Databases", "Git"],
        "preferred_skills": ["TypeScript", "Vue", "Angular", "Django", "FastAPI", "MongoDB", "PostgreSQL", "Docker"],
        "education": ["Computer Science", "Web Development", "Bachelor", "Bootcamp"],
        "experience_keywords": ["full stack development", "frontend", "backend", "web applications", "end-to-end"],
        "tools": ["VS Code", "Chrome DevTools", "Postman", "Git", "NPM", "Yarn"],
        "weight_distribution": {
            "technical_skills": 0.35,
            "frameworks": 0.30,
            "experience": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "frontend_developer": {
        "title": "Frontend Developer",
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "Vue", "Angular", "Web Development"],
        "preferred_skills": ["TypeScript", "Webpack", "Sass", "Redux", "Next.js", "Tailwind", "Bootstrap", "Git"],
        "education": ["Computer Science", "Web Development", "Design", "Bachelor", "Bootcamp"],
        "experience_keywords": ["user interface", "responsive design", "web applications", "frontend", "UI/UX"],
        "tools": ["VS Code", "Chrome DevTools", "Figma", "Adobe", "NPM", "Yarn"],
        "weight_distribution": {
            "frontend_skills": 0.40,
            "frameworks": 0.30,
            "experience": 0.15,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "mobile_developer": {
        "title": "Mobile Developer",
        "required_skills": ["Mobile Development", "iOS", "Android", "Swift", "Kotlin", "React Native", "Flutter"],
        "preferred_skills": ["Xcode", "Android Studio", "Firebase", "API Integration", "App Store", "Google Play"],
        "education": ["Computer Science", "Mobile Development", "Bachelor", "Masters"],
        "experience_keywords": ["mobile app development", "iOS development", "Android development", "app publishing"],
        "tools": ["Xcode", "Android Studio", "Git", "Firebase", "TestFlight"],
        "weight_distribution": {
            "mobile_skills": 0.40,
            "platforms": 0.30,
            "experience": 0.15,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "data_engineer": {
        "title": "Data Engineer",
        "required_skills": ["Python", "SQL", "Data Pipeline", "ETL", "Big Data", "Spark", "Hadoop"],
        "preferred_skills": ["Airflow", "Kafka", "AWS", "GCP", "Azure", "Docker", "Kubernetes", "Scala"],
        "education": ["Computer Science", "Data Engineering", "Engineering", "Bachelor", "Masters"],
        "experience_keywords": ["data pipeline", "ETL development", "data warehouse", "big data processing"],
        "tools": ["Airflow", "Kafka", "Spark", "Hadoop", "Git", "Docker"],
        "weight_distribution": {
            "technical_skills": 0.40,
            "big_data_tools": 0.30,
            "experience": 0.15,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "ml_engineer": {
        "title": "Machine Learning Engineer",
        "required_skills": ["Python", "Machine Learning", "TensorFlow", "PyTorch", "MLOps", "Model Deployment"],
        "preferred_skills": ["Kubernetes", "Docker", "AWS", "GCP", "Scikit-learn", "pandas", "NumPy"],
        "education": ["Computer Science", "Machine Learning", "AI", "Masters", "PhD"],
        "experience_keywords": ["ML model deployment", "model training", "MLOps", "production ML systems"],
        "tools": ["MLflow", "Kubeflow", "Docker", "Git", "Jupyter", "Cloud Platforms"],
        "weight_distribution": {
            "ml_skills": 0.40,
            "deployment_tools": 0.25,
            "experience": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "devops_engineer": {
        "title": "DevOps Engineer", 
        "required_skills": ["DevOps", "Docker", "Kubernetes", "AWS", "Linux", "CI/CD", "Infrastructure"],
        "preferred_skills": ["Terraform", "Ansible", "Jenkins", "Git", "Python", "Bash", "Monitoring", "Security"],
        "education": ["Computer Science", "Engineering", "Systems Administration", "Bachelor", "Certification"],
        "experience_keywords": ["automation", "deployment", "infrastructure", "cloud", "monitoring", "scaling"],
        "tools": ["Jenkins", "GitLab", "Prometheus", "Grafana", "ELK Stack", "Helm"],
        "weight_distribution": {
            "cloud_skills": 0.35,
            "automation": 0.30,
            "experience": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "qa_engineer": {
        "title": "QA Engineer",
        "required_skills": ["Testing", "Quality Assurance", "Test Automation", "Manual Testing", "Bug Tracking"],
        "preferred_skills": ["Selenium", "Jest", "Cypress", "Playwright", "Python", "JavaScript", "API Testing"],
        "education": ["Computer Science", "Software Testing", "Engineering", "Bachelor"],
        "experience_keywords": ["test automation", "manual testing", "quality assurance", "bug reporting", "test planning"],
        "tools": ["Selenium", "JIRA", "TestRail", "Postman", "Git"],
        "weight_distribution": {
            "testing_skills": 0.40,
            "automation_tools": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "ui_ux_designer": {
        "title": "UI/UX Designer",
        "required_skills": ["UI Design", "UX Design", "User Research", "Prototyping", "Wireframing"],
        "preferred_skills": ["Figma", "Adobe XD", "Sketch", "Adobe Creative Suite", "User Testing", "Design Systems"],
        "education": ["Design", "HCI", "Psychology", "Art", "Bachelor", "Masters"],
        "experience_keywords": ["user experience design", "user interface design", "user research", "design thinking"],
        "tools": ["Figma", "Adobe XD", "Sketch", "Adobe Creative Suite", "InVision", "Principle"],
        "weight_distribution": {
            "design_skills": 0.40,
            "design_tools": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "product_manager": {
        "title": "Product Manager",
        "required_skills": ["Product Management", "Strategy", "Analytics", "Leadership", "Communication"],
        "preferred_skills": ["Agile", "Scrum", "Jira", "Roadmap", "User Research", "A/B Testing", "SQL", "Python"],
        "education": ["Business", "MBA", "Engineering", "Computer Science", "Bachelor", "Masters"],
        "experience_keywords": ["product strategy", "roadmap", "stakeholder management", "user experience", "market research"],
        "tools": ["Jira", "Confluence", "Figma", "Analytics", "Excel", "Tableau"],
        "weight_distribution": {
            "leadership": 0.30,
            "analytical": 0.25,
            "experience": 0.20,
            "education": 0.15,
            "soft_skills": 0.10
        }
    },
    "project_manager": {
        "title": "Project Manager",
        "required_skills": ["Project Management", "Leadership", "Planning", "Risk Management", "Communication"],
        "preferred_skills": ["Agile", "Scrum", "PMP", "Jira", "Microsoft Project", "Budget Management"],
        "education": ["Business", "Management", "MBA", "PMP Certification", "Bachelor"],
        "experience_keywords": ["project planning", "team leadership", "budget management", "risk assessment", "stakeholder communication"],
        "tools": ["Microsoft Project", "Jira", "Confluence", "Excel", "Gantt Charts"],
        "weight_distribution": {
            "leadership": 0.35,
            "planning": 0.25,
            "experience": 0.25,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "business_analyst": {
        "title": "Business Analyst",
        "required_skills": ["Business Analysis", "Requirements Gathering", "SQL", "Excel", "Data Analysis"],
        "preferred_skills": ["Tableau", "Power BI", "Python", "R", "Process Improvement", "Documentation"],
        "education": ["Business", "MBA", "Economics", "Finance", "Bachelor", "Masters"],
        "experience_keywords": ["business requirements", "process analysis", "stakeholder engagement", "data analysis"],
        "tools": ["Excel", "Tableau", "Power BI", "SQL", "Visio", "Confluence"],
        "weight_distribution": {
            "analytical_skills": 0.35,
            "business_tools": 0.25,
            "experience": 0.25,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "cybersecurity_engineer": {
        "title": "Cybersecurity Engineer",
        "required_skills": ["Cybersecurity", "Network Security", "Risk Assessment", "Security Analysis", "Linux"],
        "preferred_skills": ["CISSP", "CEH", "Penetration Testing", "Firewall", "SIEM", "Python", "Scripting"],
        "education": ["Cybersecurity", "Computer Science", "Information Security", "Bachelor", "Certification"],
        "experience_keywords": ["security assessment", "vulnerability testing", "incident response", "security monitoring"],
        "tools": ["Wireshark", "Metasploit", "Nmap", "Burp Suite", "Splunk", "Nessus"],
        "weight_distribution": {
            "security_skills": 0.40,
            "security_tools": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "cloud_architect": {
        "title": "Cloud Architect",
        "required_skills": ["Cloud Architecture", "AWS", "Azure", "GCP", "Infrastructure", "Scalability"],
        "preferred_skills": ["Terraform", "CloudFormation", "Kubernetes", "Docker", "Microservices", "Serverless"],
        "education": ["Computer Science", "Cloud Computing", "Engineering", "Bachelor", "Masters"],
        "experience_keywords": ["cloud migration", "architecture design", "scalable systems", "cloud optimization"],
        "tools": ["AWS Console", "Azure Portal", "Terraform", "CloudFormation", "Docker", "Kubernetes"],
        "weight_distribution": {
            "cloud_expertise": 0.40,
            "architecture_skills": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "database_administrator": {
        "title": "Database Administrator",
        "required_skills": ["Database Administration", "SQL", "MySQL", "PostgreSQL", "Oracle", "Performance Tuning"],
        "preferred_skills": ["MongoDB", "Redis", "Backup & Recovery", "Replication", "Security", "Monitoring"],
        "education": ["Computer Science", "Database Management", "Information Systems", "Bachelor"],
        "experience_keywords": ["database management", "performance optimization", "backup and recovery", "database security"],
        "tools": ["MySQL Workbench", "pgAdmin", "Oracle Enterprise Manager", "MongoDB Compass"],
        "weight_distribution": {
            "database_skills": 0.45,
            "administration_tools": 0.25,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "marketing_manager": {
        "title": "Marketing Manager",
        "required_skills": ["Digital Marketing", "Campaign Management", "Analytics", "Brand Management", "Communication"],
        "preferred_skills": ["Google Analytics", "SEO", "SEM", "Social Media", "Email Marketing", "Content Marketing"],
        "education": ["Marketing", "Business", "MBA", "Communications", "Bachelor"],
        "experience_keywords": ["marketing campaigns", "brand strategy", "digital marketing", "customer acquisition"],
        "tools": ["Google Analytics", "HubSpot", "Mailchimp", "Hootsuite", "Adobe Creative Suite"],
        "weight_distribution": {
            "marketing_skills": 0.35,
            "digital_tools": 0.25,
            "experience": 0.25,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    "sales_manager": {
        "title": "Sales Manager",
        "required_skills": ["Sales Management", "Lead Generation", "CRM", "Negotiation", "Team Leadership"],
        "preferred_skills": ["Salesforce", "HubSpot", "Sales Analytics", "Pipeline Management", "Customer Relationship"],
        "education": ["Business", "Sales", "MBA", "Marketing", "Bachelor"],
        "experience_keywords": ["sales strategy", "team management", "revenue growth", "client relationships"],
        "tools": ["Salesforce", "HubSpot", "CRM Systems", "Excel", "LinkedIn Sales Navigator"],
        "weight_distribution": {
            "sales_skills": 0.35,
            "leadership": 0.30,
            "experience": 0.25,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    "hr_manager": {
        "title": "HR Manager",
        "required_skills": ["Human Resources", "Recruitment", "Employee Relations", "Performance Management", "Leadership"],
        "preferred_skills": ["HRIS", "Talent Acquisition", "Compensation", "Training", "Policy Development"],
        "education": ["Human Resources", "Psychology", "Business", "MBA", "Bachelor"],
        "experience_keywords": ["talent management", "employee engagement", "recruitment", "performance reviews"],
        "tools": ["HRIS Systems", "ATS", "Workday", "BambooHR", "LinkedIn Recruiter"],
        "weight_distribution": {
            "hr_skills": 0.35,
            "leadership": 0.30,
            "experience": 0.25,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== ADVANCED TECHNICAL ROLES ======
    "senior_software_architect": {
        "title": "Senior Software Architect",
        "required_skills": ["Software Architecture", "System Design", "Microservices", "Distributed Systems", "Leadership", "Technical Strategy"],
        "preferred_skills": ["Cloud Architecture", "Domain-Driven Design", "Event Sourcing", "CQRS", "Performance Optimization", "Security Architecture"],
        "education": ["Computer Science", "Software Engineering", "Masters", "Architecture Certification"],
        "experience_keywords": ["enterprise architecture", "system design", "technical leadership", "scalable systems", "architecture patterns"],
        "tools": ["UML", "Enterprise Architect", "Lucidchart", "AWS Well-Architected", "Azure Architecture Center"],
        "weight_distribution": {
            "architecture_skills": 0.40,
            "technical_leadership": 0.25,
            "experience": 0.25,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "ai_research_scientist": {
        "title": "AI Research Scientist",
        "required_skills": ["Artificial Intelligence", "Machine Learning", "Deep Learning", "Research", "Python", "TensorFlow", "PyTorch"],
        "preferred_skills": ["Computer Vision", "NLP", "Reinforcement Learning", "GANs", "Transformers", "BERT", "GPT", "Publications"],
        "education": ["PhD", "AI", "Machine Learning", "Computer Science", "Mathematics", "Research Publications"],
        "experience_keywords": ["AI research", "model development", "academic publications", "conference presentations", "research collaboration"],
        "tools": ["Jupyter", "Google Colab", "Weights & Biases", "MLflow", "Hugging Face", "ArXiv"],
        "weight_distribution": {
            "research_skills": 0.35,
            "ai_expertise": 0.30,
            "publications": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    "principal_engineer": {
        "title": "Principal Engineer",
        "required_skills": ["Technical Leadership", "System Architecture", "Software Engineering", "Mentoring", "Strategy", "Innovation"],
        "preferred_skills": ["Distributed Systems", "Performance Engineering", "Open Source", "Technical Writing", "Cross-functional Collaboration"],
        "education": ["Computer Science", "Engineering", "Masters", "Technical Certifications"],
        "experience_keywords": ["technical strategy", "engineering excellence", "cross-team collaboration", "innovation leadership", "technical mentoring"],
        "tools": ["Architecture Tools", "Code Review", "Technical Documentation", "Performance Profilers"],
        "weight_distribution": {
            "technical_leadership": 0.35,
            "architecture_skills": 0.30,
            "experience": 0.25,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== HEALTHCARE TECHNOLOGY ======
    "healthcare_data_scientist": {
        "title": "Healthcare Data Scientist",
        "required_skills": ["Data Science", "Healthcare Analytics", "Medical Data", "Python", "R", "Statistics", "Machine Learning"],
        "preferred_skills": ["HIPAA", "Clinical Data", "Medical Imaging", "EHR", "Epidemiology", "Biostatistics", "FDA Regulations"],
        "education": ["Data Science", "Biostatistics", "Public Health", "Computer Science", "Masters", "PhD"],
        "experience_keywords": ["healthcare analytics", "clinical data analysis", "medical research", "patient outcomes", "healthcare informatics"],
        "tools": ["SAS", "SPSS", "Epic", "Cerner", "MATLAB", "Medical Imaging Software"],
        "weight_distribution": {
            "healthcare_expertise": 0.35,
            "data_science": 0.30,
            "domain_knowledge": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    "bioinformatics_scientist": {
        "title": "Bioinformatics Scientist",
        "required_skills": ["Bioinformatics", "Genomics", "Python", "R", "Bioconductor", "NGS", "Sequence Analysis"],
        "preferred_skills": ["GWAS", "Proteomics", "Machine Learning", "Docker", "Cloud Computing", "Linux", "Perl"],
        "education": ["Bioinformatics", "Computational Biology", "Biology", "Computer Science", "PhD", "Masters"],
        "experience_keywords": ["genomic analysis", "sequence alignment", "variant calling", "pathway analysis", "biomarker discovery"],
        "tools": ["Galaxy", "GATK", "Bowtie", "SAMtools", "Bioconductor", "IGV"],
        "weight_distribution": {
            "bioinformatics_skills": 0.40,
            "programming": 0.25,
            "domain_expertise": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    # ====== FINTECH & FINANCE ======
    "quantitative_analyst": {
        "title": "Quantitative Analyst",
        "required_skills": ["Quantitative Analysis", "Financial Modeling", "Python", "R", "Statistics", "Risk Management", "Mathematics"],
        "preferred_skills": ["Bloomberg", "Reuters", "C++", "MATLAB", "Monte Carlo", "Options Pricing", "Derivatives", "VaR"],
        "education": ["Finance", "Mathematics", "Statistics", "Economics", "Quantitative Finance", "Masters", "PhD", "CFA"],
        "experience_keywords": ["quantitative modeling", "risk analysis", "algorithmic trading", "financial derivatives", "portfolio optimization"],
        "tools": ["Bloomberg Terminal", "MATLAB", "QuantLib", "R Studio", "Python", "Excel VBA"],
        "weight_distribution": {
            "quantitative_skills": 0.40,
            "financial_knowledge": 0.25,
            "programming": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    "blockchain_developer": {
        "title": "Blockchain Developer",
        "required_skills": ["Blockchain", "Smart Contracts", "Solidity", "Web3", "Cryptocurrency", "DeFi", "Ethereum"],
        "preferred_skills": ["Truffle", "Hardhat", "IPFS", "NFT", "Layer 2", "Consensus Algorithms", "Cryptography"],
        "education": ["Computer Science", "Cryptography", "Blockchain Certification", "Bachelor", "Masters"],
        "experience_keywords": ["smart contract development", "DApp development", "blockchain integration", "cryptocurrency", "decentralized applications"],
        "tools": ["MetaMask", "Remix IDE", "Ganache", "OpenZeppelin", "Alchemy", "Infura"],
        "weight_distribution": {
            "blockchain_skills": 0.45,
            "smart_contracts": 0.25,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== GAMING & ENTERTAINMENT ======
    "game_developer": {
        "title": "Game Developer",
        "required_skills": ["Game Development", "Unity", "Unreal Engine", "C#", "C++", "Game Design", "3D Graphics"],
        "preferred_skills": ["Blender", "Maya", "Photoshop", "Shader Programming", "Multiplayer", "Mobile Games", "VR/AR"],
        "education": ["Computer Science", "Game Development", "Game Design", "Computer Graphics", "Bachelor"],
        "experience_keywords": ["game programming", "gameplay mechanics", "graphics programming", "game optimization", "player experience"],
        "tools": ["Unity", "Unreal Engine", "Visual Studio", "Blender", "Perforce", "Git LFS"],
        "weight_distribution": {
            "game_development": 0.40,
            "programming_skills": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "3d_animator": {
        "title": "3D Animator",
        "required_skills": ["3D Animation", "Maya", "Blender", "Character Animation", "Rigging", "Modeling", "Animation Principles"],
        "preferred_skills": ["Motion Capture", "ZBrush", "Substance Painter", "After Effects", "Cinema 4D", "Houdini"],
        "education": ["Animation", "Computer Graphics", "Fine Arts", "Digital Media", "Bachelor"],
        "experience_keywords": ["character animation", "3D modeling", "visual effects", "animation pipeline", "creative storytelling"],
        "tools": ["Maya", "Blender", "3ds Max", "ZBrush", "Substance Suite", "Photoshop"],
        "weight_distribution": {
            "animation_skills": 0.45,
            "software_proficiency": 0.30,
            "creativity": 0.15,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== RESEARCH & ACADEMIA ======
    "research_scientist": {
        "title": "Research Scientist",
        "required_skills": ["Scientific Research", "Data Analysis", "Statistical Analysis", "Research Methodology", "Publication", "Grant Writing"],
        "preferred_skills": ["Python", "R", "MATLAB", "Laboratory Skills", "Peer Review", "Conference Presentations", "Collaboration"],
        "education": ["PhD", "Research", "Science", "Mathematics", "Postdoc", "Academic Publications"],
        "experience_keywords": ["scientific research", "experimental design", "data interpretation", "academic publications", "research collaboration"],
        "tools": ["SPSS", "R Studio", "LaTeX", "EndNote", "Laboratory Equipment", "Statistical Software"],
        "weight_distribution": {
            "research_expertise": 0.35,
            "analytical_skills": 0.25,
            "publications": 0.20,
            "education": 0.15,
            "soft_skills": 0.05
        }
    },
    
    "university_professor": {
        "title": "University Professor",
        "required_skills": ["Teaching", "Research", "Academic Writing", "Curriculum Development", "Student Mentoring", "Subject Matter Expertise"],
        "preferred_skills": ["Grant Writing", "Peer Review", "Conference Speaking", "Academic Administration", "Online Teaching"],
        "education": ["PhD", "Postdoc", "Academic Publications", "Teaching Experience", "Tenure Track"],
        "experience_keywords": ["university teaching", "academic research", "student supervision", "curriculum design", "scholarly publications"],
        "tools": ["LMS", "Research Databases", "Statistical Software", "Presentation Tools", "Academic Writing Software"],
        "weight_distribution": {
            "teaching_skills": 0.30,
            "research_expertise": 0.30,
            "publications": 0.20,
            "education": 0.15,
            "soft_skills": 0.05
        }
    },
    
    # ====== CREATIVE & MEDIA ======
    "graphic_designer": {
        "title": "Graphic Designer",
        "required_skills": ["Graphic Design", "Adobe Creative Suite", "Photoshop", "Illustrator", "InDesign", "Typography", "Branding"],
        "preferred_skills": ["Figma", "Sketch", "After Effects", "Web Design", "Print Design", "Logo Design", "Color Theory"],
        "education": ["Graphic Design", "Visual Arts", "Fine Arts", "Digital Media", "Bachelor"],
        "experience_keywords": ["visual design", "brand identity", "creative campaigns", "design thinking", "client collaboration"],
        "tools": ["Adobe Creative Suite", "Figma", "Sketch", "Canva", "CorelDRAW", "Procreate"],
        "weight_distribution": {
            "design_skills": 0.40,
            "software_proficiency": 0.30,
            "creativity": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "content_creator": {
        "title": "Content Creator",
        "required_skills": ["Content Creation", "Social Media", "Video Editing", "Photography", "Storytelling", "Brand Building"],
        "preferred_skills": ["YouTube", "TikTok", "Instagram", "Premiere Pro", "Final Cut", "SEO", "Analytics"],
        "education": ["Communications", "Marketing", "Digital Media", "Journalism", "Bachelor"],
        "experience_keywords": ["content strategy", "audience engagement", "social media growth", "brand partnerships", "multimedia production"],
        "tools": ["Adobe Premiere", "Final Cut Pro", "Photoshop", "Canva", "Analytics Tools", "Social Media Schedulers"],
        "weight_distribution": {
            "content_skills": 0.35,
            "social_media": 0.25,
            "creativity": 0.25,
            "education": 0.05,
            "soft_skills": 0.10
        }
    },
    
    # ====== OPERATIONS & LOGISTICS ======
    "operations_manager": {
        "title": "Operations Manager",
        "required_skills": ["Operations Management", "Process Improvement", "Leadership", "Supply Chain", "Project Management", "Analytics"],
        "preferred_skills": ["Lean Six Sigma", "ERP Systems", "Inventory Management", "Quality Control", "Budget Management"],
        "education": ["Business Administration", "Operations Management", "Engineering", "MBA", "Bachelor"],
        "experience_keywords": ["operational efficiency", "process optimization", "team leadership", "cost reduction", "quality improvement"],
        "tools": ["ERP Systems", "Excel", "Project Management Tools", "Analytics Software", "Quality Management Systems"],
        "weight_distribution": {
            "operations_skills": 0.35,
            "leadership": 0.30,
            "experience": 0.25,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "supply_chain_analyst": {
        "title": "Supply Chain Analyst",
        "required_skills": ["Supply Chain Management", "Data Analysis", "Forecasting", "Inventory Management", "Logistics", "Excel"],
        "preferred_skills": ["SQL", "Python", "Tableau", "SAP", "Oracle", "Demand Planning", "Vendor Management"],
        "education": ["Supply Chain Management", "Business", "Engineering", "Analytics", "Bachelor"],
        "experience_keywords": ["supply chain optimization", "demand forecasting", "inventory analysis", "vendor relationships", "cost analysis"],
        "tools": ["Excel", "SAP", "Oracle", "Tableau", "Power BI", "Supply Chain Software"],
        "weight_distribution": {
            "analytical_skills": 0.40,
            "supply_chain_knowledge": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== CONSULTING & STRATEGY ======
    "management_consultant": {
        "title": "Management Consultant",
        "required_skills": ["Management Consulting", "Strategic Planning", "Business Analysis", "Problem Solving", "Communication", "Leadership"],
        "preferred_skills": ["McKinsey Framework", "Case Studies", "Financial Modeling", "Change Management", "Client Management"],
        "education": ["MBA", "Business", "Consulting", "Strategy", "Top Tier University"],
        "experience_keywords": ["strategic consulting", "business transformation", "client engagement", "problem solving", "executive presentations"],
        "tools": ["PowerPoint", "Excel", "Financial Modeling Tools", "Project Management Software"],
        "weight_distribution": {
            "consulting_skills": 0.35,
            "analytical_thinking": 0.25,
            "communication": 0.20,
            "education": 0.15,
            "soft_skills": 0.05
        }
    },
    
    "strategy_analyst": {
        "title": "Strategy Analyst",
        "required_skills": ["Strategic Analysis", "Market Research", "Competitive Analysis", "Financial Modeling", "Data Analysis", "Business Intelligence"],
        "preferred_skills": ["SQL", "Python", "Tableau", "Excel", "PowerPoint", "Industry Analysis", "M&A Analysis"],
        "education": ["Business", "Economics", "Finance", "MBA", "Bachelor"],
        "experience_keywords": ["strategic planning", "market analysis", "competitive intelligence", "business insights", "data-driven recommendations"],
        "tools": ["Excel", "PowerPoint", "Tableau", "SQL", "Market Research Tools", "Financial Software"],
        "weight_distribution": {
            "analytical_skills": 0.40,
            "strategic_thinking": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    # ====== HEALTHCARE PROFESSIONALS ======
    "clinical_data_manager": {
        "title": "Clinical Data Manager",
        "required_skills": ["Clinical Data Management", "EDC Systems", "Clinical Trials", "GCP", "Data Quality", "SAS", "R"],
        "preferred_skills": ["Medidata Rave", "InForm", "Clinical Research", "Regulatory Compliance", "CDASH", "SDTM"],
        "education": ["Life Sciences", "Statistics", "Clinical Research", "Masters", "Clinical Data Management Certification"],
        "experience_keywords": ["clinical trials", "data management", "regulatory compliance", "database design", "data validation"],
        "tools": ["Medidata Rave", "SAS", "R", "EDC Systems", "Clinical Trial Management Systems"],
        "weight_distribution": {
            "clinical_expertise": 0.35,
            "data_management": 0.30,
            "regulatory_knowledge": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    # ====== EMERGING TECHNOLOGIES ======
    "ar_vr_developer": {
        "title": "AR/VR Developer",
        "required_skills": ["AR/VR Development", "Unity", "Unreal Engine", "C#", "3D Graphics", "Spatial Computing", "HCI"],
        "preferred_skills": ["ARCore", "ARKit", "Oculus SDK", "HoloLens", "WebXR", "Computer Vision", "3D Math"],
        "education": ["Computer Science", "Game Development", "Computer Graphics", "HCI", "Bachelor"],
        "experience_keywords": ["immersive experiences", "AR applications", "VR applications", "3D interaction", "spatial computing"],
        "tools": ["Unity", "Unreal Engine", "Blender", "ARCore", "ARKit", "Oculus SDK"],
        "weight_distribution": {
            "ar_vr_skills": 0.40,
            "3d_programming": 0.30,
            "experience": 0.20,
            "education": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "iot_engineer": {
        "title": "IoT Engineer",
        "required_skills": ["IoT", "Embedded Systems", "C/C++", "Python", "Hardware", "Sensors", "Connectivity"],
        "preferred_skills": ["Arduino", "Raspberry Pi", "MQTT", "Edge Computing", "Cloud Integration", "Wireless Protocols"],
        "education": ["Electrical Engineering", "Computer Engineering", "IoT", "Embedded Systems", "Bachelor"],
        "experience_keywords": ["IoT development", "sensor integration", "embedded programming", "device connectivity", "edge computing"],
        "tools": ["Arduino IDE", "Raspberry Pi", "PlatformIO", "AWS IoT", "Azure IoT", "Google Cloud IoT"],
        "weight_distribution": {
            "iot_skills": 0.40,
            "embedded_programming": 0.25,
            "hardware_knowledge": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    # ====== JUNIOR/ENTRY LEVEL ROLES ======
    "junior_developer": {
        "title": "Junior Developer",
        "required_skills": ["Programming", "Git", "HTML", "CSS", "JavaScript", "Problem Solving", "Learning Agility"],
        "preferred_skills": ["React", "Python", "SQL", "Testing", "Debugging", "Code Review", "Agile"],
        "education": ["Computer Science", "Bootcamp", "Self-taught", "Bachelor", "Associate"],
        "experience_keywords": ["junior developer", "entry level", "software development", "learning", "mentorship"],
        "tools": ["VS Code", "Git", "Browser DevTools", "Terminal", "Debugging Tools"],
        "weight_distribution": {
            "fundamental_skills": 0.35,
            "learning_ability": 0.25,
            "basic_tools": 0.25,
            "education": 0.10,
            "soft_skills": 0.05
        }
    },
    
    "data_analyst_entry": {
        "title": "Entry Level Data Analyst",
        "required_skills": ["Excel", "SQL", "Data Analysis", "Statistics", "Data Visualization", "Problem Solving"],
        "preferred_skills": ["Python", "R", "Tableau", "Power BI", "Google Analytics", "Statistical Analysis"],
        "education": ["Statistics", "Mathematics", "Economics", "Data Science", "Bachelor"],
        "experience_keywords": ["data analysis", "reporting", "dashboards", "entry level", "analytical thinking"],
        "tools": ["Excel", "SQL", "Tableau", "Power BI", "Google Sheets", "Basic Python"],
        "weight_distribution": {
            "analytical_skills": 0.40,
            "tools_proficiency": 0.30,
            "education": 0.20,
            "experience": 0.05,
            "soft_skills": 0.05
        }
    },
    
    "marketing_coordinator": {
        "title": "Marketing Coordinator",
        "required_skills": ["Digital Marketing", "Social Media", "Content Creation", "Email Marketing", "Analytics", "Communication"],
        "preferred_skills": ["Google Analytics", "Facebook Ads", "Mailchimp", "Canva", "SEO", "Campaign Management"],
        "education": ["Marketing", "Communications", "Business", "Digital Marketing", "Bachelor"],
        "experience_keywords": ["marketing support", "campaign coordination", "social media management", "content marketing"],
        "tools": ["Google Analytics", "Social Media Tools", "Email Platforms", "Design Software", "Marketing Automation"],
        "weight_distribution": {
            "marketing_basics": 0.35,
            "digital_tools": 0.30,
            "creativity": 0.20,
            "education": 0.10,
            "soft_skills": 0.05
        }
    }
}
