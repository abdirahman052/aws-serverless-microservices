🚨 Why I Built This Project
Understanding Real Cloud Outages — and Recreating How Cloud Engineers Diagnose & Fix Them

For years we’ve seen major outages hit platforms like AWS and Microsoft Azure, bringing down authentication systems, APIs, applications, and entire services around the world.

Those outages always made me wonder:

“What actually causes critical cloud services to go down — and how do Cloud, SRE, and Security Engineers bring them back online?”

I didn’t want the theoretical answer.
I wanted the engineering answer.

So instead of reading articles,
I built a real microservices architecture, intentionally broke part of it, and then diagnosed & restored the system exactly like cloud engineers do in production.

This project is the result.

🚀 AWS Serverless Microservices — Outage Simulation & Recovery

A production-style microservices environment built using:

AWS Lambda

API Gateway (HTTP API)

CloudWatch Metrics & Logs

Python (serverless runtime)

It includes a simulated service outage, real failure signals, monitoring analysis, and a full debugging + recovery workflow — the same approach used during real AWS/Azure incident response.

🧱 Architecture Overview

The architecture consists of three isolated microservices, each deployed as an independent AWS Lambda function:

1️⃣ Auth Service

Basic health check

Represents authentication/identity components

2️⃣ Product Service

Returns mock product data

Mimics catalog or inventory microservices

3️⃣ Payment Service (The Core of the Simulation)

Broken Version → intentionally throws an exception (simulating failure)

Fixed Version → returns a healthy JSON response

Demonstrates dependency failure, availability issues, and safe restoration

All services are exposed via API Gateway, similar to how distributed systems expose public/internal APIs in AWS and Azure.

💥 Realistic Cloud Outage Simulation

To replicate the types of cascading failures seen on AWS and Azure, I intentionally forced the payment service to fail by raising an exception:

raise Exception("Simulated payment service failure")


This instantly triggered failure patterns identical to those in real cloud outages:

❌ API Gateway returned 500 Internal Server Error
📉 CloudWatch error rate increased
🔍 Logs revealed stack traces & root cause clues
🛑 The payment workflow became unavailable

This mirrors how a single failing microservice in AWS/Azure can cause system-wide degradation.

🔧 Diagnosis & Recovery — Real SRE Workflow

After triggering the outage, I followed an SRE-style incident response cycle:

1️⃣ Investigate Metrics

Checked CloudWatch Metrics

Verified spikes in errors & failed invocations

2️⃣ Analyze Logs

Located the exception

Confirmed the exact failure point

3️⃣ Deploy Fix

Replaced the failing logic with a healthy response:

{
  "service": "payment-service",
  "status": "ok",
  "message": "payment service reachable",
  "timestamp": 123456
}

4️⃣ Validate the System

Errors dropped

Success rate returned to normal

API Gateway served healthy responses

This break → detect → diagnose → fix → validate cycle is exactly how AWS and Azure engineers manage incidents.

🌐 API Endpoints
Method	Route	Service
GET	/auth	Auth Service
GET	/product	Product Service
GET	/pay	Payment (Broken)
GET	/pay-fixed	Payment (Healthy)
📸 Full Walkthrough (Screenshots)

Inside the /screenshots folder, you’ll find:

API Gateway configuration

Lambda functions list

Healthy /auth response

Healthy /product response

Broken /pay response (500)

Fixed /pay-fixed response

CloudWatch error spike during outage

CloudWatch recovery after the fix

These screenshots document the entire engineering process.

⭐ What This Project Demonstrates
Cloud Engineering Skills

Serverless architecture

Microservice separation

API Gateway routing

AWS operational understanding

Environment isolation

SRE / CloudOps Skills

Observability (metrics, logs, failure signals)

Incident triage & root cause analysis

Failure injection (fault simulation)

Safe recovery workflows

Post-incident validation

Cybersecurity Relevance

Availability (core of the CIA Triad)

Dependency hardening

Service health monitoring

Understanding how failure impacts resilience

Cloud-native security awareness

This project mirrors the exact workflow used by AWS, Azure, FinTech, and SaaS engineering teams during real cloud failures.

🎯 Final Thoughts

This wasn’t just a coding exercise —
it was an experiment in understanding failure, resilience, and incident response in cloud environments.

By intentionally breaking a microservice, analyzing the blast radius, interpreting metrics, and restoring system health, I recreated the real-world engineering process behind major outages on AWS and Azure.

This project reflects my approach to engineering:

Understand it.
Break it.
Observe it.
Fix it.
Improve it.
