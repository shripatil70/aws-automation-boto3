# AWS Infrastructure Automation using Python (boto3)

## 📌 Overview

This project automates the provisioning of core AWS infrastructure using Python and boto3, eliminating manual setup through the AWS Console. It follows an Infrastructure-as-Code (IaC) approach to create and configure cloud resources programmatically.

---

## 🎯 Objectives

* Automate AWS resource creation without manual clicks
* Deploy a working web application on EC2
* Follow DevOps and Infrastructure-as-Code practices

---

## 🧰 AWS Services Used

* IAM (User, Role, Instance Profile)
* EC2 (Virtual Server)
* S3 (Storage Bucket)
* Security Groups (Firewall Rules)

---

## ⚙️ Features

* ✅ IAM user and role creation
* ✅ Instance profile attachment to EC2
* ✅ S3 bucket provisioning
* ✅ Security group configuration (HTTP access)
* ✅ EC2 instance launch
* ✅ Automated Flask app deployment using UserData
* ✅ Idempotent scripts (safe to re-run without failure)

---

## 🏗️ Architecture

User → EC2 Instance → Flask App → Browser Access

---

## 📂 Project Structure

```
aws-automation/
│── main.py
│── config.py
│── iam_setup.py
│── s3_setup.py
│── ec2_setup.py
│── security_group.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```
git clone https://github.com/<your-username>/aws-automation-boto3.git
cd aws-automation
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure AWS Credentials

```
aws configure
```

### 4️⃣ Run the Script

```
python main.py
```

---

## 🌐 Output

After execution, the script:

* Launches an EC2 instance
* Deploys a Flask application
* Prints a public IP

Open in browser:

```
http://<public-ip>
```

---

## 🖥️ Sample Output

## 🖥️ Sample Output  

### 🔹 EC2 + Flask Output
![Flask Output](https://aws-resource-provisioning.s3.ap-south-1.amazonaws.com/Output.png)

### 🔹 AWS Resources Created
![AWS Resources](https://aws-resource-provisioning.s3.ap-south-1.amazonaws.com/instances.png)

---

## ⚠️ Important Notes

* Do NOT upload `.pem` key files
* Do NOT expose AWS access keys
* Ensure Security Group allows port 80
* Public IP changes if instance is stopped

---

## 🧠 Key Learnings

* Infrastructure as Code (IaC)
* AWS automation using boto3
* EC2 provisioning and networking
* Secure credential management
* Debugging real-world deployment issues

---

## 🚀 Future Improvements

* Add HTTPS using Load Balancer
* Use Elastic IP for static address
* Add domain name (Route 53)
* Convert project to Terraform
* Implement CI/CD pipeline

---

## 📄 License

This project is for educational purposes.

---

## 👩‍💻 Author

Dhanashri Patil
