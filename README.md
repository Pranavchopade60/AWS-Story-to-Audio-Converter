# 🔊 AWS Story to Audio Converter

A serverless **Story to Audio Converter** built using **Amazon Polly, AWS Lambda, Amazon API Gateway, Amazon S3, Amazon DynamoDB, Amazon EC2, HTML, CSS, and JavaScript**. The application allows teachers or users to upload stories as text, automatically converts them into natural-sounding speech using Amazon Polly, stores the generated audio in Amazon S3, and provides an easy-to-use web interface for listening and downloading audio files.

---

```

---

# 📸 Screenshots

## Dashboard

![Dashboard](screenshots/Story to Audio Converter.png)


---

# ✨ Features

- Upload Stories as Text
- Convert Text to Natural Speech
- Multiple Amazon Polly Voices
- Generate High-Quality MP3 Audio
- Store Stories in Amazon S3
- Store Audio Files in Amazon S3
- Maintain Story History
- Download Generated Audio
- Built-in Audio Player
- Responsive Dashboard
- REST APIs using API Gateway
- Fully Serverless Backend
- CloudWatch Monitoring

---

# 🏗 Architecture

```
Teacher / User
      │
      ▼
Amazon EC2 (Web Application)
      │
      ▼
Amazon API Gateway
      │
      ▼
AWS Lambda
      │
      ├────────────► Amazon Polly
      │                   │
      │                   ▼
      │           Generate Speech (MP3)
      │
      ├────────────► Amazon S3
      │                   │
      │                   ▼
      │          Store Stories & Audio
      │
      ▼
Amazon DynamoDB
      │
      ▼
Story Metadata & History
```

---

# ☁️ AWS Services Used

- Amazon EC2
- Amazon Polly
- AWS Lambda
- Amazon API Gateway
- Amazon S3
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

---

# 💻 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

## Backend

- Python
- AWS Lambda

## AI Service

- Amazon Polly

## Cloud

- Amazon EC2
- Amazon API Gateway
- Amazon S3
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

---

# 📁 Project Structure

```
AWS-Story-to-Audio-Converter
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets
│
├── lambda
│   ├── uploadStory.py
│  
├── screenshots
│   ├── dashboard.png
│  
│
└── README.md
```

---

# ⚙️ API Endpoints

## Upload Story

```
POST /story
```

Request Body

```json
{
    "title": "The Lion and the Mouse",
    "content": "Once upon a time..."
}
```

---

## Convert Story to Audio

```
POST /convert
```

---

## Get Story History

```
GET /stories
```

---

## Play Audio

```
GET /audio?id=123
```

---

## Delete Story

```
DELETE /story?id=123
```

---

# 🔊 Audio Generation Workflow

1. User enters or uploads a story.
2. Story is sent to AWS Lambda through API Gateway.
3. Lambda invokes Amazon Polly.
4. Amazon Polly converts the text into an MP3 audio file.
5. The generated audio is stored in Amazon S3.
6. Story details and audio metadata are stored in DynamoDB.
7. The web application displays the audio player.
8. Users can play or download the generated audio.

---

# 🌍 Supported Amazon Polly Features

- Neural Text-to-Speech
- Natural Human-Like Voices
- Multiple Languages
- Multiple Voice Options
- MP3 Audio Output
- Fast Audio Generation
- High-Quality Speech Synthesis

---

# 🚀 Deployment

The frontend is hosted on an Ubuntu EC2 instance using Apache Web Server.

AWS Lambda handles all backend processing.

Amazon API Gateway exposes REST APIs.

Amazon Polly converts uploaded text into speech.

Amazon S3 stores both stories and generated audio files.

Amazon DynamoDB stores story metadata and conversion history.

Amazon CloudWatch provides logging and monitoring.

---

# 🔐 IAM Permissions

The Lambda execution role requires:

- polly:SynthesizeSpeech
- s3:GetObject
- s3:PutObject
- s3:DeleteObject
- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:Scan
- dynamodb:DeleteItem
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AWS-Story-to-Audio-Converter.git
```

Navigate to the project

```bash
cd AWS-Story-to-Audio-Converter
```

Deploy the frontend to Amazon EC2.

Create an Amazon S3 bucket for storing stories and audio files.

Deploy the Lambda functions.

Create the DynamoDB table.

Configure Amazon Polly permissions.

Create API Gateway endpoints.

Update the API URLs inside `script.js`.

Launch the application.

---

# 🔮 Future Improvements

- PDF to Audio Conversion
- DOCX File Support
- Multiple Voice Selection
- Speed & Pitch Controls
- Multi-Language Translation
- Audiobook Playlist
- User Authentication with Amazon Cognito
- Story Categories
- AI Story Summarization
- Voice Preview
- Mobile Responsive PWA
- Download History
- Audio Streaming Support

---

# 👨‍💻 Author

**Pranav Chopade**



---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.
