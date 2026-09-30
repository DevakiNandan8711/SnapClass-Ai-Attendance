# 📸 SnapClass — AI-Powered Attendance System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://snap-ai-attend.streamlit.app/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://snap-ai-attend.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Supabase](https://img.shields.io/badge/Database-Supabase-green.svg)](https://supabase.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🚀 **Try the Live App**: [snap-ai-attend.streamlit.app](https://snap-ai-attend.streamlit.app/)

**SnapClass** is a modern, AI-powered smart attendance platform designed to streamline classroom attendance in seconds using facial recognition and voice biometric verification. Built with Streamlit, Supabase, dlib, and Scikit-learn.

---

## ✨ Features

### 👨‍🏫 For Teachers
- **Secure Authentication**: Register and login with secure bcrypt-hashed credentials.
- **AI Classroom Photo Attendance**:
  - Capture photos in real-time or batch-upload classroom images.
  - Automatic multi-face detection, 128D facial embedding extraction, and SVM classification.
  - Interactive verification dialog: inspect detected vs. absent students before committing records.
- **Voice Attendance (Multimodal)**:
  - Audio phrase verification using deep voice embeddings via Resemblyzer and Librosa.
- **Subject Management**:
  - Create subjects with course code, name, and section.
  - Generate shareable **QR Codes** and direct join links for instant student self-enrollment.
- **Attendance Analytics & Logs**:
  - Chronological attendance records with aggregate attendance statistics per session.

### 🎓 For Students
- **FaceID Instant Login**:
  - Position your face in front of the camera for real-time authentication.
- **Smart Profile Onboarding**:
  - One-time facial biometric registration with optional voice enrollment.
- **Student Dashboard**:
  - View enrolled subjects, attendance logs, and class attendance percentages.
- **Easy Course Enrollment**:
  - Enroll via subject join code or by scanning a teacher's generated QR code.

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/) with custom responsive CSS styling
- **Face Recognition**: [dlib](http://dlib.net/), `face_recognition_models`, [scikit-learn](https://scikit-learn.org/) (SVC)
- **Voice Recognition**: [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), [librosa](https://librosa.org/)
- **Database & Cloud Backend**: [Supabase](https://supabase.com/) (PostgreSQL & PostgREST API)
- **Security**: [bcrypt](https://github.com/pyca/bcrypt/) password hashing
- **QR Code Generation**: [segno](https://github.com/heuer/segno)

---

## 📂 Project Structure

```text
SnapClass/
├── app.py                      # Main entrypoint and screen router
├── requirements.txt            # Python dependencies
├── secrets.example.toml        # Sample template for Supabase credentials
├── .gitignore                  # Git exclusions for secrets, venvs, and cache
├── src/
│   ├── components/             # Reusable UI dialogs, headers, footers & cards
│   │   ├── dialog_add_photos.py        # Photo upload/camera capture dialog
│   │   ├── dialog_attendance_results.py # Attendance confirmation modal
│   │   ├── dialog_auto_enroll.py       # Join link auto-enrollment
│   │   ├── dialog_create_subject.py    # Subject creation form
│   │   ├── dialog_enroll.py            # Manual enrollment dialog
│   │   ├── dialog_share_subject.py     # QR Code & join code generator
│   │   ├── dialog_voice_attendance.py  # Voice attendance modal
│   │   ├── footer.py                   # Custom page footer
│   │   ├── header.py                   # Custom brand header
│   │   └── subject_card.py             # Subject card component
│   ├── database/               # Database integration
│   │   ├── config.py           # Supabase client initialization
│   │   └── db.py               # Supabase CRUD operations & queries
│   ├── pipelines/              # Machine Learning pipelines
│   │   ├── face_pipelines.py   # Face landmarks, embeddings & SVM classification
│   │   └── voice_pipelines.py  # Voice embedding extraction
│   ├── screens/                # Application views
│   │   ├── home_screen.py      # Landing role-selector page
│   │   ├── student_screen.py   # Student FaceID login & dashboard
│   │   └── teacher_screen.py   # Teacher authentication, dashboard & logs
│   └── ui/
│       └── style_base_layout.py # Custom typography, colors, and layout CSS
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python**: Version `3.10` or higher (tested on Python 3.11, 3.12, and 3.13)
- **C++ Build Tools**: Required for compiling `dlib` (or install pre-compiled `dlib-bin`)
- **Git**

### 2. Clone the Repository
```bash
git clone https://github.com/DevakiNandan8711/SnapClass-Ai-Attendance.git
cd SnapClass-Ai-Attendance
```

### 3. Create and Activate a Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup (Supabase)

SnapClass uses Supabase for database storage. Set up the following tables in your Supabase SQL editor:

```sql
-- Teachers Table
create table teachers (
  teacher_id bigint generated by default as identity primary key,
  username text unique not null,
  password text not null,
  name text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Students Table
create table students (
  student_id bigint generated by default as identity primary key,
  name text not null,
  username text unique not null,
  password text not null,
  face_embedding float8[],
  voice_embedding float8[],
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Subjects Table
create table subjects (
  subject_id bigint generated by default as identity primary key,
  subject_code text not null,
  name text not null,
  section text,
  teacher_id bigint references teachers(teacher_id) on delete cascade,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Subject-Student Enrollments
create table subject_students (
  id bigint generated by default as identity primary key,
  subject_id bigint references subjects(subject_id) on delete cascade,
  student_id bigint references students(student_id) on delete cascade,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  unique(subject_id, student_id)
);

-- Attendance Logs
create table attendance_logs (
  log_id bigint generated by default as identity primary key,
  subject_id bigint references subjects(subject_id) on delete cascade,
  student_id bigint references students(student_id) on delete cascade,
  is_present boolean default false,
  timestamp timestamp with time zone default timezone('utc'::text, now()) not null
);
```

---

## 🔐 Configuring Secrets

1. Create a `.streamlit` directory in the project root (if not already present):
   ```bash
   mkdir .streamlit
   ```
2. Create `secrets.toml` inside `.streamlit/`:
   ```toml
   # .streamlit/secrets.toml
   SUPABASE_URL = "https://your-project-id.supabase.co"
   SUPABASE_KEY = "your-supabase-key"
   ```

> ⚠️ **Important Security Note**: The `.streamlit/secrets.toml` file contains confidential credentials and is excluded by `.gitignore`. **Never commit your actual `secrets.toml` file to GitHub.**

---

## 🏃 Running the Application

Launch the Streamlit app locally:
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Deployment (Streamlit Community Cloud)

1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Connect your repository, set the main file path to `app.py`, and branch to `main`.
4. Under **Advanced settings → Secrets**, paste your Supabase configuration:
   ```toml
   SUPABASE_URL = "https://your-project-id.supabase.co"
   SUPABASE_KEY = "your-supabase-key"
   ```
5. Click **Deploy!**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
