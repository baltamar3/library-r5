# library-r5
library-r5 is a server application made using Django + Postgres + Graphql.

The application aims to search for books in different data sources, mainly from an internal database, as well as two external sources (Google and Gutendex)

## Base URL
https://library-r5.herokuapp.com/graphql

all requests require an authentication header:
```
Authorization: Bearer <Your-Token>
```

#### 1. Obtain token

Credentials:
```
username: admin
password: 123456
```

```
mutation TokenAuth($username: String!, $password: String!) {
  tokenAuth(username: $username, password: $password) {
    token
    payload
    refreshExpiresIn
  }
}
```

Example:
![image](https://user-images.githubusercontent.com/20992846/236375369-1c7987bd-ee86-46e3-bdf5-45ab64794df6.png)

#### 2 Search book query
```
query{
    books(query:"Aventutas de don gato"){
        id
        source
        title
        categories
        authors
        categories
        description
        image
    }
}
```

#### 3 Delete book
```
mutation{
    deleteBook(id:6){
        book{
            title
        }
    }
}
```
#### 4 Create book (Source:db)
```
mutation{
    createBook(input: {source: "db", title: "Aventuras de juanito", subtitle:"Don juanito", categories:"Humor, Ficción", authors: "Monica Florez", description: "Test description", publisher:"Editorial SAS", publicationDate:"2023"}){
        title
        errors{
            field
            messages
        }
    }
}
```

#### 5 Create book (Source:google)
```
mutation{
    createBook(input: {source: "google", externalId:"wl2MclqgHeEC"}){
        title
        errors{
            field
            messages
        }
    }
}
```

#### 6 Create book (Source:gutendex)
```
mutation{
    createBook(input: {source: "gutendex", externalId:"51689"}){
        title
        errors{
            field
            messages
        }
    }
}
```
