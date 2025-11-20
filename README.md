🚨 Why I Built This Project: Understanding Real Cloud Outages
Simulating How AWS, Cloudflare, and Azure Outages Happen — And How Cloud Engineers Fix Them

Over the past year, several major cloud providers — AWS, Cloudflare, Azure, Microsoft — experienced large-scale outages that took down hundreds of apps and businesses.

I kept asking myself:

“Why do these outages happen? And how do cloud / SRE engineers fix them in real time?”

Instead of Googling it…
I built a full serverless microservices system and intentionally broke it, then diagnosed and fixed the outage like a real cloud engineer.

This project is the result.


🚀 AWS Serverless Microservices — Outage Simulation & Recovery

A production-style, 3-service microservices architecture built using:

AWS Lambda

API Gateway (HTTP API)

CloudWatch Metrics & Logs

Python

Includes a realistic outage simulation, debugging workflow, and recovery process — the exact steps cloud engineers follow during real incidents.


🧱 Architecture Overview

This system uses three independent microservices, each running as its own Lambda function:

1️⃣ Auth Service

Simple health check

Mimics authentication systems in real apps

2️⃣ Product Service

Returns mock products

Represents catalog / inventory microservices

3️⃣ Payment Service (most important)

Broken Version → throws errors (simulated outage)

Fixed Version → returns healthy JSON

Demonstrates realistic dependency failure & recovery

These services are wired through API Gateway, just like real production APIs.

💥 Realistic Cloud Outage Simulation

To replicate how real outages happen (like the AWS / Cloudflare ones), I forced the payment service to fail:
raise Exception("Simulated payment service failure")

This created a chain of events identical to real incidents:
❌ API Gateway returned 500 errors
📉 CloudWatch error metrics spiked
🔍 Logs captured stack traces
🛑 Payment flow became unavailable

This is EXACTLY how outages start in real microservice-based environments.

🔧 Diagnosis & Recovery (Real Cloud Engineering Process)

After simulating the outage, I:

1. Investigated CloudWatch Metrics

Saw error count increase → confirmed the failure.

2. Checked CloudWatch Logs

Found the forced exception → root cause identified.

3. Redeployed a fixed version of the payment service:
{
  "service": "payment-service",
  "status": "ok",
  "message": "payment service reachable",
  "timestamp": 123456
}

4. Validated the fix

Errors dropped

Invocations succeeded

Service returned to green

This entire cycle — break → detect → diagnose → fix → validate — mirrors real SRE / CloudOps workflows

🌐 API Endpoints
Method	Route	Service
GET	/auth	Auth Service
GET	/product	Product Service
GET	/pay	Payment Service (Broken)
GET	/pay-fixed	Payment Service (Healthy)

📸 Screenshots Included (Full Walkthrough)

Inside the /screenshots folder, you’ll find:

API Gateway configuration

Lambda functions list

Working /auth and /product responses

Broken payment service (500 error)

Fixed payment service

CloudWatch error spike during outage

CloudWatch recovery after fix

These screenshots tell the full story of the outage and recovery.

🎯 Final Thoughts

This project wasn’t just about writing code — it was a real experiment in understanding how cloud outages happen at companies like AWS, Cloudflare, and Azure.

By intentionally breaking a microservice, tracing the failure, analyzing metrics, and restoring the system, I recreated the exact workflow cloud and security engineers follow during real incidents.

This project demonstrates curiosity, real engineering thinking, and hands-on AWS experience — not just theory.

It reflects how I approach problems:
break it, analyze it, understand it, fix it, and make it better.
