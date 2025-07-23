# from flask  import Flask
# app = Flask(__name__)  

# @app.route('/')
# def hello_world():
#     return 'bro Minh, First Step into CLOUD'

from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Template chính
MAIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} - Portfolio</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }
        
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 100px 0;
            text-align: center;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .profile-img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            border: 5px solid white;
            margin-bottom: 2rem;
            object-fit: cover;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .section {
            padding: 80px 0;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 3rem;
            color: #333;
        }
        
        .skill-bar {
            background: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 1rem;
            height: 25px;
        }
        
        .skill-progress {
            height: 100%;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 10px;
            transition: width 2s ease-in-out;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 0.9rem;
        }
        
        .project-card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            overflow: hidden;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        
        .project-img {
            height: 200px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
        }
        
        .contact-form {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
        }
        
        .navbar-custom {
            background: rgba(255,255,255,0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .btn-custom {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            transition: all 0.3s;
        }
        
        .btn-custom:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            color: white;
        }
        
        footer {
            background: #333;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        .social-links a {
            color: white;
            font-size: 1.5rem;
            margin: 0 10px;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: #667eea;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top navbar-custom">
        <div class="container">
            <a class="navbar-brand fw-bold" href="#home">{{ name }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#home">Trang chủ</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#about">Giới thiệu</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#skills">Kỹ năng</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#projects">Dự án</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Liên hệ</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-section">
        <div class="container">
            <img src="https://via.placeholder.com/200x200/667eea/ffffff?text=Avatar" alt="Profile" class="profile-img">
            <h1 class="hero-title">{{ name }}</h1>
            <p class="hero-subtitle">{{ title }}</p>
            <a href="#contact" class="btn btn-custom btn-lg">
                <i class="fas fa-envelope"></i> Liên hệ với tôi
            </a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">Giới thiệu</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <div class="text-center">
                        <p class="lead">{{ about }}</p>
                        <div class="row mt-4">
                            <div class="col-md-6">
                                <h5><i class="fas fa-birthday-cake text-primary"></i> Tuổi</h5>
                                <p>{{ age }} tuổi</p>
                            </div>
                            <div class="col-md-6">
                                <h5><i class="fas fa-map-marker-alt text-primary"></i> Địa chỉ</h5>
                                <p>{{ location }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section bg-light">
        <div class="container">
            <h2 class="section-title">Kỹ năng</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    {% for skill in skills %}
                    <div class="mb-3">
                        <div class="d-flex justify-content-between mb-1">
                            <span class="fw-bold">{{ skill.name }}</span>
                            <span>{{ skill.level }}%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-progress" style="width: {{ skill.level }}%">
                                {{ skill.level }}%
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <div class="container">
            <h2 class="section-title">Dự án</h2>
            <div class="row g-4">
                {% for project in projects %}
                <div class="col-md-6 col-lg-4">
                    <div class="card project-card h-100">
                        <div class="project-img">
                            <i class="{{ project.icon }}"></i>
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{{ project.name }}</h5>
                            <p class="card-text">{{ project.description }}</p>
                            <div class="mb-2">
                                {% for tech in project.technologies %}
                                <span class="badge bg-secondary me-1">{{ tech }}</span>
                                {% endfor %}
                            </div>
                        </div>
                        <div class="card-footer bg-transparent">
                            <a href="{{ project.link }}" class="btn btn-custom btn-sm" target="_blank">
                                <i class="fas fa-external-link-alt"></i> Xem dự án
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section bg-light">
        <div class="container">
            <h2 class="section-title">Liên hệ</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <div class="contact-form">
                        <form id="contactForm">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="mb-3">
                                        <label class="form-label">Họ tên *</label>
                                        <input type="text" class="form-control" name="name" required>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="mb-3">
                                        <label class="form-label">Email *</label>
                                        <input type="email" class="form-control" name="email" required>
                                    </div>
                                </div>
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Chủ đề</label>
                                <input type="text" class="form-control" name="subject">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Tin nhắn *</label>
                                <textarea class="form-control" name="message" rows="5" required></textarea>
                            </div>
                            <div class="text-center">
                                <button type="submit" class="btn btn-custom">
                                    <i class="fas fa-paper-plane"></i> Gửi tin nhắn
                                </button>
                            </div>
                        </form>
                    </div>
                    
                    <div class="row mt-5">
                        <div class="col-md-4 text-center">
                            <i class="fas fa-envelope fa-2x text-primary mb-2"></i>
                            <h5>Email</h5>
                            <p>{{ email }}</p>
                        </div>
                        <div class="col-md-4 text-center">
                            <i class="fas fa-phone fa-2x text-primary mb-2"></i>
                            <h5>Điện thoại</h5>
                            <p>{{ phone }}</p>
                        </div>
                        <div class="col-md-4 text-center">
                            <i class="fas fa-map-marker-alt fa-2x text-primary mb-2"></i>
                            <h5>Địa chỉ</h5>
                            <p>{{ location }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="social-links mb-3">
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-github"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
            </div>
            <p>&copy; 2024 {{ name }}. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const offsetTop = target.offsetTop - 70;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Contact form
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            fetch('/send-message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Tin nhắn đã được gửi thành công!');
                    this.reset();
                } else {
                    alert('Có lỗi xảy ra. Vui lòng thử lại!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Có lỗi xảy ra. Vui lòng thử lại!');
            });
        });

        // Animate skill bars on scroll
        function animateSkillBars() {
            const skillBars = document.querySelectorAll('.skill-progress');
            skillBars.forEach(bar => {
                const rect = bar.getBoundingClientRect();
                const windowHeight = window.innerHeight;
                
                if (rect.top < windowHeight && rect.bottom > 0) {
                    bar.style.width = bar.getAttribute('style').split('width: ')[1];
                }
            });
        }

        window.addEventListener('scroll', animateSkillBars);
        window.addEventListener('load', animateSkillBars);

        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(255,255,255,0.98)';
            } else {
                navbar.style.background = 'rgba(255,255,255,0.95)';
            }
        });
    </script>
