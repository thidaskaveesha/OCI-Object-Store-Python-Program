# 📦 OCI Object Storage Upload Tool

## 🚀 Overview

This project demonstrates how to use Oracle Cloud Infrastructure (OCI) Python SDK to:

- Create an Object Storage bucket if it does not already exist
- Upload files to the bucket
- Authenticate using OCI config file
- Handle service errors like bucket conflicts gracefully

This project is created as part of my Oracle ACE Apprentice contribution milestone to demonstrate real OCI product usage and cloud automation skills.

---

## 🏗️ Architecture

Local Machine  
↓  
OCI Python SDK  
↓  
Oracle Cloud Infrastructure (OCI)  
↓  
Object Storage Namespace  
↓  
Bucket (auto-created if not exists)  
↓  
Uploaded Files (Objects)

---

## ⚙️ Features

- Auto-create OCI bucket if missing
- Upload local files to Object Storage
- Uses OCI SDK authentication
- Handles "bucket already exists" errors safely
- Simple and reusable Python script

---

## 🧰 Tech Stack

- Python 3.x  
- Oracle Cloud Infrastructure SDK (oci)  
- OCI Object Storage Service  

---

## 📦 Installation

### Install OCI SDK

pip install oci

---

## 🔐 OCI Configuration

Create your OCI config file at:

~/.oci/config

Example configuration:

[DEFAULT]
user=ocid1.user.oc1..
fingerprint=xx:xx:xx:xx:xx
key_file=/path/to/privatekey.pem
tenancy=ocid1.tenancy.oc1..
region=us-ashburn-1

---

## ▶️ How to Run

### Step 1: Create a file

Create a file named:

file.txt

---

### Step 2: Run script

python upload.py

---

## 📜 How It Works

### 1. Initialize OCI Client
Loads OCI config and creates Object Storage client.

### 2. Get Namespace
OCI uses a namespace for all object storage operations.

### 3. Create Bucket
Creates bucket if it does not exist.

If bucket already exists, it safely skips creation.

### 4. Upload File
Uploads file using put_object API into the bucket.

---

## 🧪 Example Output

First run:

Bucket 'my-bucket' created successfully.
File uploaded successfully.

Next runs:

Bucket already exists, skipping creation.
File uploaded successfully.

---

## 📁 Project Structure

oci-object-storage-uploader/
│
├── upload.py
├── file.txt
└── README.md

---

## 📸 Screenshots (For ACE Submission)

Include:

- OCI bucket created in console
- Uploaded file visible in Object Storage
- Terminal execution output
- Timestamp visible screenshots

---

## 🎯 What I Learned

- OCI Object Storage architecture (namespace, buckets, objects)
- Using OCI Python SDK
- Creating cloud resources programmatically
- Error handling in cloud APIs
- Real-world cloud automation workflow

---

## 🚀 Future Improvements

- Upload entire folders recursively
- Add CLI arguments (file + bucket input)
- Add file versioning support
- Build REST API using Flask or FastAPI
- Add logging system
- Integrate with GitHub Actions CI/CD

---

## 👨‍💻 Author

Created as part of Oracle ACE Apprentice Program contribution milestone.

---

## 📌 License

Educational use only for Oracle ACE learning contributions.