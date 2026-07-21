# Pipeline templates

Minimal, safe GitHub Actions starters from the Master Prompt Pack (Part 4).

| File | Platform | Required secrets |
|------|----------|------------------|
| `deploy-ec2.yml` | AWS EC2 + PM2 | `EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY` |
| `deploy-digitalocean.yml` | DigitalOcean App Platform | `DIGITALOCEAN_ACCESS_TOKEN`, `DO_APP_ID` |
| `deploy-vercel.yml` | Vercel | `VERCEL_TOKEN` |
| `deploy-cpanel.yml` | cPanel (SFTP) | `CPANEL_HOST`, `CPANEL_USER`, `CPANEL_PASSWORD` |
| `deploy-railway.yml` | Railway | `RAILWAY_TOKEN`, `RAILWAY_SERVICE_ID` |
| `deploy-render.yml` | Render | `RENDER_DEPLOY_HOOK_URL` |

## Cross-platform rules

1. Lint + tests + build must pass before any deploy step.
2. Deploy only on push to `main` (or a release tag) — never arbitrary branches or fork PRs.
3. All credentials are CI secrets — never inline values in YAML.
4. Production deploys require the same PR-review gate as merging to `main`.

Copy a template into your app repo under `.github/workflows/` and adapt build commands to your stack.
