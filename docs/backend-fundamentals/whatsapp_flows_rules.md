The Five Rules of WhatsApp Flows

Based on this incident, let's define some engineering rules.

Rule 1 — Static Flow JSON Defines the UI

Contains:

version
routing_model
screens

Think of it as the blueprint.

Rule 2 — Data Exchange Provides Dynamic Data

Contains only:

{
  "screen": "...",
  "data": { ... }
}

It fills the blueprint with live data.

Rule 3 — Never Invent the Contract

If Meta's documentation says:

{
  "screen": "...",
  "data": { ... }
}

Don't add extra fields because they "seem harmless."

Rule 4 — Every Flow Starts with an Event

The event:

Flow Opened

should trigger

flow_action = "data_exchange"

That ensures fresh data is loaded.

Rule 5 — Protect Yourself with Tests

Every integration bug should result in a new automated test so the same mistake is caught before it reaches users again.