from flask import Flask

app = Flask(__name__)
from flask import Flask, request, render_template_string
from flask_mail import Mail, Message   # <- this line must exist

app.config["MAIL_SERVER"]   = "smtp.gmail.com"
app.config["MAIL_PORT"]     = 587
app.config["MAIL_USE_TLS"]  = True
app.config["MAIL_USE_SSL"]  = False
app.config["MAIL_USERNAME"] = "ScottsWebDesignGA@gmail.com"
app.config["MAIL_PASSWORD"] = "ziyg nazf lomv kkjy"
mail = Mail(app)

mail = Mail(app)

mail = Mail(app)

@app.route("/")
def home():
    return """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scott’s Web Design</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-image: url("/static/images/background2.jpg");
            background-color: #2c3e50;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            font-family: 'Poppins', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 8px;
        }

        .container h1 {
            text-align: center;
            font-size: 42px;
            margin-bottom: 16px;
            color: #ffffff;
        }

        .nav-center {
            text-align: center;
            margin-bottom: 20px;
        }

        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropbtn {
            background: linear-gradient(135deg, #ff4757, #ff7a59);
            color: #ffffff;
            padding: 16px 34px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 8px 18px rgba(255, 71, 87, 0.35);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
            font-family: 'Poppins', Arial, sans-serif;
        }

        .dropbtn:hover {
            transform: translateY(-1px) scale(1.02);
            filter: brightness(1.05);
            box-shadow: 0 10px 22px rgba(255, 71, 87, 0.45);
        }

        .dropdown-content {
            display: none;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            background-color: #000000;
            min-width: 190px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.28);
            border-radius: 10px;
            z-index: 1;
            overflow: hidden;
        }

        .dropdown-content a {
            color: #ff4757;
            padding: 14px 16px;
            text-decoration: none;
            display: block;
            font-weight: 600;
            font-family: 'Poppins', Arial, sans-serif;
        }

        .dropdown-content a:hover {
            background-color: #111111;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        p {
            text-align: center;
            font-size: 1.1rem;
            margin: 10px 0 0 0;
            line-height: 1.6;
        }

        h2 {
            color: #ffffff;
            margin-top: 30px;
            text-align: center;
        }

        ul {
            max-width: 700px;
            margin: 16px auto 0 auto;
            line-height: 1.7;
            padding-left: 20px;
        }

        li {
            margin-bottom: 8px;
        }

        .section-box {
            margin-top: 30px;
            padding: 22px;
            background-color: rgba(255, 255, 255, 0.08);
            border-radius: 12px;
        }

        .local-box {
            text-align: center;
            margin-top: 28px;
            padding: 18px;
            background-color: rgba(255, 255, 255, 0.06);
            border-radius: 12px;
        }

        .cta-btn {
            display: inline-block;
            text-align: center;
            background: linear-gradient(135deg, #3498db, #6c5ce7);
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 999px;
            text-decoration: none;
            font-weight: 800;
            letter-spacing: 0.2px;
            box-shadow: 0 10px 20px rgba(52, 152, 219, 0.30);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
            margin: 10px 15px;
            font-family: 'Poppins', Arial, sans-serif;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 14px 24px rgba(52, 152, 219, 0.40);
        }

        .btn-center {
            text-align: center;
            margin-top: 24px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Scott’s Web Design</h1>

        <div class="nav-center">
            <div class="dropdown">
                <button class="dropbtn">Menu ▼</button>
                <div class="dropdown-content">
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/services">Services</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </div>

        <p>Scott’s Web Design helps small businesses get online with a site that looks good and feels easy to use.</p>
        <p>I build websites that are clean, professional, and made to fit the business, not some one-size-fits-all template.</p>
        <p>My goal is to make the process simple and give you something that helps your business look solid online.</p>

        <div class="section-box">
            <h2>What you get</h2>
            <ul>
                <li>A website that looks good on phones, tablets, and computers.</li>
                <li>A layout that is easy for customers to understand.</li>
                <li>A site built around your business and your goals.</li>
                <li>Simple communication so you always know what’s going on.</li>
            </ul>
        </div>

        <div class="local-box">
            <h2>Serving Douglas and surrounding areas</h2>
            <p>I work with small businesses in Douglas, Georgia and nearby towns that want a better website without the hassle.</p>
        </div>

        <div style="text-align: center; margin-top: 22px;">
            <a class="cta-btn" href="/services">View Services</a>
            <a class="cta-btn" href="/contact">Get a Quote</a>
        </div>
    </div>
</body>
</html>
"""


