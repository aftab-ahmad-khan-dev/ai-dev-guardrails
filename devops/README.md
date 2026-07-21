# devops — CI/CD & Deployment Rule Pack

Rules and platform playbooks for **AWS EC2, DigitalOcean, Vercel, cPanel,
Railway, Render**, plus Docker, Actions, and reliability practices.

- Rules: [`devops-rules.yaml`](devops-rules.yaml)
- Pipeline starters: [`pipelines/`](pipelines/)

**Source:** AI Dev Rules Master Prompt Pack — Part 4 (v2.0.0)

## Index (20 rules · prefix `OPS`)

| ID | Rule | Severity | Template |
|----|------|----------|----------|
| OPS-01 | CI/CD pipeline principles | high | — |
| OPS-02 | Secrets & env vars in pipelines | critical | — |
| OPS-03 | AWS EC2 deployment | high | [`pipelines/deploy-ec2.yml`](pipelines/deploy-ec2.yml) |
| OPS-04 | DigitalOcean deployment | high | [`pipelines/deploy-digitalocean.yml`](pipelines/deploy-digitalocean.yml) |
| OPS-05 | Vercel deployment | high | [`pipelines/deploy-vercel.yml`](pipelines/deploy-vercel.yml) |
| OPS-06 | cPanel deployment | medium | [`pipelines/deploy-cpanel.yml`](pipelines/deploy-cpanel.yml) |
| OPS-07 | Railway deployment | high | [`pipelines/deploy-railway.yml`](pipelines/deploy-railway.yml) |
| OPS-08 | Render deployment | high | [`pipelines/deploy-render.yml`](pipelines/deploy-render.yml) |
| OPS-09 | Docker containerization | high | — |
| OPS-10 | GitHub Actions workflow standards | high | — |
| OPS-11 | Build & artifact management | medium | — |
| OPS-12 | Zero-downtime deployment | high | — |
| OPS-13 | Rollback & recovery | high | — |
| OPS-14 | Infrastructure as Code | medium | — |
| OPS-15 | Nginx reverse proxy & SSL | high | — |
| OPS-16 | Process management (PM2 / systemd) | medium | — |
| OPS-17 | Database migrations in pipeline | high | — |
| OPS-18 | Monitoring & alerting | medium | — |
| OPS-19 | Logging & log rotation | medium | — |
| OPS-20 | Backup & disaster recovery | high | — |

> **Status:** All 20 rules are fully written (`status: complete`).
