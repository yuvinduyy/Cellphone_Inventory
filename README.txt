
Cell Phone Inventory Management System

## Project Overview

This application is a data-structure-centered inventory solution designed to manage mobile device stock for both **Marketing** and **Engineering** teams. It allows for the tracking of technical specifications, pricing, and stock levels using a high-performance Hash Map (Dictionary) design.



## Key Features

Inventory Tracking: Add, remove, and search for devices using unique IMEI identifiers.

Technical Specifications: Detailed hardware tracking including CPU, RAM, Storage, and Battery for Engineering needs.

Marketing Integration: Manage retail pricing, condition status (New/Refurbished/Used), and promotional marketing tags.

Data Integrity: Input validation using regular expressions and Enums to ensure numeric and status consistency.





## Prerequisites

Python 3.7 or higher is required due to the use of `dataclasses`, `enums`, and dictionary insertion order preservation.



## Installation & Setup

1. Download the `inventory.py` file to your local machine.


2. Open your terminal or command prompt.


3. Navigate to the directory containing the file.




## How to Run

Execute the program by running the following command:

```bash
python inventory.py

```



## Usage Instructions

Upon launching, a command-line interface (CLI) menu will appear. Follow the on-screen prompts:

1. Add Phone: Enter the device details step-by-step. Note that IMEI must be unique.


2. Remove Phone: Enter the IMEI of the device you wish to delete from the records.


3. Search Phone: Quickly retrieve full details for a device using its IMEI.


4. View Inventory: Display a comprehensive list of all devices currently in stock.


5. Exit: Securely close the application.






## Technical Design Rationale

Primary Data Structure: Python Dictionary (Hash Map). This choice ensures that searching for a device by IMEI occurs in  time, regardless of inventory size.


Attribute Management: Uses structured objects for specifications to support complex engineering data while maintaining a flat structure for basic marketing attributes.


For more,
Git Hub - yuvinduyy

-----------Thank you!!! ------------------