@app.route("/services")
def services():
    return """
<!doctype html>
<html>
<head>
    <title>Services – Ryan Website Help</title>
    <style>
        body {
            background-image: url("/static/images/background2.jpg");
            background-color: #2c3e50;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            background-color: rgba(0, 0, 0, 0.68);
            padding: 32px;
            border-radius: 14px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.28);
        }

        .container h1 {
            text-align: center;
            font-size: 42px;
            margin-bottom: 16px;
            color: #ffffff;
        }

        .nav-center {
            text-align: center;
            margin-bottom: 18px;
        }

        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropbtn {
            background: linear-gradient(135deg, #ff4757, #ff7a59);
            color: #ffffff;
            padding: 16px 34px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 8px 18px rgba(255, 71, 87, 0.35);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
        }

        .dropbtn:hover {
            transform: translateY(-1px) scale(1.02);
            filter: brightness(1.05);
            box-shadow: 0 10px 22px rgba(255, 71, 87, 0.45);
        }

        .dropdown-content {
            display: none;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            background-color: #000000;
            min-width: 190px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.28);
            border-radius: 10px;
            z-index: 1;
            overflow: hidden;
        }

        .dropdown-content a {
            color: #ff4757;
            padding: 14px 16px;
            text-decoration: none;
            display: block;
            font-weight: 600;
        }

        .dropdown-content a:hover {
            background-color: #111111;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        p {
            text-align: center;
            font-size: 1.08rem;
            margin: 10px 0 0 0;
            line-height: 1.6;
        }

        h2, h3, h4 {
            color: #ffffff;
        }

        ul {
            padding-left: 20px;
            line-height: 1.5;
        }

        li {
            margin-bottom: 8px;
        }

        a {
            margin: 0 8px;
            text-decoration: none;
            color: #3498db;
        }

        a:hover {
            text-decoration: underline;
        }

        .ctn-btn {
            display: inline-block;
            background-color: #3498db;
            color: #ffffff;
            padding: 12px 24px;
            margin: 10px 0;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .ctn-btn:hover {
            background-color: #2980b9;
        }

        .offer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 18px;
            margin-top: 18px;
        }

        .plan-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.12), rgba(255,255,255,0.08));
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 16px;
            padding: 22px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.22);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
        }

        .plan-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 14px 34px rgba(0,0,0,0.30);
            border-color: rgba(255, 71, 87, 0.55);
        }

        .plan-top {
            text-align: center;
            margin-bottom: 14px;
        }

        .plan-name {
            margin: 0;
            color: #ffffff;
            font-size: 1.4rem;
        }

        .plan-price {
            margin: 8px 0 0 0;
            color: #ff4757;
            font-size: 1.55rem;
            font-weight: 800;
        }

        .plan-card ul {
            padding-left: 18px;
            margin: 0 0 18px 0;
        }

        .plan-card li {
            margin-bottom: 8px;
            line-height: 1.45;
        }

        .cta-btn {
            display: block;
            text-align: center;
            background: linear-gradient(135deg, #3498db, #6c5ce7);
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 999px;
            text-decoration: none;
            font-weight: 800;
            letter-spacing: 0.2px;
            box-shadow: 0 10px 20px rgba(52, 152, 219, 0.30);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 14px 24px rgba(52, 152, 219, 0.40);
            text-decoration: none;
        }

        .note {
            margin-top: 22px;
            font-size: 0.98rem;
            opacity: 0.95;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Services – Ryan Website Help</h1>

        <div class="nav-center">
            <div class="dropdown">
                <button class="dropbtn">Menu ▼</button>
                <div class="dropdown-content">
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/services">Services</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </div>

        <p>I help small businesses in Douglas, GA build, fix, and update professional websites that help increase visibility and ease of use. </p>

        <h2>What I Offer</h2>
        <ul>
            <li>New websites that are clean, simple, and mobile‑friendly.</li>
            <li>Fixes and updates for existing websites.</li>
            <li>Google Business Profile setup to help you show up in Google Search and Maps.</li>
        </ul>

        <h2 class="section-title">Packages I Offer</h2>
        <div class="offer-grid">
            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Starter Website</h3>
                    <div class="plan-price">$150–$250</div>
                </div>
                <ul>
                    <li>1‑page website focused on what customers need to know</li>
                    <li>Clear layout, contact info, and mobile‑friendly design</li>
                    <li>Basic local SEO so Google can show your site faster</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>

            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Basic Business</h3>
                    <div class="plan-price">$400–$600</div>
                </div>
                <ul>
                    <li>4‑page website (Home, About, Services, Contact)</li>
                    <li>Better layout and readability on phones</li>
                    <li>Basic SEO setup for your key services</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>

            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Plus Local</h3>
                    <div class="plan-price">$600–$800</div>
                </div>
                <ul>
                    <li>4‑page business website</li>
                    <li>Google Business Profile setup and basic SEO</li>
                    <li>Help show up in Google Maps and local search</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>

            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Website Tune‑Up</h3>
                    <div class="plan-price">$150–$250</div>
                </div>
                <ul>
                    <li>Fix broken links, outdated text, and missing info</li>
                    <li>Clean up layout and make it look better on phones</li>
                    <li>Small tweaks and updates based on your needs</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>

            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Website Refresh</h3>
                    <div class="plan-price">$300–$450</div>
                </div>
                <ul>
                    <li>Modernize the look and feel of your site</li>
                    <li>Improve mobile view and navigation</li>
                    <li>Update content and fix common issues</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>

            <div class="plan-card">
                <div class="plan-top">
                    <h3 class="plan-name">Hourly Fix‑It</h3>
                    <div class="plan-price">$25/hour</div>
                </div>
                <ul>
                    <li>Small tasks: text changes, basic design tweaks</li>
                    <li>Quick edits and minor fixes</li>
                    <li>Flexible help for small recurring updates</li>
                </ul>
                <a class="cta-btn" href="/contact">Contact Me</a>
            </div>
        </div>

        <p class="note">Packages include two revisions.   Any extra changes will be billed at the hourly rate.</p>
    </div>
</body>
</html>
"""

