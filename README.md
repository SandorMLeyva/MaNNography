# MaNNography

## Dataset Builder

In the `mannography` folder run the following to create the database:

```python
python datasetBuilder.py createdb
```

Then, generate the dataset run:

```python
python datasetBuilder.py path/to/dataset
```

`path/to/dataset` should be the parent directory of the `classes`, for example:

    dataset/
    ├── normals/
    ├── benign_without_callbacks/
    ├── cancers/
    └── benigns/

Here, the path would end in `dataset/`.