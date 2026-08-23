## GOAL
1. Deeply understand Onion Architecture (specifically the "Core Domain") from first principles .
2. Define my core domain classes (Student, Vendor, Order) in pure, dependency-free Python inside a `domain/models.py` file.
3. Understand why this layer must have ZERO external framework imports (no ORM, no SQLAlchemy, no FastAPI, no Pydantic)


## What I learned?
- Onion architecture is all about the separation of unchangeable core business rules(entities and all) that dont really change with the external possible dependencies. Thus teh core domain should be proytected from the outside world
- Center:Core Domain- The student,order,vendor enytities and the business rules 
- App Services: These are the use cases PlaceOrder,AcceptOrder,MarkReady...what we do in the system.
- Adapters/Interfaces: The external delivery drivedrs that handle the receiving,sending of data within the system(whatsapp flow handler,fastapi webhook,postgresql repo,whatsapp message sender.)
- Infrastructure: Specific teh we are interacting with(looking at other pieces of tech we use just look at the .env file the keys there tell you the tech we are using and all as well as the imports /libraries)

  ## Connections
  - The dependencies point inwards and all(the center sees nothing outside- the outside report to the center)

This lesson connects to:
-Domain Driven design 
- software engineering
- Separation of concerns and all 
- Changes and migrations
