the code according to architecture should be as follows in which each service has a predefined game plan of the four layers in it

file  architecture :
organizer/
musician/
booking/
matching/
rating/
notification/

what was the criteria used for creating these modules or even the thought process.

each module having:
controller.py

service.py

repository.py

models.py--what does thisone do 

schemas.py-- and this one.

considering all this what do we do first lets say we have created these files and all

Takudzwa...

**This question tells me your thinking is changing.**

You're no longer asking:

> "How do I write this code?"

You're asking:

> **"Why is the architecture shaped this way?"**

That is exactly how software architects think.

Today I want to teach you one of the biggest lessons you'll ever learn.

---

# Systems Engineering Lab

# How Architects Think Before They Write Code

## First Principle

Forget Python.

Forget Java.

Forget FastAPI.

Imagine computers don't exist.

You're building a company.

---

Imagine you start your musician marketplace.

You hire six people.

Who do you hire?

Probably someone for:

* Organisers
* Musicians
* Bookings
* Matching
* Ratings
* Notifications

Wait...

Doesn't that look familiar?

```
organizer/
musician/
booking/
matching/
rating/
notification/
```

Exactly.

---

## The Biggest Mistake Beginners Make

Most beginners organize projects like this:

```
controllers/

services/

repositories/

models/
```

Looks clean.

Until you have

```
60 controllers

80 services

120 models

70 repositories
```

Now finding code becomes difficult.

Instead we organize around **business capabilities**.

---

# This is called Vertical Slice Architecture (Feature-Based Architecture)

Instead of organizing by technical type...

We organize by **business responsibility**.

```
booking/

matching/

rating/

notification/
```

Each folder owns one capability.

Think of each folder as a mini business.

---

# Where did these modules come from?

Excellent question.

They did NOT come from Python.

They did NOT come from FastAPI.

They came from the DOMAIN.

Remember Day 1?

We asked:

"What exists in reality?"

Let's look.

Church wants musician.

↓

Matching happens.

↓

Booking happens.

↓

Notifications happen.

↓

Ratings happen.

Each major business capability became a module.

---

# Rule 1

## Modules come from Business Capabilities.

NOT database tables.

NOT endpoints.

NOT classes.

---

# How do we discover modules?

We ask one question.

> If this business hired different departments...

What departments would exist?

For your platform.

```
Registration

Matching

Booking

Payments

Notifications

Ratings

Analytics
```

Each becomes a module.

---

# The Thought Process

Let's build it from scratch.

Step 1

Understand workflow.

```
Organiser creates opportunity
```

Question.

Who owns this?

Organizer module.

---

Next.

```
Find musicians
```

Who owns this?

Matching.

---

Next.

```
Booking confirmed
```

Booking module.

---

Next.

```
Notify everyone
```

Notification module.

---

Next.

```
Leave rating
```

Rating module.

---

Notice something.

We didn't mention code once.

Architecture follows the business.

---

# Now let's open one module.

```
booking/
```

Inside.

```
controller.py

service.py

repository.py

models.py

schemas.py
```

Let's understand WHY.

---

# Layer 1

## Controller

Think receptionist.

Student says

```
POST /booking
```

Controller says

```
Okay.

I'll pass this to Booking Service.
```

That's all.

Controllers should be boring.

---

# Layer 2

## Service

This is the brain.

Business thinking happens here.

Example.

```
Can musician accept?

Is booking overlapping?

Calculate score.

Reserve booking.

Generate event.
```

Business logic lives here.

---

# Layer 3

## Repository

Repository speaks SQL.

Service says

```
Find booking
```

Repository translates.

```
SELECT ...
```

Service doesn't know SQL.

Repository does.

---

# Layer 4

## Models

This is one students confuse.

There are actually TWO kinds of models.

---

## Database Models

These represent database tables.

Example.

```python
class Booking:
```

Contains

```
id

musician_id

organizer_id

status
```

This is usually SQLAlchemy.

It represents persistence.

---

Think of models as

> "How my data lives."

---

# Schemas

These are different.

Schemas describe

> "How data travels."

Example.

Client sends

```json
{
   "date":"..."
}
```

Pydantic converts that JSON into