@app.route("/about")
def about():
    html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Scott – Scott’s Web Design</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', Arial, sans-serif;
            font-size: 1.1rem;
            line-height: 1.6;
            background-image: url("/static/images/background2.jpg");
            background-color: #2c3e50;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 8px;
        }

        h1 {
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 700;
            font-size: 42px;
            text-align: center;
            margin-bottom: 16px;
            color: #ffffff;
        }

        .nav-center {
            text-align: center;
            margin-bottom: 20px;
        }

        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropbtn {
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 600;
            background: linear-gradient(135deg, #ff4757, #ff7a59);
            color: #ffffff;
            padding: 16px 34px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            font-size: 18px;
            box-shadow: 0 8px 18px rgba(255, 71, 87, 0.35);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
        }

        .dropbtn:hover {
            transform: translateY(-1px) scale(1.02);
            filter: brightness(1.05);
            box-shadow: 0 10px 22px rgba(255, 71, 87, 0.45);
        }

        .dropdown-content {
            display: none;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            background-color: #000000;
            min-width: 190px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.28);
            border-radius: 10px;
            z-index: 1;
            overflow: hidden;
        }

        .dropdown-content a {
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 500;
            color: #ff4757;
            padding: 14px 16px;
            text-decoration: none;
            display: block;
        }

        .dropdown-content a:hover {
            background-color: #111111;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        p {
            margin: 10px 0;
        }

        ul {
            margin: 0 0 10px 20px;
            padding: 0;
        }

        h2 {
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 600;
            color: #ffffff;
            margin-top: 20px;
            margin-bottom: 8px;
        }

        .intro {
            text-align: center;
        }

        .intro p {
            max-width: 700px;
            margin: 0 auto 10px;
        }

        .cert-block {
            text-align: center;
            margin: 25px 0 15px;
        }

        .cert-block img {
            max-width: 180px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        }

        .cert-block p {
            margin-top: 10px;
            font-size: 0.95rem;
            opacity: 0.95;
        }

        .skill-box {
            background-color: rgba(0, 0, 0, 0.4);
            border-radius: 8px;
            padding: 16px 20px;
            margin: 16px 0 0 0;
        }

        .cta-btn {
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 700;
            display: inline-block;
            text-align: center;
            background: linear-gradient(135deg, #3498db, #6c5ce7);
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 999px;
            text-decoration: none;
            letter-spacing: 0.2px;
            box-shadow: 0 10px 20px rgba(52, 152, 219, 0.30);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
            margin: 10px 15px;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 14px 24px rgba(52, 152, 219, 0.40);
        }

        .btn-center {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>About Scott – Scott’s Web Design</h1>

        <!-- Main navigation -->
        <div class="nav-center">
            <div class="dropdown">
                <button class="dropbtn">Menu ▼</button>
                <div class="dropdown-content">
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/services">Services</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </div>

        <!-- Personal intro -->
        <div class="intro">
            <p>I’m Scott, and I run Scott’s Web Design.</p>
            <p>I help small businesses get a website that fits what they do, looks professional, and works the way it should.</p>
        </div>

        <!-- ITIL 4 Foundation certification -->
        <div class="cert-block">
            <img src="/static/images/cert1.jpg" alt="ITIL 4 Foundation certification badge">
            <p>
                <strong>ITIL 4 Foundation Certified</strong>
                – I’ve trained in modern IT service management practices,
                so I understand how technology should support real‑world business needs and keep things running smoothly.
            </p>
        </div>

        <!-- Who I help most -->
        <h2>Who I help the most</h2>
        <p>I work mainly with small local businesses that need a simple, clear website they can actually use.</p>
        <ul>
            <li>Fixing broken navigation or confusing layouts.</li>
            <li>Making sites easy to update and manage over time.</li>
            <li>Keeping information organized and reliable, without unnecessary complexity.</li>
        </ul>

        <!-- What my background brings -->
        <h2>What my background brings to your site</h2>
        <p>My ITIL 4 training gives me a solid understanding of how technology supports customers and business goals. I approach websites as tools that should:</p>
        <ul>
            <li>Be easy for customers to use.</li>
            <li>Keep information clear and dependable.</li>
            <li>Work smoothly day‑to‑day without constant tech headaches.</li>
        </ul>
        <p>That means I build your site with structure and reliability in mind, not just “looks good for today.”</p>

        <!-- How I work with clients -->
        <h2>How I work with clients</h2>
        <p>I like to keep things simple and honest:</p>
        <ul>
            <li>We start by talking about what you actually need, not just what sounds fancy.</li>
            <li>I build a plan around your business, then show you progress as the site comes together.</li>
            <li>When it’s done, I’ll explain how to manage the basics so you don’t feel stuck.</li>
        </ul>
        <p>If you ever feel confused, that’s on me to fix—not you.</p>

        <!-- Why this matters for the business -->
        <div class="skill-box">
            <p><strong>Why this matters for your business</strong></p>
            <p>Small businesses deal with limited time and resources. I focus on giving you a website that:</p>
            <ul>
                <li>Loads quickly and works well on phones and laptops.</li>
                <li>Clearly shows what you do and how to contact you.</li>
                <li>Is built in a way that’s easier to maintain and update over time.</li>
            </ul>
        </div>

        <!-- Call to action buttons -->
        <div class="btn-center">
            <a class="cta-btn" href="/services">View Services</a>
            <a class="cta-btn" href="/contact">Get a Quote</a>
        </div>
    </div>
</body>
</html>
    """
    return html
@app.route("/contact", methods=["GET", "POST"])
def contact():
    msg = ""

    if request.method == "POST":
        name   = request.form.get("name", "").strip()
        email  = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            try:
                body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""
                msg_obj = Message(
                    subject="New Contact Form Submission – Scott’s Web Design",
                    sender=app.config["MAIL_USERNAME"],
                    recipients=["ScottsWebDesignGA@gmail.com"]
                )
                msg_obj.body = body
                mail.send(msg_obj)
                msg = "Thank you! Your message has been sent. I’ll get back to you soon."
            except Exception as e:
                print("Email send failed:", e)
                msg = "Sorry, something went wrong sending your message. Please try again or email me directly."
        else:
            msg = "Please fill in all fields."

    html = f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact – Scott’s Web Design</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Poppins', Arial, sans-serif;
            font-size: 1.1rem;
            line-height: 1.6;
            background-image: url("/static/images/background2.jpg");
            background-color: #2c3e50;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 8px;
        }}

        h1 {{
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 700;
            font-size: 42px;
            text-align: center;
            margin-bottom: 16px;
            color: #ffffff;
        }}

        .nav-center {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .dropdown {{
            position: relative;
            display: inline-block;
        }}

        .dropbtn {{
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 600;
            background: linear-gradient(135deg, #ff4757, #ff7a59);
            color: #ffffff;
            padding: 16px 34px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            font-size: 18px;
            box-shadow: 0 8px 18px rgba(255, 71, 87, 0.35);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
        }}

        .dropbtn:hover {{
            transform: translateY(-1px) scale(1.02);
            filter: brightness(1.05);
            box-shadow: 0 10px 22px rgba(255, 71, 87, 0.45);
        }}

        .dropdown-content {{
            display: none;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            background-color: #000000;
            min-width: 190px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.28);
            border-radius: 10px;
            z-index: 1;
            overflow: hidden;
        }}

        .dropdown-content a {{
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 500;
            color: #ff4757;
            padding: 14px 16px;
            text-decoration: none;
            display: block;
        }}

        .dropdown-content a:hover {{
            background-color: #111111;
        }}

        .dropdown:hover .dropdown-content {{
            display: block;
        }}

        .intro {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .contact-form {{
            max-width: 600px;
            margin: 0 auto;
        }}

        label {{
            display: block;
            margin: 12px 0 6px;
            font-weight: 500;
        }}

        input, textarea {{
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            font-family: 'Poppins', Arial, sans-serif;
            font-size: 1.1rem;
        }}

        textarea {{
            resize: vertical;
            min-height: 120px;
        }}

        .alert {{
            text-align: center;
            padding: 12px;
            border-radius: 8px;
            margin: 16px 0;
        }}

        .alert.error {{
            background: #aa0000;
        }}

        .alert.success {{
            background: #00aa00;
        }}

        .btn-center {{
            text-align: center;
            margin-top: 20px;
        }}

        .cta-btn {{
            font-family: 'Poppins', Arial, sans-serif;
            font-weight: 700;
            display: inline-block;
            text-align: center;
            background: linear-gradient(135deg, #3498db, #6c5ce7);
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 999px;
            text-decoration: none;
            letter-spacing: 0.2px;
            box-shadow: 0 10px 20px rgba(52, 152, 219, 0.30);
            transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
            margin: 5px 15px;
        }}

        .cta-btn:hover {{
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 14px 24px rgba(52, 152, 219, 0.40);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Scott – Scott’s Web Design</h1>

        <!-- Main navigation -->
        <div class="nav-center">
            <div class="dropdown">
                <button class="dropbtn">Menu ▼</button>
                <div class="dropdown-content">
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/services">Services</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </div>

        <div class="intro">
            <p>Have a project, question, or just want to chat about your business website? Fill out the form and I’ll get back to you.</p>
        </div>

        {f'<div class="alert success">{msg}</div>' if msg and "Thank you" in msg else ''}
        {f'<div class="alert error">{msg}</div>' if msg and "Sorry" in msg else ''}
        {f'<div class="alert error">{msg}</div>' if msg and "Please fill" in msg else ''}

        <form class="contact-form" method="POST">
            <label for="name">Your Name</label>
            <input type="text" id="name" name="name" placeholder="Enter your name">

            <label for="email">Your Email</label>
            <input type="email" id="email" name="email" placeholder="Enter your email">

            <label for="message">Message</label>
            <textarea id="message" name="message" placeholder="Tell me about your business or project..."></textarea>

            <div class="btn-center">
                <button type="submit" class="cta-btn">Send Message</button>
            </div>
        </form>

        <div class="btn-center" style="margin-top: 20px;">
            <a class="cta-btn" href="/about">About</a>
            <a class="cta-btn" href="/services">Services</a>
        </div>
    </div>
</body>
</html>
    """
    return html
if __name__ == "__main__":
    app.run(debug=True)