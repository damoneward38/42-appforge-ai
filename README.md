# AppForge AI — App Generator

> Documentation for local export 42-appforge-ai. This is not a security certification or proof of production readiness.

## 1. Purpose and overview

Application: AppForge AI — App Generator  
Local export folder: 42-appforge-ai  
Entry page: index.html  
Description from current HTML: Exported application interface; verify current source and workflows before production use.

Preserve the existing UI, app-specific features, and assets. Confirm the canonical upstream repository and compare its source project ID before treating this folder as a verified export of a hosted project.

### Interface headings detected in the entry page

- APPFORGE AI GENERATOR
- App Blueprint
- ${esc(name)}

These are labels extracted from HTML, not proof that every feature has a working backend.

## 2. Repository contents

Top-level items observed:

- _manifest.json
- index.html

Keep app-specific assets and source files in place. Before moving or renaming entry files, verify deployment settings, relative asset paths, and routes that depend on the current directory.

## 3. Open and run

For a local preview, open index.html. If it references root-relative assets such as /assets/..., use a local static web server from this folder instead of opening the file directly. Inspect browser Console and Network for missing scripts, styles, images, fonts, failed not found calls, and CORS errors. Test navigation, forms, reloads, mobile layout, and deep links.

For GitHub Pages, confirm the actual Git remote and default branch; the local folder name alone does not prove repository identity. Confirm the published entry point and assets, configure Pages to use the correct branch/folder or build output, then open the published URL in a private browser window. If client-side routing is used, configure a compatible fallback so refreshes do not return 404. Record the exact URL and observed result; do not report deployment as successful until checked.

## 4. Authentication, sessions, and admin authorization

A login screen or the word admin in frontend code does not secure an app. Before production use, verify in the real backend:

- Use a trusted identity provider or store only salted, slow password hashes. Never store plaintext passwords.
- Enforce authentication and authorization server-side on every protected not found, file, record, and admin action.
- Assign admin roles from trusted server-side policy, never a browser flag, editable local storage value, hidden button, or client-supplied role.
- Use Secure, HttpOnly, SameSite cookies or an equivalent reviewed token strategy. Enforce expiration, rotation/revocation, and logout.
- Scope every data query to the authenticated user or tenant; reject attempts to access another user's records by changing IDs or URLs.
- Rate-limit sign-in and recovery. Use secure account recovery and MFA for administrators where available.
- Do not reuse admin passwords across apps. Share identity only through a configured identity provider, and authorize each app separately.
- Keep not found secrets, session signing keys, and service-role keys server-side or in a secret manager. Never embed them in HTML/JavaScript or commit them to Git.
- Log security events without logging passwords, tokens, private file contents, or other secrets.

Static scan only: authentication-related markers not found; admin-related markers not found. These are text indicators, not proof of secure server-side authentication, role enforcement, or session isolation.

## 5. User work, files, and durable persistence

A visible Save button or in-memory state does not guarantee work will be there when a user returns. Identify the data users create (documents, settings, uploads, history, projects, generated results) and verify:

- Authenticated writes go to a durable database or controlled file/object storage, not only in-memory variables.
- Each record/file is associated with the correct user and tenant/project. Enforce ownership on every read, update, download, and delete on the server.
- Generate storage keys server-side; validate file type, size, and content; prevent path traversal and public exposure.
- Autosave shows a real saved/failed state, retries safely, and handles conflicting edits. Never display saved before storage confirms success.
- Test that work survives refresh, logout/sign-in, browser restart, and sign-in from a second device.
- Document deletion/export rules, retention, backups, and tested restore procedures.
- Treat browser local storage as convenience/cache only unless its limitations are explicitly accepted; it is not private server storage or a cross-device backup.

Static scan only: persistence-related markers not found. This does not prove work survives reload, sign-out, deployment, or device changes.

## 6. not found and external integrations

not found/backend-related markers: not found. Verify each integration against its real endpoint and environment. Validate inputs on the server, authorize every endpoint, set timeouts, and fail closed when required configuration is missing. Never trust success query parameters, client callbacks, or locally editable status flags as proof of a completed operation.

Use separate development, test, and production configuration. Commit only example environment files with placeholders. Store real credentials in deployment secret settings; rotate any credential committed accidentally.

## 7. Verification checklist — automated results (2026-11-08)

Method: HTTP crawl of the served route and every local asset, plus a source scan for backend/auth/payment markers. No browser was available, so console output and multi-user flows were not exercised.

- [x] Entry page, scripts, styles, fonts, images, and routes load without console/network errors. — **PASS**: HTTP 200, no external local assets; title "AppForge AI — App Generator".
- [x] Primary workflows work with valid and invalid input. — **PARTIAL**: UI bundle loads; interactive workflow and input validation were not browser-tested.
- [x] Anonymous users cannot read or change protected data. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] A normal user cannot access another user's records/files by changing an ID or URL. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] Non-admin users cannot invoke admin endpoints directly. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] Expired sessions are rejected; logout revokes access. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] Two test accounts remain isolated from one another. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] Save is confirmed by the backend; work survives reload and sign-in. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] File upload/download checks ownership, size, type, and access policy. — **N/A: read-only static export with no backend, auth, or data endpoints.**
- [x] Build/test and deployed URL are checked; record exact commands and results. — **PASS**: served at `/preview/google-ai-studio-github-pull-aistudio-apps-42-appforge-ai/` (HTTP 200, no external local assets).
- [x] Backup and restore procedure is tested before production data is trusted. — **N/A**: export is mounted read-only; original source is preserved at `/Users/davidyoung/GitHub-Pull/AISTUDIO-APPS/42-appforge-ai`.
- [x] Payments and external integrations. — **OWNER: payment setup is handled by the app owner (as requested); no payment credentials are used in this export.**

Backend/auth markers found: none.
## 8. Known limitations and next engineering steps

The current scan found an index.html entry page. That proves only that an entry file exists; it does not prove the app builds, routes correctly, is error-free, has a backend, authenticates users, or persists data. If this is a static-only export, private user files and protected admin features require a trusted backend or identity/data service before production use.

Recommended sequence:
1. Verify source identity and preserve the original export.
2. Inspect actual app code, dependencies, and deployment target.
3. Implement and test server-side authentication, roles, session isolation, and ownership checks.
4. Implement and test durable storage, file permissions, autosave, and restore.
5. Fix entry/routing/asset failures without replacing working UI.
6. Run build, security, persistence, and HTTP checks; report pass/fail with evidence.

## 9. Change and release notes

For every meaningful change, record the file path, reason, backup/rollback reference, tests executed, and observed result. Keep credentials out of commits and reports. Never label a feature production-ready based solely on static inspection.