</body>
</html>
'''

# Dữ liệu mẫu - bạn có thể thay đổi theo thông tin của mình
portfolio_data = {
    "name": "Nguyễn Văn A",
    "title": "Full Stack Developer",
    "about": "Tôi là một lập trình viên với niềm đam mê tạo ra những ứng dụng web hiện đại và thân thiện với người dùng. Với kinh nghiệm trong việc phát triển cả frontend và backend, tôi luôn sẵn sàng học hỏi công nghệ mới và giải quyết các thử thách phức tạp.",
    "age": 25,
    "location": "Hồ Chí Minh, Việt Nam",
    "email": "example@email.com",
    "phone": "+84 123 456 789",
    "skills": [
        {"name": "Python", "level": 90},
        {"name": "JavaScript", "level": 85},
        {"name": "React", "level": 80},
        {"name": "Flask/Django", "level": 85},
        {"name": "HTML/CSS", "level": 95},
        {"name": "MySQL/PostgreSQL", "level": 75},
        {"name": "Git", "level": 80}
    ],
    "projects": [
        {
            "name": "E-commerce Website",
            "description": "Website thương mại điện tử hoàn chỉnh với tính năng thanh toán, quản lý sản phẩm và đơn hàng.",
            "technologies": ["Python", "Flask", "MySQL", "Bootstrap"],
            "icon": "fas fa-shopping-cart",
            "link": "#"
        },
        {
            "name": "Task Management App",
            "description": "Ứng dụng quản lý công việc với tính năng theo dõi tiến độ, deadline và team collaboration.",
            "technologies": ["React", "Node.js", "MongoDB"],
            "icon": "fas fa-tasks",
            "link": "#"
        },
        {
            "name": "Weather Dashboard",
            "description": "Dashboard hiển thị thông tin thời tiết chi tiết với dự báo 7 ngày và bản đồ thời tiết.",
            "technologies": ["JavaScript", "API", "Chart.js"],
            "icon": "fas fa-cloud-sun",
            "link": "#"
        },
        {
            "name": "Personal Blog",
            "description": "Blog cá nhân với hệ thống CMS, comment, tag và tối ưu SEO.",
            "technologies": ["Django", "PostgreSQL", "Redis"],
            "icon": "fas fa-blog",
            "link": "#"
        },
        {
            "name": "Chat Application",
            "description": "Ứng dụng chat real-time với tính năng nhóm, chia sẻ file và emoji.",
            "technologies": ["Socket.io", "Express", "MongoDB"],
            "icon": "fas fa-comments",
            "link": "#"
        },
        {
            "name": "Data Visualization",
            "description": "Dashboard phân tích dữ liệu với các biểu đồ tương tác và báo cáo tự động.",
            "technologies": ["Python", "Plotly", "Pandas"],
            "icon": "fas fa-chart-bar",
            "link": "#"
        }
    ]
}

@app.route('/')
def home():
    return render_template_string(MAIN_TEMPLATE, **portfolio_data)

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        # Ở đây bạn có thể xử lý gửi email hoặc lưu tin nhắn vào database
        # Hiện tại chỉ in ra console để demo
        print(f"Tin nhắn từ {data['name']} ({data['email']}):")
        print(f"Chủ đề: {data.get('subject', 'Không có chủ đề')}")
        print(f"Nội dung: {data['message']}")
        
        return jsonify({"success": True, "message": "Tin nhắn đã được gửi thành công!"})
    except Exception as e:
        print(f"Lỗi: {e}")
        return jsonify({"success": False, "message": "Có lỗi xảy ra!"})

if __name__ == '__main__':
    app.run(debug=True)
