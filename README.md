# Teamsource HSE Intelligence

**AI-Powered Health, Safety and Environment Management & Incident Intelligence Platform**

## 1. Project Overview

Teamsource HSE Intelligence is an AI-powered Health, Safety and Environment (HSE) management and incident intelligence platform designed to help organisations identify workplace hazards, report incidents, manage safety inspections, track corrective actions and improve workplace safety performance.

The platform is intended to support organisations across multiple industries, including:

- Oil and gas.
- Manufacturing.
- Construction and engineering.
- Logistics and transportation.
- Warehousing and distribution.
- Healthcare.
- Other industrial and commercial operations.

The goal is to provide organisations with a centralised system for managing HSE activities, maintaining safety records, monitoring risks and making better-informed safety decisions.

AI capabilities will support reporting, classification, summarisation and analysis. Safety-critical decisions will remain subject to qualified human review.

## 2. Problem Statement

Many organisations still manage workplace safety activities using disconnected spreadsheets, paper-based forms, messaging applications and manual reporting processes.

This creates challenges such as:

- Delayed incident reporting.
- Poor visibility into workplace hazards.
- Difficulty tracking corrective actions.
- Inconsistent safety inspection records.
- Limited visibility into recurring incidents.
- Difficulty measuring HSE performance.
- Fragmented safety documentation.

Teamsource HSE Intelligence aims to address these challenges through a centralised digital platform.

## 3. Project Objectives

The platform aims to:

1. Simplify incident and near-miss reporting.
2. Improve hazard identification and risk assessment.
3. Digitise workplace safety inspections.
4. Track corrective and preventive actions.
5. Provide meaningful HSE analytics and reports.
6. Introduce AI-assisted safety intelligence.
7. Support multiple organisations and operational sites.
8. Provide a scalable foundation for future HSE capabilities.

## 4. Target Users

The platform will support different user roles within an organisation.

| User Role | Main Responsibilities |
|---|---|
| Teamsource Administrator | Platform-level administration and oversight |
| Organisation Administrator | Organisation configuration and user management |
| HSE Manager | HSE oversight, approvals and performance monitoring |
| HSE Officer | Incident investigations, inspections and risk management |
| Supervisor | Operational safety monitoring and action follow-up |
| Employee | Incident, near-miss and hazard reporting |

Permissions will be enforced by the backend according to the user's organisation, role and assigned access.

## 5. Core Product Modules

The initial product will consist of six major modules.

### Module 1: Incident and Near-Miss Reporting

Allows employees and authorised users to report workplace incidents and near misses.

Planned capabilities:

- Incident submission.
- Near-miss reporting.
- Incident date, time and location.
- Incident descriptions and categories.
- Severity classification.
- Supporting evidence and attachments.
- Witness information where appropriate.
- Investigation and follow-up.
- Incident status tracking.

### Module 2: Hazard Identification and Risk Assessment

Provides a structured way to identify hazards and assess workplace risks.

Planned capabilities:

- Hazard identification.
- Hazard categorisation.
- Likelihood and severity assessment.
- Risk rating.
- Existing safety controls.
- Recommended mitigation measures.
- Assigned responsible persons.
- Risk review and monitoring.

### Module 3: Safety Inspection Management

Digitises workplace safety inspections.

Planned capabilities:

- Inspection scheduling.
- Digital inspection checklists.
- Inspection findings.
- Evidence and attachments.
- Identified non-conformities.
- Inspection status.
- Follow-up actions.

### Module 4: Corrective and Preventive Actions (CAPA)

Manages actions required to address identified safety problems.

Planned capabilities:

- Corrective action creation.
- Preventive action creation.
- Assignment of responsible persons.
- Priority levels.
- Due dates.
- Progress tracking.
- Overdue action monitoring.
- Closure evidence and verification.

### Module 5: HSE Analytics and Reporting

Provides visibility into workplace safety performance.

Planned capabilities:

- Incident summaries.
- Incident category analysis.
- Hazard trends.
- Inspection performance.
- Open and overdue corrective actions.
- Organisational safety reports.
- Site-level reporting.
- Historical comparisons.

All operational metrics must be calculated from actual application records. AI must not invent numerical performance results.

### Module 6: AI HSE Assistant

Provides AI-assisted support for HSE activities.

Planned capabilities:

