Diligent Hiring Assessment – A-SDLC Task (Cursor)

Candidate Name: [Your Full Name]
Assessment: Diligent – Develop with Cursor (A-SDLC)
Duration: 30 minutes
Status: Completed Successfully
Submitted: AI-assisted via Cursor IDE + GitHub

------------------------------------------------------------------------

This repository contains the complete end-to-end solution for the A-SDLC
(AI-Software Development Life Cycle) assessment.

Demonstrated skills:

-   GitHub version control
-   AI-prompted Python code generation
-   Synthetic e-commerce data creation
-   SQLite ingestion pipeline
-   Multi-table SQL JOIN queries
-   Clean, modular, documented code

------------------------------------------------------------------------

Project Structure

├── generate_data.py # Generates 5 synthetic CSV files ├──
ingest_to_sqlite.py # Loads CSVs → SQLite (ecom.db) ├── run_query.py #
Executes JOIN query & prints report │ ├── users.csv # Users (ID, name,
email) ├── products.csv # Products (ID, name, price) ├── orders.csv #
Orders (ID, user_id, date) ├── order_items.csv # Order items (order_id,
product_id, qty) ├── payments.csv # Payments (order_id, amount) │ ├──
ecom.db # Final SQLite database │ └── README.md # This file

------------------------------------------------------------------------

Step 1: Generate Synthetic Data

Run:

    python generate_data.py

Output:
✔️ 5 realistic e-commerce CSV files generated using Faker

------------------------------------------------------------------------

Step 2: Ingest Into SQLite

    python ingest_to_sqlite.py

Creates ecom.db with tables:

-   users
-   products
-   orders
-   order_items
-   payments

------------------------------------------------------------------------

Step 3: Run SQL JOIN Query

    python run_query.py

Example output (sample):

order_id | customer | product | quantity | amount | order_date
1001 | Alice Johnson | Wireless Mouse | 2 | 599.98 | 2025-11-01
1002 | Bob Smith | USB-C Cable | 1 | 199.99 | 2025-11-02

------------------------------------------------------------------------

Technologies Used

Python 3
Faker
Pandas
SQLite
Cursor IDE
GitHub

------------------------------------------------------------------------

Assessment Focus Areas (All Met)

AI-assisted code generation – Completed
Generate 5 synthetic CSV files – Completed
SQLite ingestion pipeline – Completed
Multi-table SQL JOIN – Completed
Clean, modular scripts – Completed
Full pipeline (Gen→Load→Query) – Completed
GitHub push + documentation – Completed

------------------------------------------------------------------------

How to Run the Full Workflow

    python generate_data.py
    python ingest_to_sqlite.py
    python run_query.py

------------------------------------------------------------------------

AI Development Note

All scripts were generated and refined using Cursor IDE with targeted
prompts.

------------------------------------------------------------------------

GitHub Repository

https://github.com/SrustiSulipalmath/diligent-a-sdlc-assessment

------------------------------------------------------------------------

THANK YOU FOR THE OPPORTUNITY!
