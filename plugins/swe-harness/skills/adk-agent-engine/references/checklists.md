# ADK Agent Engine Checklists

## Standard Repo Shape

Prefer this shape unless the existing repo already has a strong pattern:

```text
repo/
  my_agent/
    __init__.py
    agent.py
    agent_engine_app.py
    config.py
    agents/
    tools/
  scripts/
    deploy_agent_engine.py
    register_gemini_enterprise.py
    run_local_api_server.py
  envs/
    prod.env
  tests/
  .env
  .env.example
  Makefile
  pyproject.toml
```

## Local Preflight

- Confirm `uv sync --dev` or the repo’s install command has run.
- Confirm `.env` exists.
- Confirm the local `.env` includes:
  - `GOOGLE_APPLICATION_CREDENTIALS`
  - `GOOGLE_CLOUD_PROJECT`
  - `AGENT_ENGINE_LOCATION`
  - `AGENT_ENGINE_SERVICE_ACCOUNT`
  - `VERTEX_AI_SEARCH_SERVING_CONFIG_PATH`
- Confirm the runtime env file includes only runtime settings needed by the deployed service.

## Credentials Check

Run a minimal Python check before touching the agent:

```bash
.venv/bin/python - <<'PY'
import google.auth
creds, project = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
print(project)
print(type(creds).__name__)
print(getattr(creds, "service_account_email", "n/a"))
PY
```

## Retrieval Check

- Confirm the serving configuration path points at the expected engine or app.
- Run the Discovery Engine or Vertex AI Search call directly before debugging prompts.
- Confirm search returns results for at least one known document query.

## Local ADK Check

- Start the local server with a wrapper that loads `.env` safely.
- Confirm `/list-apps` contains the intended app only.
- Confirm `/app-info` exposes the expected root agent, sub-agents, and tools.
- Run a greeting request.
- Run a document question that should trigger the retrieval tool.

## Deployment Check

- Change into the repo root before creating the Agent Engine config.
- Generate the requirements file inside the uploaded package.
- Pass `source_packages` as relative names.
- Pass `requirements_file` as a path relative to the uploaded source root.
- Capture the resulting Agent Engine resource id.
- Write `deployment_metadata.json`.

## Remote Smoke Test

- Create a remote session.
- Run a greeting against the deployed agent.
- Run a document question against the deployed agent.
- Confirm the answer includes source-backed behavior, not only a successful transport call.

## Registration Check

- Confirm `GEMINI_ENTERPRISE_APP_ID` is set.
- Confirm the Agent Engine resource id is available in `.env` or deployment metadata.
- Prefer the same `Makefile` registration command shape the reference repo uses.
