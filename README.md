## Practice for data engineering

### What each folder
Explain the meaning of each type of folder.
<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th>✅&nbsp; oop </th>
      <th>✅&nbsp; pattern</th>
      <th>✅    &nbsp; BlobAzure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
Folder for learning OOP
like inherited , encapsulate ..etc
      </td>
      <td>
      Folder for learning desgin pattern
      <li>
abstract factory
</li>
<li>
Builder factory
</li>
<li>
...etc
</li>
and update later
      </td>
      <td>
      Folder for imprement code with azure and repostiory pattern
      </td>
      </tr>
  </tbody>
</table>


### Getting started
**Required**
docker init database in code here use **Options**( Postgresql ) In other you don't need to use the above.

```zsh
poetry install  
```
For installation dependencies required


setup .env in root dir for use azure blob with key vault like this 

``` python
## config azure blob
STORAGEACCOUNTURL= ....
SAS_TOKEN = .....
CONTAINERNAME= .....


## config db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=test
POSTGRES_USER=root
POSTGRES_PASSWORD=abc

```