- Incident report summarisation.
- Suggested incident classifications.
- Suggested hazard categories.
- Investigation question suggestions.
- Safety report summarisation.
- Identification of recurring patterns in available records.
- Assistance with HSE documentation.

AI recommendations are advisory. Qualified personnel must review safety-critical recommendations and decisions.

## 6. Technology Stack

The project will use the following technologies.

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend programming language |
| FastAPI | Backend API framework |
| React | Frontend application |
| PostgreSQL | Relational database |
| SQLAlchemy | Python database ORM |
| Alembic | Database migration management |
| Psycopg | PostgreSQL database driver |
| Pydantic | Request validation and data schemas |
| Uvicorn | Python application server |
| Pytest | Backend automated testing |
| HTTPX | API testing |
| Git and GitHub | Version control and collaboration |

Additional tools for AI development, deployment and infrastructure will be selected as the project progresses.

## 7. System Architecture

The application will follow a frontend-backend-database architecture.

### Application flow

```text
              USERS
                |
                v
         REACT FRONTEND
                |
                | HTTP / REST API
                v
       PYTHON + FASTAPI BACKEND
                |
       +--------+---------+
       |        |         |
       v        v         v
   VALIDATION  BUSINESS  AUTHENTICATION
               LOGIC     & PERMISSIONS
       |
       v
    SQLALCHEMY
       |
       v
    POSTGRESQL
       |
       v
  PERSISTENT DATA
```

AI services will be accessed through the backend when required.

### How the components communicate

1. Users interact with the React frontend.
2. The frontend sends HTTP requests to FastAPI endpoints.
3. FastAPI validates incoming information.
4. Backend services execute business logic.
5. SQLAlchemy communicates with PostgreSQL.
6. The backend returns structured responses.
7. React displays the results to the user.

The backend is responsible for enforcing authentication, authorisation, data validation and organisation-level access.

## 8. Development and Learning Roadmap

All three interns will participate in building the complete application.

Development will be organised into sequential learning and implementation phases.

### Phase 1: Backend Development

**Technologies:** Python and FastAPI.

Learning objectives:

- Python fundamentals relevant to backend development.
- FastAPI application structure.
- API routing and endpoints.
- Request and response handling.
- Pydantic schemas and validation.
- Business logic and service layers.
- API testing with Swagger and Postman.
- Backend code organisation.

Expected deliverable:

A functioning backend API foundation with documented and tested endpoints.

### Phase 2: Frontend Development

**Technology:** React.

Learning objectives:

- React fundamentals.
- Components and reusable interfaces.
- Pages and application navigation.
- Forms and state management.
- API integration.
- Loading and error states.
- Responsive application design.

Expected deliverable:

A functional frontend that communicates with the previously developed backend APIs.

### Phase 3: Database Development

**Technologies:** PostgreSQL, SQLAlchemy and Alembic.

Learning objectives:

- Relational database fundamentals.
- SQL queries.
- Database design.
- Tables and relationships.
- SQLAlchemy models.
- Database connections.
- Alembic migrations.
- CRUD operations.
- Data integrity.

Expected deliverable:

A persistent database integrated with the backend, replacing temporary demonstration data.

**Important:** Database requirements and API data contracts must be considered during the earlier phases. The database implementation and persistent integration will be completed in this phase.

### Phase 4: Application Integration

Learning objectives:

- Connect frontend, backend and database.
- Implement authentication and role-based permissions.
- Integrate real application workflows.
- Test data validation and access controls.
- Verify organisation-level data isolation.
- Test application functionality end to end.

Expected deliverable:

A functional end-to-end HSE application foundation.

### Phase 5: AI Integration and Enhancement

Learning objectives:

- AI service integration.
- Structured AI responses.
- Incident summarisation.
- Hazard classification assistance.
- Testing AI outputs.
- Human review and safety controls.

Expected deliverable:

An AI-assisted HSE platform with validated, advisory AI functionality.

## 9. Team Development Methodology

All three interns will learn and contribute to each major development phase.

We will use a collaborative learning model.

### How the team will work

- Developers will work on assigned tasks.
- Coding, testing and review responsibilities will rotate.
- Each developer must understand and explain their contributions.
- Team members will collaborate on technical decisions.
- Progress will be reviewed regularly.
- Completed functionality must be demonstrated and tested.

### Project supervision

The Project Manager and Technical Supervisor will:

