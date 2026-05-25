# Common Failures

This file is a troubleshooting map for Google Agent Development Kit (ADK) agents deployed on Vertex AI Agent Engine with Google Gen AI Software Development Kit (SDK) tools.

## Accidentally using Google Developers Gemini API

Meaning:
- The code is using API-key auth, Google AI Studio assumptions, or a non-Vertex Gen AI client path.

Signals:
- `GOOGLE_API_KEY` appears in production env or code.
- `genai.Client()` is used without `vertexai=True` and without `GOOGLE_GENAI_USE_VERTEXAI=True`.
- Model calls work locally but fail on Agent Engine with auth or project-location errors.

Fix:
- Use `genai.Client(vertexai=True, project=..., location=...)`.
- Or set `GOOGLE_GENAI_USE_VERTEXAI=True`, `GOOGLE_CLOUD_PROJECT`, and `GOOGLE_CLOUD_LOCATION`.
- Remove API keys from production env files.

## Wrong model endpoint or location

Meaning:
- The Agent Engine region, retrieval location, and Gemini model endpoint are being treated as one setting.

Signals:
- Gemini 3 calls fail outside `global`.
- Discovery Engine searches fail because the datastore or Enterprise app is in `global`, `us`, or `eu`, while Agent Engine is in a regional location.
- The app works locally only because local env variables differ from runtime env variables.

Fix:
- Keep separate variables for Agent Engine location, retrieval location, Gemini model location, document-understanding location, and Gemini Enterprise app location.
- For Gemini 3 preview models, use `global` unless current official Vertex AI model docs say otherwise.

## `No module named '<your package>'`

Meaning:
- The uploaded source archive does not expose the package at the import path the runtime expects.

Fix:
- Use a top-level importable package.
- Pass `source_packages` as a relative package name.
- Change into the project root before building the Agent Engine config.
- Keep `entrypoint_module` aligned with the real package path.

## `No module named 'vertexai'` or `No module named 'google.genai'`

Meaning:
- The runtime did not install the requirements file that contains `google-cloud-aiplatform` or `google-genai`.

Fix:
- Generate the requirements file inside the uploaded source package.
- Pass `requirements_file` as a path relative to the uploaded source root.
- Redeploy after confirming build logs show the user requirements file being found and installed.

## Enterprise feature precondition error from Discovery Engine or Vertex AI Search

Meaning:
- The serving configuration points at a raw datastore when the request needs Enterprise extractive features.

Fix:
- Switch `VERTEX_AI_SEARCH_SERVING_CONFIG_PATH` to the engine or app serving configuration.
- Re-run the direct search test before re-running the agent.

## Empty search results from a known-good corpus

Meaning:
- The serving configuration, query location, collection, or filter no longer matches the uploaded corpus.

Fix:
- Run a direct Discovery Engine or Vertex AI Search request outside the agent.
- Confirm the path includes the expected project, location, collection, engine or datastore, and serving config.
- Confirm the datastore has completed indexing.
- Remove overly narrow filters before prompt debugging.

## Full-document inspection fails

Meaning:
- The Google Gen AI SDK document-understanding tool could not read or process the Cloud Storage document.

Signals:
- Permission denied on `gs://` URI.
- Unsupported Multipurpose Internet Mail Extensions (MIME) type.
- File exceeds model limits.
- Bucket does not match an allow-list.

Fix:
- Grant the runtime service account Cloud Storage object read access.
- Validate only supported Portable Document Format (PDF) or text documents are sent.
- Check the current Vertex AI model page for file size, page, and token limits.
- Return structured tool failure and let the synthesizer abstain or rely on other evidence.

## Signed URLs fail or links are broken

Meaning:
- The agent generated source links that Gemini Enterprise cannot render or the runtime identity cannot sign.

Signals:
- Link renders as literal `[Title](<https://...>)`.
- Signed URL returns 403.
- Duplicate source entries appear because every signed URL has a unique signature.

Fix:
- Render links as `[Title](https://...)`.
- Deduplicate by canonical `gs://` URI or document id before signing.
- Confirm runtime identity can sign URLs or has access to the configured signing service account.
- Confirm the signed URL bucket matches the datastore corpus bucket.
- Keep the original `gs://` URI in state for deduplication; use signed URLs only for final display.

## Duplicate sources at the end of the answer

Meaning:
- Sources are appended in multiple callback layers or deduplicated by signed URL instead of canonical document identity.

Fix:
- Maintain one canonical `sources_by_id` state collection.
- Append sources only in the final synthesizer callback.
- Deduplicate before signing or before final markdown emission.
- Add a regression assertion that each source title appears once in the final source list.

## Intermediate workflow output leaks into Gemini Enterprise

Meaning:
- Planner or parallel research agents emit text events that the Enterprise interface renders before the final answer.

Fix:
- Use a workflow wrapper or event filter that hides non-final text events.
- Preserve function-call events, function-response events, and state deltas.
- Prefer final-only synthesis as the only user-visible text.
- Re-test in Gemini Enterprise because local streams and Enterprise rendering may differ.

## `MAX_TOKENS` or truncated synthesis

Meaning:
- The final synthesizer or document-inspection model hit output-token limits.

Fix:
- Inspect response finish reason and usage metadata if available.
- Increase final output tokens for synthesis.
- Lower parallel lane verbosity.
- Deduplicate sources and compress research notes before synthesis.
- Experiment with Flash versus Pro models and thinking level, but re-check groundedness.

## Slow deep-research runs

Meaning:
- Too many parallel lanes, too many full-document reads, high thinking level, or Pro model usage is pushing latency up.

Fix:
- Benchmark one variable at a time: lane count, research model, document model, thinking level, max document reads, and output limit.
- Keep retrieval first and full-document reads selective.
- Prefer Flash for parallel research lanes when quality remains acceptable.
- Cache or skip repeated full-document reads within a single request.

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
- Run a full-document question if supported.
- Treat remote query success as part of deployment completion.

## Gemini Enterprise registration succeeds but routing is poor

Meaning:
- Gemini Enterprise has an agent registration, but the display description is not specific enough for the outer Enterprise router.

Fix:
- Rewrite the Gemini Enterprise agent description as a routing description, not marketing copy.
- Include supported domains and explicit exclusions.
- Re-register or update the Enterprise agent metadata.
