# brof
CLI utility for automagically updating a file if its brother is modified, useful for my dotfiles

## Install 

`pip install brof`
### Problem

Currently you need to create a file_pairs.json file in the directory you want to use this, so its nor really useful, windows fix coming soon

## Usage

### Show current pairs/brothers

`python -m brof -show`

### Delete all pairs/brothers

`python -m brof -clear`

### Add a new pair/brother

`python -m brof -add foo.txt bar.txt`

### Add a new pair/brother of directories

`python -m brof -dir foo bar`

### Refresh existing pairs/brothers 

`python -m brof -refresh`
