## A Django Graphql (Graphene)

This is a simple Django Graphql (Graphene) project.

## Installation

1. Clone the repository
2. Create a virtual environment with Python 3.6
3. Install dependencies from requirements.txt
4. Run migrations
5. Run the server
6. Go to http://localhost:8000/graphql
7. Run the following query:

### Mutations

Create a new user:

```
mutation{
  createUser(email:"test@mail.com",name:"test",isActive:true,password:"pass"){
    user{
      name
      email
      id
    }
  }
}
```

Update a user:

```
mutation{
  updateUser(id:4,email:"update",name:"test",isActive:false,password:"pass"){
    user{
      name
      email
      isActive
    }
  }
}
```

Delete a user:

```
mutation{
  deleteUser(id:4){
    user{
      name
    }
  }
}
```

### Queries

Get all users:

```
query{
  allUsers{
    name
    email
    id
    isActive
  }
}


```

Get a user by id:

```
query{
  user(id:4){
    id
    name
    email
  }
}

```