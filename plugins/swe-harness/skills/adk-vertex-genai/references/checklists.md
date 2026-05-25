# ADK Vertex Gen AI Checklists

Use these checklists before touching production-shaped Google Agent Development Kit (ADK) agents. ADK means Google Agent Development Kit. SDK means Software Development Kit. ADC means Application Default Credentials. IAM means Identity and Access Management.

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
    callbacks/
    tools/
  scripts/
    deploy_agent_engine.py
    register_gemini_enterprise.py
    run_local_api_server.py
    smoke_test_agent_engine.py
  envs/
    prod.env
  evals/
  tests/
  .env
  .env.example
  Makefile
  pyproject.toml
```

## Vertex AI-Only Configuration

- Confirm the production target is Vertex AI Agent Engine, not Google Developers Gemini API.
- Confirm `google-genai` calls use either `genai.Client(vertexai=True, project=..., location=...)` or `GOOGLE_GENAI_USE_VERTEXAI=True`.
- Confirm no production code depends on `GOOGLE_API_KEY`.
- Confirm Gemini 3 models use `global` unless current official Vertex AI model docs say another endpoint is supported.
- Confirm `.env.example` separates local-only values from runtime values.
- Confirm Agent Engine runtime env files do not pass `GOOGLE_APPLICATION_CREDENTIALS`, `GOOGLE_CLOUD_PROJECT`, local `GOOGLE_CLOUD_LOCATION`, or Gemini Enterprise registration-only variables.
- Confirm model names, locations, thinking levels, output limits, and document-inspection settings are env-configurable.

## Local Preflight

- Confirm the repo install command has run, usually `uv sync --dev`.
- Confirm `.env` exists and local secrets are not checked in.
- Confirm local `.env` includes `GOOGLE_APPLICATION_CREDENTIALS`, `GOOGLE_CLOUD_PROJECT`, `AGENT_ENGINE_LOCATION`, and deployment display metadata if needed.
- Confirm runtime env file includes only values needed by the deployed service.
- Confirm the runtime service account email is set for deployment.
- Confirm the curated corpus, datastore, engine, or app paths are explicit and environment-driven.

## Credentials Check

Run a minimal ADC check before involving the agent:

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

- Confirm the project is the intended Google Cloud project.
- Confirm the credential identity is expected.
- Confirm the runtime service account has Discovery Engine or Vertex AI Search access.
- Confirm the runtime service account has Cloud Storage object read access for any `gs://` document inspection.
- Confirm the runtime service account can sign URLs only if signed links are required. This usually means IAM Service Account Token Creator on the signing identity or an equivalent configured signing path.

## Retrieval And Source Links

- Confirm the serving configuration path points at the expected engine or app when Enterprise extractive answers or segments are required.
- Run the Discovery Engine or Vertex AI Search call directly before debugging prompts.
- Normalize every result into citation-ready fields: `title`, `uri`, `snippet`, `chunk_text`, `source_id`, `score`, and optional signed-link metadata.
- Return machine-readable empty-result and error states.
- Deduplicate sources by canonical document identity, not signed URL string. Signed URLs change and should not be deduplication keys.
- Use markdown links as `[Document Title](https://...)`. Do not use `[Title](<https://...>)` in Gemini Enterprise unless that renderer has been verified.
- Keep signed URL expiration long enough for the user interaction, but not longer than needed.

## Google Gen AI SDK Document Tool

- Use the Google Gen AI SDK in Vertex AI mode.
- Use `types.HttpOptions(api_version="v1")` for stable Vertex AI calls when the project uses the versioned API.
- Use `types.Part.from_uri(file_uri="gs://bucket/object.pdf", mime_type="application/pdf")` for Portable Document Format (PDF) files in Cloud Storage.
- Validate supported document types before calling the model.
- Validate bucket allow-lists before full-document reads.
- Bound full-document calls with output token limits, media resolution, and thinking level.
- Return a structured object with `ok`, `supported`, `title`, `uri`, `mime_type`, `document_notes`, `model`, `location`, and `error`.
- Do not turn document-inspection failures into invented content. Let the synthesizer abstain or answer from remaining evidence.

## ADK App And Workflow

- Export `root_agent` from the package agent entrypoint.
- Export an Agent Engine app object, usually `agent_engine = AdkApp(agent=root_agent)`.
- Keep root-agent instructions narrow: greet, explain scope, guardrail, and delegate.
- Put grounded document answering in specialist agents.
- For deep research, prefer `SequentialAgent` around planner, `ParallelAgent` research lanes, and synthesizer.
- If hiding intermediate output, preserve function calls, function responses, and state deltas.
- Use callbacks for source aggregation, post-tool normalization, final citation append, markdown cleanup, and latency instrumentation.

## Local ADK Check

- Start the local server with a wrapper that loads `.env` safely.
- Confirm `/list-apps` contains the intended app only.
- Confirm `/app-info` exposes the expected root agent, sub-agents, workflow agents, and tools.
- Run a greeting request.
- Run an out-of-scope request and confirm redirect-only behavior if guardrails require it.
- Run a document question that should trigger retrieval.
- Run a question that should trigger full-document inspection if that tool exists.
- Confirm the final answer has distinct sources exactly once.

## Deployment Check

- Change into the repo root before creating the Agent Engine config.
- Generate the requirements file inside the uploaded package.
- Pass `source_packages` as relative package names.
- Pass `requirements_file` as a path relative to the uploaded source root.
- Use `entrypoint_module` and `entrypoint_object` that import cleanly in a fresh Python process.
- Include all files needed at runtime in the uploaded source package.
- Set runtime service account, CPU, memory, min instances, max instances, concurrency, and labels intentionally.
- Capture the resulting Agent Engine resource id.
- Write `deployment_metadata.json`.

## Remote Smoke Test

- Create a remote session.
- Run a greeting against the deployed agent.
- Run a retrieval-backed question against the deployed agent.
- Run a full-document question if the agent has a document tool.
- Confirm no local credential path is required remotely.
- Confirm the answer includes source-backed behavior, not only a successful transport call.
- Capture latency, selected model, and whether the request hit output-token limits.

## Gemini Enterprise Registration

- Confirm `GEMINI_ENTERPRISE_APP_ID` points to the full Gemini Enterprise app resource or the exact command accepts the shorter value.
- Confirm the Agent Engine resource id is available in `.env` or `deployment_metadata.json`.
- Prefer the same `Makefile` command shape the reference repo uses, usually `make register-gemini-enterprise`.
- Keep a repo-local Python registration script only as a fallback.
- Confirm the Gemini Enterprise description is written for routing. It should tell Gemini Enterprise when to invoke the agent.
- Omit authorization configuration unless the agent needs to access Google Cloud resources on behalf of the end user.
- Test in Gemini Enterprise after registration. The rendered markdown, source links, intermediate emissions, and final citation list are part of acceptance.

## Evaluation And Regression

- Add prompt-level regression tests for greeting, routing, out-of-scope redirect, insufficient evidence, citations, and signed-link formatting.
- Add at least one multi-turn evaluation.
- Use ADK evaluation criteria for hallucinations, safety, and tool-use quality when practical.
- Add a simple deterministic assertion for citation presence and duplicate-source absence.
- Re-run latency/quality experiments when changing model, thinking level, document-inspection model, parallel lane count, or source appending logic.