```python
BookingCreate
```

Later.

You return

```python
BookingResponse
```

Schemas represent communication.

---

Think

```
Models

↓

Database
```

Schemas

↓

API

---

Example

Student sends

```json
{
"name":"Takudzwa"
}
```

Schema validates.

Model saves.

Notice.

Different jobs.

---

# Analogy

Imagine a passport office.

Person

↓

Passport Form

↓

Government Database

The form

is Schema.

Government record

is Model.

They're not the same.

---

# Why Separate Them?

Imagine database has

```
password_hash
```

Should API return it?

Absolutely not.

Model

```
password_hash
```

Schema

Doesn't include it.

Beautiful.

---

# Why Not Use Models Everywhere?

Because the API and the database evolve differently.

Tomorrow.

Database adds

```
created_at
```

Should client receive it?

Maybe.

Maybe not.

Schemas give us control.

---

# Let's Build Booking Module

Imagine user presses

Accept Booking.

Journey.

```
HTTP Request
```

↓

Controller

```python
booking_controller.accept_booking()
```

↓

Service

```python
booking_service.accept()
```

↓

Repository

```
Find booking

Update booking
```

↓

Database

↓

Repository

↓

Service

↓

Controller

↓

JSON Response

---

Notice.

Each layer has ONE responsibility.

---

# What do we build FIRST?

This...

is the question professionals ask.

Many beginners start here.

```
Controller
```

Wrong.

Because controller doesn't know business.

---

Professional order.

## Step 1

Understand domain.

Already done.

---

## Step 2

Business Rules.

Example.

```
Musician cannot accept overlapping bookings.
```

---

## Step 3

Models

Because we need to understand

"What exists?"

Example.

```python
Booking

Musician

Invitation
```

---

## Step 4

Schemas

What enters?

What leaves?

Example.

```
BookingCreate

BookingResponse
```

---

## Step 5

Repository

How do we save?

---

## Step 6

Service

How does business work?

---

## Step 7

Controller

Expose through HTTP.

---

Notice something.

HTTP comes LAST.

Business comes FIRST.

---

# The Real Thought Process

Professional engineers think like this:

```
Business

↓

Rules

↓

Objects

↓

Data

↓

Logic

↓

Storage

↓

API
```

NOT

```
FastAPI

↓

Controller

↓

Hope
```

😂

---

# Applying This to Tengai

Suppose you're building Orders.

You'd first ask:

### What is an Order?

Not a table.

A business agreement between a customer and a vendor.

---

Then ask:

### What rules exist?

* Vendor must be open.
* Menu item must exist.
* Customer must choose pickup point.
* Order cannot be accepted twice.

---

Then:

### What data represents an Order?

Now create the model.

---

Then:

### What should clients send?

Create `OrderCreateSchema`.

---

Then:

### How do I store it?

Repository.

---

Then:

### What business logic?

Service.

---

Finally:

### How do clients call it?

Controller.

---

# Founder Lesson

This is why I keep telling you:

> **Your API is not your product.**

Your controllers are merely doors into your business.

The real value of Tengai is not:

```
POST /orders
```

The real value is:

* Matching vendors
* Reliable ordering
* Smart workflows
* Great customer experience

The API simply exposes that value.

---

# Your Homework (No Coding Yet)

Before writing a single line of Python, I want you to take one feature—**Booking**—and write a one-page design answering these questions:

1. **What problem does the Booking module solve?**
2. **What business rules does it enforce?**
3. **What entities does it work with?**
4. **What events can happen?** (e.g., `BookingRequested`, `BookingConfirmed`, `BookingCancelled`, `BookingCompleted`)
5. **What data comes into the system?** (future `BookingCreate` schema)
6. **What data leaves the system?** (future `BookingResponse` schema)
7. **What data must be stored permanently?** (future `Booking` model)
8. **What responsibilities belong in the service?**
9. **What database operations belong in the repository?**
10. **What HTTP endpoints will the controller expose?**

If you can answer those ten questions **before opening your editor**, you've already done most of the difficult engineering work. The code then becomes the translation of a design you've already thought through.

That's the mindset we're building over these four months: **think like an architect first, then implement like an engineer.**
