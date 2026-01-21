Dealer Management & Field Visit

Module Technical Name: fd_dealer_mgmt_fixed10

Odoo Version: 16+ (compatible with multi‑company & modern stock models)

Author: Nasar A Tawhid

License: LGPL‑3

📌 Overview
FD Dealer Management & Field Visit is a custom Odoo module designed to manage Dealer master data, Sales Executive field visits, and generate Executive‑wise Field Visit Reports.
The module enables sales teams to:

Maintain dealer master records within Contacts

Record daily dealer visit activities

Track targets, achievements, lifting, inquiries, retail & stock

Generate management‑ready PDF reports of executive field activity


Folder Structure

fd_dealer_mgmt_fixed10/

├── __init__.py

├── __manifest__.py

│

├── data/

│   └── sequence.xml

│

├── models/

│   ├── __init__.py

│   ├── res_partner.py

│   └── dealer_visit.py

│

├── wizard/

│   ├── __init__.py

│   ├── exec_visit_report_wizard.py

│   └── exec_visit_report_wizard_views.xml

│

├── views/

│   ├── res_partner_dealer_view.xml

│   ├── res_partner_dealer_search.xml

│   ├── dealer_visit_views.xml

│   └── menu.xml

│

├── report/

│   ├── exec_visit_report_actions.xml

│   └── exec_visit_report_templates.xml

│

└── security/

    └── ir.model.access.csv
		
