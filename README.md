# Fitness & Wellness Management System — Frappe / ERPNext v15+

A comprehensive Frappe/ERPNext custom application to manage the complete fitness business value chain — from member onboarding and subscription management through class scheduling, trainer management, equipment maintenance, health assessments, nutrition planning, and billing.

## Features

- **👥 Member & Subscription Management** — Full lifecycle tracking, membership plans, automated renewals, attendance check-ins, and subscription freezing.
- **📅 Class & Schedule Management** — Dynamic class types, recurring timetables, batch enrollment, waitlisting, and attendance capture.
- **🏋️ Trainer & Staff Management** — Trainer profiles, shift availability, class assignments, personal training slots, and commission calculations.
- **🏢 Facility & Equipment Management** — Equipment registry, maintenance scheduling, AMC contracts, locker assignment.
- **🩺 Health & Fitness Assessment** — Health profiling, detailed body metric logs, progress photos, and fitness goal tracking.
- **🍏 Nutrition & Diet Management** — Custom diet plans, meal templates, calorie tracking, and supplement logging.
- **💸 Billing & Finance** — POS walk-in payments, subscription invoices, EMI schedules, and daily cash reconciliation.
- **📈 Reports & Analytics** — Member retention metrics, trainer performance scorecards, class popularity, and P&L dashboards.

## Directory Structure

```
fitness_wellness/                  ← Frappe app root
├── setup.py
├── requirements.txt
├── pyproject.toml
└── fitness_wellness/              ← Python package
    ├── __init__.py                ← Version string
    ├── hooks.py                   ← App configuration hub
    ├── patches.txt
    ├── utils/                     ← Shared utilities
    │   ├── __init__.py
    │   ├── calculations.py        ← Proration, EMI, commission engine
    │   ├── notifications.py       ← SMS/email triggers
    │   └── validators.py
    │
    ├── member_management/         ← Module: Members & Subscriptions
    │   ├── __init__.py            ← Doc events
    │   ├── doctype/
    │   └── report/
    │
    ├── class_management/          ← Module: Classes & Schedules
    │   ├── __init__.py            ← Doc events
    │   ├── doctype/
    │   └── report/
    │
    ├── trainer_management/        ← Module: Trainers & Staff
    ├── facility_management/       ← Module: Facility & Equipment
    ├── health_assessment/         ← Module: Health & Metrics
    ├── nutrition/                 ← Module: Diet & Nutrition
    │
    ├── billing/                   ← Module: Invoicing & Finance
    │   ├── __init__.py            ← Doc events
    │   ├── doctype/
    │   └── report/
    │
    ├── config/                    ← Desk workspaces and docs
    │   ├── desktop.py
    │   └── docs.py
    │
    ├── fixtures/                  ← Custom fields and roles
    │
    └── tasks.py                   ← Scheduled tasks (Daily, Weekly, Monthly)

public/
├── js/
└── css/
```

## Installation

```bash
# Inside your Frappe bench directory
bench get-app fitness_wellness https://github.com/nick200555/fitness_wellness.git
bench --site your.site.name install-app fitness_wellness
bench --site your.site.name migrate
```

## Roles Required

| Role | Access |
|------|--------|
| **Front Desk Executive** | Create members, check-ins, class bookings, walk-in payments |
| **Fitness Manager** | Class scheduling, membership plans, trainer management, reports |
| **Trainer** | Class attendance, PT assignments, client health assessments |
| **Dietitian** | Nutrition plans, meal templates, health profiles |
| **Accounts Executive** | Invoices, EMI scheduling, daily cash reconciliation |
| **Facility Supervisor** | Equipment registry, maintenance logs, lockers |
| **Member** | Self-service portal access (bookings, diet plans, invoices) |

## License

MIT
