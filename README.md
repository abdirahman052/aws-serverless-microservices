🚨 Why I Built This Project

*Understanding Real Cloud Outages — and Recreating How Cloud Engineers Diagnose & Fix Them*

For years, major cloud platforms like AWS and Microsoft Azure have had outages that disrupted thousands of apps and businesses.

Those outages made me wonder:

“What actually causes critical cloud services to go down — and how do Cloud, SRE, and Security Engineers bring them back online?”

I didn’t want a theoretical explanation — I wanted the real engineering experience.

So I built a full serverless microservices system, intentionally broke part of it, then diagnosed and restored it the same way real cloud engineers handle production incidents.

This project is the result.

---

🚀 AWS Serverless Microservices — Outage Simulation & Recovery

A production-style microservices environment built using:

- AWS Lambda

- API Gateway (HTTP API)

- CloudWatch Metrics & Logs

- Python

This project includes:

- A simulated microservice outage

- Real failure signals (500 errors, CloudWatch spikes, logs)

- A full debugging workflow

- Complete service recovery

- Validation of system health

Exactly how AWS/Azure engineers operate during real incidents.

---

🧱 Architecture Overview

This system consists of three isolated microservices, each deployed as its own AWS Lambda function:

---

1️⃣ Auth Service

- Returns a basic health check

- Represents authentication/identity components

---

2️⃣ Product Service

- Returns mock product data

- Mimics catalog or inventory microservices

---

3️⃣ Payment Service (Core of the Simulation)

- Broken Version → intentionally throws an exception

- Fixed Version → returns a healthy JSON response

- Demonstrates dependency failures, outages, and recovery

---

All three services are routed through API Gateway, similar to real-world distributed systems in AWS and Azure.

---



💥 Realistic Cloud Outage Simulation

To recreate the type of cascading failures seen in cloud outages, I deliberately forced the payment service to fail:

raise Exception("Simulated payment service failure")

This triggered the same patterns seen in real cloud incidents:

- ❌ API Gateway returned 500 Internal Server Errors

- 📉 CloudWatch error metrics spiked

- 🔍 Logs captured stack traces & failure signatures

- 🛑 The payment workflow became unavailable

This mirrors how a single failing microservice can impact downstream systems.

---

🔧 Diagnosis & Recovery — Real SRE Workflow

After triggering the outage, I followed an industry-style incident response cycle:



1️⃣ Investigate Metrics

- Checked CloudWatch Metrics

- Confirmed spikes in errors and failed invocations



2️⃣ Analyze Logs

- Located the exception

- Verified the root cause



3️⃣ Deploy Healthy Version

Replaced failing logic with a fixed response:

{
  "service": 
  "payment-service",
   "status": "ok",
  "message": "payment service reachable",
  "timestamp": 123456
}




4️⃣ Validate the Fix

- Error rate dropped

- Success rate returned to normal

- API Gateway responded with healthy results again



This break → detect → diagnose → fix → validate workflow is the same pattern used by CloudOps and SRE teams at AWS/Azure.

---


🌐 API Endpoints:


- GET	/auth	Auth Service
---
- GET	/product	Product Service
---
- GET	/pay	Payment (Broken)
---
- GET	/pay-fixed	Payment (Healthy)

---

📸 Screenshot Walkthrough

The /screenshots folder includes:

- API Gateway configuration

- Lambda functions overview

- Healthy /auth response

- Healthy /product response

- Broken /pay response (500 error)

- Fixed /pay-fixed response

- CloudWatch error spike

- CloudWatch recovery after the fix

These images show the full outage → diagnosis → recovery lifecycle.

---

⭐ What This Project Demonstrates
Cloud Engineering

- Serverless architecture

- API Gateway routing

- Isolated microservices

- AWS operational knowledge

SRE / CloudOps

- Fault injection

- Incident analysis

- Observability (logs, metrics, error rates)

- Root cause identification

- Progressive recovery

Cybersecurity (Availability)

- Service resilience

- Failure impact analysis

- High-availability concepts

- Recovery validation

🎯 Final Thoughts

This wasn’t just a coding project —
it was an experiment in understanding how real cloud outages happen and how engineers bring systems back online.

By intentionally breaking a microservice, analyzing the blast radius, examining CloudWatch data, and restoring service health, I recreated the workflows used by real Cloud, DevOps, Security, and SRE teams.

This project reflects my engineering mindset:

Understand it → Break it → Observe it → Fix it → Improve it.
