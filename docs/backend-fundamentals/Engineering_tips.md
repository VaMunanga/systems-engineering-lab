The Thought Process of a Senior Engineer

Here's what junior developers do.

"Dropdown empty."

↓

"Maybe FastAPI is broken."

↓

Random code changes.

Senior engineers think differently.

They ask:

Step 1

Where does the truth originate?

Supabase.

Step 2

Did the backend retrieve it?

Yes.

Step 3

Did Python build the response?

Yes.

Step 4

Was JSON correct?

Let's inspect it.

Step 5

Did it follow Meta's contract?

No.

Bug found.

Notice something.

Nobody guessed.

They followed evidence.

Debugging Framework

Whenever something fails:

Ask:

Where?

Client?

Network?

API?

Database?

Business Logic?

What changed?

Always ask.

In this case:

Only one thing changed.

A single field.

"version"
Who owns the contract?

Meta.

Not you.

Therefore...

Your code must adapt.

Never the opposite.

Let's Understand the Bug Deeply

Expected

{
  "screen":"ORDER",
  "data":{}
}

Actual

{
  "version":"6.0",
  "screen":"ORDER",
  "data":{}
}

Humans say:

Only one extra field.

Computers say:

Different schema.

Imagine this interview question.

Interviewer:

Why can adding one JSON field break an API?

Because many APIs validate responses against a predefined schema. If the schema is strict, unexpected fields can cause validation to fail, even if the rest of the payload is correct. When integrating with third-party systems, following the documented contract exactly is essential.