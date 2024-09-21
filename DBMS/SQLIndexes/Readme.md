Indexes are used for efficient querying, they are used on Tables as well as Views.

```
CREATE IX_TABLENAME_COLUMN on TableName (Column ASC) - This  is a generic format
```

How Indexes Work : https://www.youtube.com/watch?v=lYh6LrSIDvY

Types of Index
1. Non Clustered
2. Clustered
3. Unique
4. Filtered
5. XML
6. Full Text
7. Spatial
8. Column Store
9. Index with Included Columns
10. Index on Computed Colums

How Ever, Clustered, Non Clustered and Unqiue are mostly used.
## Clustered and Non Clustered Index
1. Non Clustered ( Similar to index Page on a Book)
2. Clustered ( Similar to Telephone Directory) and Primary Key Constraint creates Clustered index automatically if no clustered index already exists on the table.

### Clustered

A Clustered Index determines the physical order of data in a table. (Basically they sort the data). __A Table can only have one Clustered Index, However that Index can be a composite Index__. 

```
Composite Clustered Index
CREATE CLUSTERED INDEX IX_TABLENAME_GENDER_SALARY on TABLENAME(GENDER DESC, SALARY ASC)
```
