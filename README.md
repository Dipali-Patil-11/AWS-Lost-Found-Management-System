# 🏷️ Lost & Found Management System using AWS Cloud

A serverless Lost & Found Management System built using AWS Lambda, API Gateway, Amazon S3, DynamoDB, and EC2. This project allows users to report lost or found items by uploading item details and an image, which are securely stored in AWS services. The responsive frontend is hosted on an Amazon EC2 instance and communicates with the backend through Amazon API Gateway.

## 🚀 Project Overview

The Lost & Found Management System simplifies the process of reporting, searching, and managing lost or found items.

Users can:

- 📤 Report a Lost or Found item
- 🖼️ Upload an image of the item
- 📋 View all reported items
- 🔍 Search an item using its unique ID
- 🗑️ Delete an item along with its image
- 🌐 Access the application through a web interface hosted on Amazon EC2

The backend follows a serverless architecture, making the application scalable, lightweight, and cost-effective.

## 🏗️ Architecture
```text
                     Users
                       │
                       ▼
            Amazon EC2 (Frontend Hosting)
                       │
          HTML • CSS • JavaScript
                       │
                       ▼
           Amazon API Gateway (REST API)
                       │
                       ▼
          AWS Lambda (Single Backend Function)
                │                     │
                ▼                     ▼
      Amazon DynamoDB           Amazon S3
    (Item Information)      (Uploaded Images)
```

## ☁️ AWS Services Used
| AWS Service | Purpose |
| ----------- | ------- |
| Amazon EC2 | Hosts the frontend website |
| Amazon API Gateway | Exposes REST APIs |
| AWS Lambda | Handles all backend logic |
| Amazon DynamoDB | Stores item information |
| Amazon S3 | Stores uploaded item images |
| AWS IAM | Manages service permissions |
| Amazon CloudWatch | Logs and monitoring |

## 📂 DynamoDB Table

**Table Name**: `LostFoundItems`

**Attributes**
| Attribute | Type |
| --------- | ---- |
| itemId | Partition Key (String) |
| name | String |
| description | String |
| location | String |
| date | String |
| status | String |
| image | String (URL) |

## 📡 REST APIs

### 1️⃣ Report Item
- **POST** `/report`
- Uploads the image to Amazon S3 and stores item details in DynamoDB.

### 2️⃣ Get All Items
- **GET** `/items`
- Returns all reported items.

### 3️⃣ Search Item
- **GET** `/items?itemId=id`
- Returns a specific item using its unique ID.

### 4️⃣ Delete Item
- **DELETE** `/delete?itemId=id`
- Deletes the record from DynamoDB and removes the corresponding image from Amazon S3.

## 📸 Application Features
- Responsive User Interface
- Report Lost/Found Items
- Upload Item Images
- View All Reported Items
- Search by Item ID
- Delete Items
- Store Images in Amazon S3
- Store Metadata in DynamoDB
- REST API Integration
- Frontend Hosted on Amazon EC2

## 📁 Project Structure
```text
LostFoundSystem/
│
├── LOSTFOUND.html          # Frontend UI (HTML, CSS, JS)
├── lambda.py               # Backend AWS Lambda logic
├── Demo/                   # Project demonstration files
├── Screenshots/            # UI screenshots
├── Sample Images/          # Sample images for testing
└── README.md               # Project documentation
```

## 🔄 Project Workflow
1. User opens the web application hosted on Amazon EC2.
2. User fills in the Lost/Found item details.
3. User uploads an image.
4. Frontend converts the image into Base64 format.
5. API Gateway receives the request.
6. Lambda uploads the image to Amazon S3.
7. Lambda stores item details and image URL in DynamoDB.
8. User can view all reported items.
9. User can search an item using its unique ID.
10. User can delete an item, which removes both the DynamoDB record and the corresponding image from S3.

## 💻 Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- AWS Lambda

### Cloud Services
- Amazon EC2
- Amazon API Gateway
- Amazon S3
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## 🌟 Key Features
- Serverless Backend
- REST API Architecture
- Cloud Image Storage
- Secure Data Storage
- Responsive Web Interface
- Single Lambda Function for All APIs
- Event-Driven Architecture
- Scalable AWS Cloud Deployment

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:
- Building REST APIs using Amazon API Gateway
- Developing serverless applications using AWS Lambda
- Working with Amazon DynamoDB for NoSQL data storage
- Uploading and managing files in Amazon S3
- Hosting frontend applications on Amazon EC2
- Configuring IAM Roles and Permissions
- Debugging applications using Amazon CloudWatch
- Integrating frontend applications with AWS cloud services

## 📌 Future Enhancements
- User Authentication using Amazon Cognito
- Email Notifications using Amazon SNS
- Admin Dashboard
- Item Matching using Amazon Rekognition
- QR Code Integration
- Mobile Responsive Enhancements
- Search Filters and Pagination

## 👨‍💻 Author

**Dipali Arjun Patil**  
*AWS | Python | AI & ML | Cloud Computing Enthusiast*  

⭐ If you found this project useful, consider giving it a Star on GitHub!
