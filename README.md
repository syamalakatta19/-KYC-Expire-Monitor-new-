KYC-Expire-Monitor
KYC Document Expiry Monitor for Bank Branches
📌 Project Overview
The KYC Document Expiry Monitor for Bank Branches is a web-based banking compliance application developed using Python Flask, SQLite, HTML, and CSS.

The system helps bank branches maintain customer KYC information and identify documents that are expired or going to expire soon.

The application also handles different Date of Birth (DOB) formats and provides a branch-wise pending KYC report.

🎯 Problem Statement
Banks maintain a large amount of customer KYC information. Manually checking KYC document expiry dates can be time-consuming and may result in missed renewals.

The main problems addressed by this project are:

KYC documents may expire without timely renewal.
Customer DOB may be stored in different date formats.
Banks need to identify customers whose KYC is expired or expiring soon.
Branch-wise pending KYC information is required for monitoring.
Joint account holders may have separate KYC dates.
💡 Objectives
The main objectives of this project are:

Store customer KYC information digitally.
Validate different DOB formats.
Monitor KYC document expiry dates.
Identify expired KYC documents.
Identify documents expiring within 30 days.
Generate branch-wise pending KYC reports.
Reduce manual KYC monitoring work.
Improve banking compliance tracking.
✨ Features
1. Customer Registration
The application allows users to enter:

Customer ID
Customer Name
Account Number
Branch
Date of Birth
Document Type
KYC Expiry Date
Holder Type
The customer information is stored in an SQLite database.

2. DOB Format Validation
The system accepts multiple DOB formats:

DD-MM-YYYY
DD/MM/YYYY
YYYY-MM-DD
The application converts valid DOB values into the standard:

YYYY-MM-DD

This helps solve the problem of inconsistent DOB formats.

3. KYC Expiry Monitoring
The system automatically checks the KYC expiry date.

KYC status is classified as:

Status	Condition
Expired	Expiry date has already passed
Expiring Soon	Expiry is within 30 days
Valid	More than 30 days remaining
Invalid Date	Incorrect expiry date format
The expiry calculation is implemented in the Flask backend. :contentReference[oaicite:2]{index=2}

4. Branch-wise KYC Report
The application provides a branch-wise report.

The report displays customers whose KYC status is:

Expired
Expiring Soon
For example:

/report?branch=Vijayawada
