# AppForge Cybersecurity Workbench — Integration Contract

## Product layout

Cybersecurity is a dedicated page/route, separate from the ordinary app generator. It is a dual-window workspace:

- **Computer / browser window:** a visible, isolated browser session controlled through the approved NeuralCore → Sapphire computer-use capability. It shows the active target, current page, navigation state, and actions performed. The user can observe and intervene.
- **Tools / terminal window:** the selected cybersecurity tool, job state, terminal output, findings, evidence, and remediation controls. Tools are launched through a governed dispatcher, never by exposing a host shell or Docker socket to the browser.
- **Voice / Ollama side panel:** local Ollama conversation with microphone input and speaker output. Speech-to-text and text-to-speech are explicit, user-permissioned browser capabilities. The panel can receive the current authorized task context and user-selected browser context so the assistant can answer questions and guide the task.

## Orchestration responsibilities

1. **NeuralCore** is the central coordinator: identity, task routing, policy checks, durable job state, tool selection, audit trail, timeouts, checkpoints, and recovery.
2. **Sapphire** supplies the computer-use capability: open the authorized browser/computer session, navigate pages, inspect visible content, interact with forms, and report action results to NeuralCore.
3. **Ollama** supplies local model inference. The configured local model is selected by policy; model names and capabilities are discovered from the local Ollama API rather than assumed.
4. **Cybersecurity tools and agents** run as isolated jobs behind a registry/dispatcher. Each tool advertises its actual installed status, supported actions, required permissions, and health. A UI card is not evidence that a tool is installed or working.
5. **Voice** is a user interface to the same governed task context, not a separate privileged route around policy.

## Computer-use behavior

- Open a separate browser/computer session inside the cybersecurity page; do not take over the user's everyday browser silently.
- Keep the active authorized target and scope visible throughout the job.
- Support navigation, page inspection, form filling, screenshots/evidence, and multi-step workflows where the connected Sapphire implementation actually exposes those operations.
- Require a visible user confirmation before submitting externally consequential forms, changing account/security settings, deleting data, sending messages, purchasing, or performing other irreversible actions.
- Do not bypass MFA, CAPTCHA, access controls, or site security. User-provided authenticated sessions remain private and are never exposed to public visitors.
- Record action timestamps, tool identity, target, outcome, and evidence references. Redact passwords, tokens, cookies, and other secrets from logs.

## Public/private separation

- Public visitors may use only explicitly published, sandboxed AppForge capabilities and their own authenticated sessions.
- The owner's Mac, NeuralCore, Sapphire sessions, Docker containers, local files, credentials, and private security tools remain owner-only by default.
- The public frontend must never call localhost on the owner's Mac. No public endpoint may expose Docker, host shell, Ollama, or the private NeuralCore gateway directly.
- A future public service requires a separately deployed authenticated broker with per-user isolation, rate limits, quotas, job timeouts, audit logging, and strict tool allowlists. Private local execution requires an owner-authenticated connector/tunnel with narrow scopes; do not create a tunnel until the broker and access controls are verified.

## Voice and context permissions

- Ask for microphone permission only when the user enables voice input; provide a visible recording state and stop control.
- Use speaker output only after user activation and respect browser audio policies.
- The assistant may inspect only the active workbench browser session and content that the user has authorized it to access. It does not have universal visibility into the computer, microphone, camera, or other applications.
- Show which model is active, whether inference is local, and whether voice services are available.

## Required service API boundary

The frontend talks only to an authenticated workbench API. The API exposes safe operations such as:

- GET /api/workbench/status
- GET /api/workbench/tools
- POST /api/workbench/jobs (validated tool ID, authorized target, bounded parameters)
- GET /api/workbench/jobs/{job_id}
- POST /api/workbench/jobs/{job_id}/cancel
- POST /api/workbench/computer/sessions and scoped session actions
- POST /api/workbench/voice/transcribe and /api/workbench/voice/speak when enabled

These are target contracts, not claims that these endpoints already exist. Implementations must authenticate every request, authorize every action server-side, validate inputs, and write audit events.

## Acceptance tests

- The cybersecurity route is distinct from the AppForge generator.
- Computer and tool windows are simultaneously visible and independently usable.
- A browser task runs in a dedicated session and reports real action results.
- NeuralCore dispatches only registered, healthy, authorized tools.
- Ollama model availability is discovered live; no fake model/tool status is shown.
- Mic and speaker permissions are opt-in and visibly indicated.
- Public sessions cannot enumerate or invoke private owner tools, containers, files, or browser sessions.
- Sensitive actions pause for explicit confirmation.
- Every job can be inspected, cancelled, and audited.
- If Sapphire, NeuralCore, Ollama, or a tool is offline, the UI reports the real unavailable state and does not simulate success.

## Current implementation status (2026-11-01)

This document records the requested integration contract. The GitHub project is currently a static HTML generator and has no backend. The Base44 ForgeAI site is a separate application and its source is not present in this repository. The local NeuralCore web gateway was previously restricted to loopback, but its inspected source still documents no request authentication. Do not expose it publicly or claim public/private brokerage is complete until authentication and the owner-only dispatcher are implemented and tested. Sapphire's exact callable API and the active microphone/speaker services still need to be verified against the installed local components before wiring live controls.
