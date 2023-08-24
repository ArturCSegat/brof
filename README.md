# brof
CLI utility for automagically updating a file if its brother is modified, useful for my dotfiles

## Install 

`pip install brof`

## Usage

### Show current pairs/brothers

`python -m brof -show`

### Remove a single pair/brothers

`python -m brof -remove foo.txt bar.txt`

### Delete all pairs/brothers

`python -m brof -clear`

### Add a new pair/brothers

`python -m brof -add foo.txt bar.txt`

### Add a new pair/brother of directories

`python -m brof -dir foo bar`

### Refresh existing pairs/brothers 

`python -m brof -refresh`
