
# 📦 Cloud-Native File Storage Microservice

A lightweight, scalable backend microservice built with Flask and AWS S3 for secure file uploads, downloads, and listing. Designed for cloud-native deployments with Docker and optimized for minimal latency and high reliability.

---

## 🚀 Features
- Upload, download, and list files securely via RESTful APIs.
- Integrated with AWS S3 for scalable and durable file storage.
- Health-checked and containerized using Docker and Docker Compose.
- Supports concurrent file operations with minimal latency (<100ms uploads).
- Modular, production-ready Flask app structure.
- Gunicorn-based deployment for better concurrency and performance.

---

## 🛠 Tech Stack
- **Backend:** Flask, Gunicorn
- **Cloud Storage:** AWS S3
- **Containerization:** Docker, Docker Compose
- **Infrastructure:** AWS (S3, IAM)
- **Language:** Python 3.10

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|:---|:---|:---|
| `POST` | `/upload` | Upload a file to S3 |
| `GET` | `/download/<filename>` | Download a file from S3 |
| `GET` | `/list` | List all files in the S3 bucket |

---

## 📦 Project Structure

cloud-native-file-storage/
├── app/
│   ├── init.py
│   ├── routes.py
│   ├── s3_utils.py
│   ├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── run.py
└── README.md

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cloud-native-file-storage.git
   cd cloud-native-file-storage
   ```

2.	Set up AWS credentials:
    Create a .env file in the root directory:
    ```bash
    AWS_ACCESS_KEY_ID=your-access-key
    AWS_SECRET_ACCESS_KEY=your-secret-key
    AWS_BUCKET_NAME=your-s3-bucket
    AWS_REGION=your-region
    ```

3. 	Build and run with Docker Compose:
    ```bash
    docker-compose up --build
    ```

4.	Access the API: 
    Open Postman or your browser and use:
    ```bash
    http://localhost:5000/upload
    http://localhost:5000/download/<filename>
    http://localhost:5000/list
    ```

🧹 To-Do (Future Enhancements)
	• Add JWT-based authentication.
	• Enable direct client-to-S3 uploads using pre-signed URLs.
	• Add file size and type validations.
	• Set up CI/CD pipeline for automated deployments.
	• Implement retry logic and exponential backoff on S3 interactions.

⸻

🧠 Lessons Learned
	• Implementing stateless services with Flask and AWS.
	• Handling concurrent file operations reliably.
	• Best practices for containerizing Python microservices.
	• Integrating AWS S3 with robust error handling.

👨‍💻 Author
	• Rahul Saxena
