# Common Failures

## `No module named '<your package>'`

Meaning:
- The uploaded source archive does not expose the package at the import path the runtime expects.

Fix:
- Use a top-level importable package.
- Pass `source_packages` as a relative package name.
- Change into the project root before building the Agent Engine config.
- Keep `entrypoint_module` aligned with the real package path.

## `No module named 'vertexai'`

Meaning:
- The runtime did not install the requirements file that contains `google-cloud-aiplatform`.

Fix:
- Generate the requirements file inside the uploaded source package.
- Pass `requirements_file` as a path relative to the uploaded source root.
- Redeploy after confirming the build logs show the user requirements file being found and installed.

## Enterprise feature precondition error from Discovery Engine or Vertex AI Search

Meaning:
- The serving configuration points at a raw datastore when the request needs Enterprise extractive features.

Fix:
- Switch `VERTEX_AI_SEARCH_SERVING_CONFIG_PATH` to the engine or app serving configuration.
- Re-run the direct search test before re-running the agent.

## Local ADK server shows the wrong apps

Meaning:
- The discovery directory is too broad or points at the wrong folder.

Fix:
- Point local ADK discovery at a narrow shim directory or a directory that contains only the intended app package.
- Do not distort the deployed package layout just to satisfy local discovery.

## Local `adk` command breaks after moving the repo

Meaning:
- The virtual environment entrypoint has a stale shebang.

Fix:
- Use `.venv/bin/python -m google.adk.cli ...` or a wrapper script instead of relying on the stale executable.
- Rebuild the virtual environment later if needed.

## Deployment says created but the agent was never queried

Meaning:
- The container started, but end-to-end behavior is still unverified.

Fix:
- Create a remote session.
- Run a greeting.
- Run a retrieval-backed question.
- Treat remote query success as part of deployment completion.