- Define product requirements.
- Coordinate the development roadmap.
- Assign tasks.
- Review technical implementation.
- Monitor project progress.
- Approve integration of completed work.
- Coordinate quality assurance.

## 10. Repository Structure

The project repository will be organised as follows:

```text
teamsource-hse-intelligence/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   └── (React application - to be established)
│
├── ai/
│   └── (AI services - to be established)
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── ROADMAP.md
│   ├── DATABASE_DESIGN.md
│   └── API_SPECIFICATION.md
│
├── .github/
│   └── ISSUE_TEMPLATE/
│
├── .gitignore
└── README.md
```

Some directories and files are planned and will be added as development progresses.

## 11. Development Environment Setup

### Prerequisites

Developers should have:

- Python 3.13.
- Git.
- Node.js LTS for frontend development.
- PostgreSQL 18 for local database development.
- VS Code or another suitable IDE.
- A GitHub account.

### Clone the repository

```bash
git clone https://github.com/NwankwoDave01/teamsource-hse-intelligence.git

cd teamsource-hse-intelligence
```

### Switch to the development branch

```bash
git checkout develop
```

### Create a Python virtual environment

```bash
py -3.13 -m venv .venv
```

### Activate the environment (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install backend dependencies

```bash
python -m pip install -r backend/requirements.txt
```

### Run the backend application

```bash
python -m uvicorn app.main:app --app-dir backend --reload
```

### Access the API

- Backend: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

Database connection configuration and frontend setup instructions will be added when those stages are implemented.

## 12. GitHub Collaboration Workflow

GitHub will serve as the central source repository.

### Branch structure

- `main`: Stable and approved releases.
- `develop`: Shared integration branch.
- `feature/*`: Individual development tasks.

### Development process

1. Start from the latest `develop` branch.
2. Create a feature branch.
3. Implement the assigned task.
4. Test the changes locally.
5. Commit the changes with meaningful messages.
6. Push the feature branch to GitHub.
7. Open a Pull Request into `develop`.
8. Submit the changes for review.
9. Merge only after approval.

### Example commands

```bash
git checkout develop

git pull origin develop

git checkout -b feature/incident-api

# Make your changes

git add .

git commit -m "feat: add incident API foundation"

git push -u origin feature/incident-api
```

Open a Pull Request on GitHub after pushing.

No developer should push directly to `main`.

## 13. Code Quality and Security Standards

All contributors must follow these principles:

- Write readable and maintainable code.
- Use meaningful names for files, functions and variables.
- Validate all incoming data.
- Handle errors appropriately.
- Write automated tests for implemented functionality.
- Never commit passwords, API keys or database credentials.
- Use environment variables for sensitive configuration.
- Enforce backend authentication and authorisation.
- Ensure organisations cannot access one another's data.
- Keep an auditable record of important application activities.
- Review uploaded files and validate their types and sizes.
- Require human review of safety-critical AI recommendations.

Security, organisation isolation and data protection must be designed into the application from the beginning.

## 14. Future Development Opportunities

Features that may be considered after the initial product foundation include:

- HSE training and certification management.
- Personal protective equipment (PPE) management.
- Permit-to-work management.
- Environmental monitoring.
- Mobile incident reporting.
- IoT and sensor integrations.
- Multi-site operational intelligence.
- Subscription and SaaS management.

These are future possibilities, not commitments for the initial MVP.

## 15. Current Project Status

**Project:** Teamsource HSE Intelligence

**Repository:** [GitHub Repository](https://github.com/NwankwoDave01/teamsource-hse-intelligence)

**Current development stage:** Environment preparation and technical onboarding.

| Component | Current status |
|---|---|
| GitHub repository | Set up |
| Main and develop branches | Set up |
| Project folder structure | Created |
| Python 3.13 environment | Set up |
| FastAPI dependencies | Installed |
| FastAPI starter application | Created and tested |
| PostgreSQL 18 | Installed and running |
| Development database | Created |
| Python-to-PostgreSQL connection | Pending |
| React application | Pending |
| Database models and migrations | Pending |
| HSE product modules | Pending |

## 16. Project Vision

Teamsource HSE Intelligence aims to become a practical and scalable digital safety management platform that helps organisations move from reactive workplace safety management to more structured, proactive and data-informed HSE operations.

We are building a product that solves real operational problems, supports multiple industries and creates opportunities for intelligent safety management.

**Build collaboratively. Learn continuously. Develop responsibly.**
